import os
from env.loan_env import LoanEnv
from tasks.tasks import TASKS
from graders.grader import compute_score

MODEL_NAME = os.getenv("MODEL_NAME", "baseline")

def run_task(task):
    env = LoanEnv(task)
    state = env.reset()

    rewards = []

    print(f"[START] task={task} env=loan-risk model={MODEL_NAME}")

    for step in range(1, 3):
        if state["credit_history"] == "good":
            action = "approve"
        else:
            action = "reject"

        state, reward, done, _ = env.step(action)
        rewards.append(reward)

        print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

        if done:
            break

    score = compute_score(rewards)
    success = score > 0.5

    rewards_str = ",".join([f"{r:.2f}" for r in rewards])

    print(f"[END] success={str(success).lower()} steps={len(rewards)} score={score:.2f} rewards={rewards_str}")

if __name__ == "__main__":
    for t in TASKS:
        run_task(t)