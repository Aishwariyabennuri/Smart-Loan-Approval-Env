from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from env.loan_env import LoanEnv

app = FastAPI()

class ActionRequest(BaseModel):
    action: str

@app.post("/reset")
def reset():
    env = LoanEnv("easy")
    app.state.env = env
    return {"state": env.reset()}

@app.post("/step")
def step(req: ActionRequest):
    env = getattr(app.state, "env", None)
    state, reward, done, info = env.step(req.action)
    return {"state": state, "reward": reward, "done": done, "info": info}

@app.get("/state")
def state():
    env = getattr(app.state, "env", None)
    return {"state": env.state if env else None}

def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
