def compute_score(rewards):
    if not rewards:
        return 0.5

    score = sum(rewards) / len(rewards)

    if score <= 0.0:
        score = 0.01
    elif score >= 1.0:
        score = 0.99

    return round(score, 2)
