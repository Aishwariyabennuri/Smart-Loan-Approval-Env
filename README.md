# 💰 Smart Loan Approval Environment

## 📌 What this project does
This project simulates a loan approval system where an AI agent decides whether to approve or reject a loan.

The goal is to mimic how banks make decisions — approving good customers while avoiding risky ones.

---

## 🌐 Live API

- Swagger UI: https://bennuri-smart-loan-approval-env.hf.space/docs

---

## 🧠 How the environment works

Each applicant (state) includes:

- income stability (stable / unstable)
- credit history (good / bad)
- employment type (salaried / self-employed)
- loan amount
- past defaults

---

## 🎮 Actions

The agent can:
- approve
- reject

---

## 🏆 Reward logic

Instead of simple correct/incorrect rewards, partial rewards are used:

- Approve + safe → 0.9  
- Approve + risky → 0.1  
- Reject + risky → 0.8  
- Reject + safe → 0.3  

This better reflects real-world trade-offs.

---

## 🎯 Tasks

### 1. Easy (low risk customers)
Clear approval cases

### 2. Medium (mixed signals)
Some good, some risky features

### 3. Hard (high uncertainty)
Ambiguous and risky cases

---

## ⚙️ API

- `POST /reset` → start new case  
- `POST /step` → take action  
- `GET /state` → view state  

---

## 🤖 Agent

An LLM is used as the decision-maker.  
It observes the state and chooses an action.

---

## 🧾 Sample Output
[START] task=easy_low_risk_customer env=loan-risk model=Qwen
[STEP] step=1 action=approve reward=0.90 done=true error=null
[END] success=true steps=1 score=0.90 rewards=0.90
## 🚀 Run locally

```bash
pip install -r requirements.txt
uvicorn server.app:app --host 0.0.0.0 --port 7860

Open:
http://127.0.0.1:7860/docs
