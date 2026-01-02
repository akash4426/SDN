import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from stable_baselines3 import PPO

# --------------------------------------------------------------
# LOAD MODELS + DATA
# --------------------------------------------------------------
@st.cache_resource
def load_all():
    clf = joblib.load("detector_xgb.pkl")
    scaler = joblib.load("detector_scaler.pkl")
    features = joblib.load("detector_features.pkl")
    rl_model = PPO.load("ppo_sdn_agent.zip")

    # Load dataset for random sampling
    df = pd.concat([
        pd.read_parquet("Dataset/MSSQL-training.parquet"),
        pd.read_parquet("Dataset/UDPLag-training.parquet"),
        pd.read_parquet("Dataset/Portmap-training.parquet"),
        pd.read_parquet("Dataset/UDP-training.parquet"),
        pd.read_parquet("Dataset/Syn-training.parquet"),
        pd.read_parquet("Dataset/NetBIOS-training.parquet"),
        pd.read_parquet("Dataset/LDAP-training.parquet"),
    ], ignore_index=True)

    df.columns = [c.upper() for c in df.columns]
    return clf, scaler, features, rl_model, df


clf, scaler, feature_cols, rl_model, df = load_all()

# --------------------------------------------------------------
# UI
# --------------------------------------------------------------
st.title("🛡️ SDN Self-Healing System (ML + RL)")
st.write("Upload one flow OR generate a random one.")

# --------------------------------------------------------------
# INPUT MODE
# --------------------------------------------------------------
choice = st.radio(
    "Select Input Mode:",
    ["Random Flow", "Upload CSV Row"]
)

sample = None

if choice == "Upload CSV Row":
    file = st.file_uploader(
        "Upload a CSV with EXACTLY ONE row",
        type=["csv"]
    )
    if file is not None:
        temp = pd.read_csv(file)
        if len(temp) != 1:
            st.error("❌ CSV must contain EXACTLY one row")
        else:
            sample = temp

if sample is None:
    sample = df.sample(1)

# --------------------------------------------------------------
# SHOW FLOW
# --------------------------------------------------------------
st.subheader("📌 Selected Flow")
st.dataframe(sample)

# --------------------------------------------------------------
# ML DETECTION
# --------------------------------------------------------------
X = sample[feature_cols].values
X_scaled = scaler.transform(X)

prob = float(clf.predict_proba(X_scaled)[0][1])
pred = "Attack" if prob >= 0.5 else "Benign"

c1, c2 = st.columns(2)
c1.metric("Predicted Class", pred)
c2.metric("Attack Probability", f"{prob:.4f}")

# --------------------------------------------------------------
# RL DECISION
# --------------------------------------------------------------
st.subheader("🤖 RL Agent Mitigation Decision")

def safe_get(row, col, default=0.0):
    if col in row:
        return float(row[col])
    return default

def make_obs(row):
    pkt = safe_get(row, "FLOW PACKETS/S")
    byte = safe_get(row, "FLOW BYTES/S")
    fwd = safe_get(row, "FWD HEADER LENGTH", 1.0)
    bwd = safe_get(row, "BWD HEADER LENGTH", 1.0)

    pkt_norm = pkt / (df["FLOW PACKETS/S"].max() + 1e-9)
    byte_norm = byte / (df["FLOW BYTES/S"].max() + 1e-9)
    fwd_norm = fwd / (df["FWD HEADER LENGTH"].max() + 1e-9)
    bwd_norm = bwd / (df["BWD HEADER LENGTH"].max() + 1e-9)

    return np.array(
        [prob, pkt_norm, byte_norm, fwd_norm, bwd_norm],
        dtype=np.float32
    ).reshape(1, -1)

obs = make_obs(sample.iloc[0])

# --------------------------------------------------------------
# ✅ RL ACTION (100% SAFE EXTRACTION)
# --------------------------------------------------------------
rl_action_raw, _ = rl_model.predict(obs, deterministic=True)

# THIS IS THE ONLY CORRECT WAY (works for [1], [[1]], etc.)
rl_action = int(rl_action_raw.item())

# --------------------------------------------------------------
# HYBRID DECISION FUSION
# --------------------------------------------------------------
if prob >= 0.995:
    final_action = 1          # Block Source
elif prob >= 0.90:
    final_action = 2          # Rate Limit
else:
    final_action = rl_action  # RL decides

actions_map = {
    0: "No Action",
    1: "Block Source",
    2: "Rate Limit",
    3: "Redirect to Honeypot"
}

st.metric(
    "Recommended Mitigation Action",
    actions_map.get(final_action, "Unknown")
)

# --------------------------------------------------------------
# VISUALIZATION
# --------------------------------------------------------------
st.subheader("📊 Detector Probability Visualization")

fig, ax = plt.subplots(figsize=(4, 1.5))
ax.barh(
    ["Attack Probability"],
    [prob],
    color="red" if prob >= 0.5 else "green"
)
ax.set_xlim(0, 1)
st.pyplot(fig)

st.success("Demo ready! 🚀")
