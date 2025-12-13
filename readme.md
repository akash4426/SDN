# 🛡️ SDN – Self-Healing Software Defined Network (ML + RL)

[![Repository](https://img.shields.io/badge/repo-akash4426/SDN-blue.svg)](https://github.com/akash4426/SDN)
[![Issues](https://img.shields.io/github/issues-raw/akash4426/SDN)](https://github.com/akash4426/SDN/issues)
[![Top Language](https://img.shields.io/github/languages/top/akash4426/SDN)](https://github.com/akash4426/SDN)
[![Lines of Code](https://img.shields.io/tokei/lines/github/akash4426/SDN)](https://github.com/akash4426/SDN)

A complete **Self-Healing SDN System** that uses  
🧠 **Machine Learning (XGBoost)** for DDoS attack detection and  
🤖 **Reinforcement Learning (PPO)** for autonomous mitigation decisions.

Built as part of **20CYS303 – Computer Networks**, this project demonstrates an intelligent SDN controller that automatically detects attacks and chooses the best mitigation action.

---

## 📌 Table of Contents
- [About](#about)
- [Demo / Screenshots](#demo--screenshots)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Getting Started](#getting-started)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Results](#results)
- [Research Question](#research-question)
- [Novelty](#novelty)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Contact](#contact)

---

## 📘 About

This project aims to build a **Self-Healing SDN controller** capable of:

1. **Detecting DDoS attacks in real time** using an XGBoost classifier  
2. **Taking optimal mitigation actions** using PPO reinforcement learning  
3. Operating autonomously without human intervention  
4. Learning how attacks behave through flow statistics

We use **CIC-DDoS2019 Parquet datasets** as real SDN-like flow records.

---

## 🎥 Demo / Screenshots

> **Interactive Streamlit Dashboard**  
> - Upload a CSV flow  
> - ML model classifies: Attack / Benign  
> - RL agent chooses mitigation action  
> - Shows probability, graphs, and decision reasoning
> 
---

## ⭐ Features
- High-accuracy **binary ML attack detector**
- PPO-based **mitigation action selection**
- Flow-level SDN statistics:
  - FLOW PACKETS/S  
  - FLOW BYTES/S  
  - FWD HEADER LENGTH  
  - BWD HEADER LENGTH  
- Fully responsive **Streamlit UI**
- Supports:
  - Random flow generation  
  - CSV upload  
  - Real-time probability plots  
- Modular architecture (easy to integrate with Ryu/ONOS later)

---

## 🛠 Tech Stack

### **Languages**
- Python 3.11

### **Libraries**
- XGBoost  
- Stable-Baselines3  
- Gymnasium  
- Pandas / NumPy  
- Matplotlib / Seaborn  
- Streamlit  

### **Dataset**
- CIC-DDoS2019 (Parquet formatted)

---

## 🏗 Project Architecture



Add your GIF at:

**Pipeline Flow:**

Flow → ML Detector → Attack Probability → RL Agent → Optimal Mitigation

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

---

## 📌 Usage Examples

### ✨ **Random Flow Demo**
The app automatically samples one flow and shows:
- ML Prediction  
- RL Mitigation Action  
- Visual probability graphs  

### ✨ **Upload a Custom Flow**
Upload a **single-row CSV** with your flow features:

---

## 🧪 Testing

Run the ML detector testing code inside the notebook or Jupyter environment.

Run PPO RL simulation:

---

## 📊 Results

### 🔹 ML Detection
- **Accuracy:** ~99.2%
- **AUC:** ~0.99  
- **Very strong attack/benign separation**

### 🔹 RL Mitigation
- Learns to:
  - Block high-intensity attacks  
  - Rate-limit moderate ones  
  - Avoid unnecessary blocking of benign flows  
- Achieves high cumulative rewards over episodes  

---

## ❓ Research Question

**How can an SDN controller automatically detect and mitigate multi-vector DDoS attacks using a combined Machine Learning + Reinforcement Learning approach?**

---

## 🚀 Novelty

This project introduces **a hybrid SDN security framework**:
1. **ML detector** for DDoS identification  
2. **RL-based mitigation** mimicking autonomous controllers  
3. Uses **flow-level metrics** suitable for real SDN switches  
4. Solves a key research gap:  
   *Most SDN systems detect, but do NOT autonomously mitigate attacks.*

---

## 🗺 Roadmap
- Integrate with **Ryu SDN controller**  
- Add **real OpenFlow packet-in actions**  
- Multi-agent RL  
- Zero-day attack generalization  
- Cloud-scale datasets  

---

## 🤝 Contributing

1. Fork the project  
2. Create a feature branch  
3. Commit your changes  
4. Submit a PR  


---

## ✍️ Authors
- **Akash Karri** — Project Author  

---

## 📧 Contact
For queries:  
**akash4426@users.noreply.github.com**

