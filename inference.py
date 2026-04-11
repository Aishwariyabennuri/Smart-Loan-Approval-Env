import os
import logging
from openai import OpenAI
from env.loan_env import LoanEnv
from tasks import TASKS
from graders.grader import compute_score

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

if not API_BASE_URL or not API_KEY:
    raise ValueError("Missing API_BASE_URL or API_KEY")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

def get_action_from_llm(state: dict) -> str:
    prompt = f"""You are a strict loan approval agent.
Approve only if: income is stable, credit is good, employment is salaried, loan < 50000.
State: {state}
Reply with exactly one word: approve or reject"""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
        )
        raw = response.choices[0].message.content.strip().lower()
        return "approve" if "approve" in raw else "reject"  # ✅ robust parsing
    except Exception as e:
        log.error(f"LLM call failed: {e}")   # ✅ log the actual error
        return "reject"

def run_task(task: str) -> dict:
    env = LoanEnv(task)
    state = env.reset()
    log.info(f"[START] task={task} model={MODEL_NAME}")

    action = get_action_from_llm(state)        # ✅ single step (done=True always)
    state, reward, done, _ = env.step(action)

    score = compute_score([reward])
    success = score > 0.5
    log.info(f"[END] task={task} action={action} score={score:.2f} success={success}")

    return {"task": task, "action": action,    # ✅ return results instead of just printing
            "score": score, "success": success}

if __name__ == "__main__":
    results = [run_task(t) for t in TASKS]
    for r in results:
        print(r)
