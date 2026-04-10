from fastapi import FastAPI
from pydantic import BaseModel
from env.loan_env import LoanEnv

app = FastAPI()

env = LoanEnv()

class ActionRequest(BaseModel):
    action: str

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(req: ActionRequest):
    state, reward, done, info = env.step(req.action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def get_state():
    return {"state": env.current_state}