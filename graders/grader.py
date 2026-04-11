def compute_score(rewards: list[float]) -> dict:
    if not rewards:
        return {"avg_reward": 0.0, "total_episodes": 0}
    
    return {
        "avg_reward": round(sum(rewards) / len(rewards), 4),
        "total_episodes": len(rewards),
        "best_reward": max(rewards),
        "worst_reward": min(rewards)
    }
