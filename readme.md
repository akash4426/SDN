# 🛡️ SDN – Self-Healing Software Defined Network (ML + RL)

[![Repository](https://img.shields.io/badge/repo-akash4426/SDN-blue.svg)](https://github.com/akash4426/SDN)
[![License](https://img.shields.io/github/license/akash4426/SDN)](https://github.com/akash4426/SDN/blob/main/LICENSE)
[![Issues](https://img.shields.io/github/issues-raw/akash4426/SDN)](https://github.com/akash4426/SDN/issues)
[![Top Language](https://img.shields.io/github/languages/top/akash4426/SDN)](https://github.com/akash4426/SDN)
[![Lines of Code](https://img.shields.io/tokei/lines/github/akash4426/SDN)](https://github.com/akash4426/SDN)

A complete **Self-Healing SDN System** that uses  
🧠 **Machine Learning (XGBoost)** for DDoS attack detection and  
🤖 **Reinforcement Learning (PPO)** for autonomous mitigation decisions.

Built as part of **20CYS303 – Computer Networks Lab**, this project demonstrates an intelligent SDN controller that automatically detects attacks and chooses the best mitigation action.

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

Add your GIF at:
