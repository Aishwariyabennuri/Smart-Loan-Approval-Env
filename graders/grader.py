def compute_score(rewards):
    return sum(rewards) / len(rewards) if rewards else 0.0