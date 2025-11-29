# 🛡️ Self-Healing SDN Against DDoS Attacks  
### Machine Learning + Reinforcement Learning Based Autonomous Mitigation System

This project implements an intelligent **Self-Healing Software Defined Network (SDN)** that automatically **detects DDoS attacks using XGBoost** and **mitigates them using PPO Reinforcement Learning**. The system works in two stages:  
1. ML-based attack detection  
2. RL-based optimal mitigation action selection  

This satisfies Phase-2 and Phase-3 requirements for the 20CYS303 Computer Networks Laboratory.

---

## 🚀 Key Features
- High-accuracy ML attack detector  
- RL agent chooses between:
  - No Action  
  - Block Source  
  - Rate Limit  
  - Redirect to Honeypot  
- Fully interactive Streamlit UI  
- Real CIC-DDoS2019 data  
- Demonstration-friendly dashboard  

---

## 📂 Project Structure


---

## 🧠 Research Question
**How can SDN automatically detect and mitigate multi-vector DDoS attacks using a hybrid ML + RL pipeline?**

---

## 🧪 Tools Used
- Python  
- Streamlit  
- XGBoost  
- Stable-Baselines3 (PPO)  
- Gymnasium  
- Pandas  
- NumPy  

---

## 📊 Results
### ML Detector
- Accuracy: **99%+**
- AUC: **0.99**
- Excellent separation of attack vs benign flows

### RL Mitigator
- Learns optimal actions:
  - Blocks high-confidence attacks  
  - Rate-limits moderate attacks  
  - Avoids false positives on benign traffic  

---

## 🔍 Novelty of This Work
- Hybrid **ML + RL** pipeline  
- Uses real SDN-like flow features  
- RL agent considers attack probability + flow intensity  
- Automatic mitigation (rare in academic SDN works)  
- Lightweight, deployable, real-time  

This solves the research gap:  
👉 *“Most SDN systems detect attacks but do not autonomously mitigate them.”*

---

## 🏁 Conclusion
- ML detect attacks accurately  
- RL decides best mitigation strategy  
- Combined system behaves like a self-healing SDN  
- Shows promise for real controller integration (Ryu/ONOS)

---

## 🔮 Future Work
- Integrate with real SDN controller  
- Multi-agent RL  
- Zero-day attack training  
- Extend to multi-class attack types  

---

## 🌐 How to Run Locally
Install dependencies:


---

## 📬 Contact  
**Author:** Akash Karri  

⭐ *If this helped you, consider starring the repo!* ⭐
