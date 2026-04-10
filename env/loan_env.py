import random

class LoanEnv:
    def __init__(self,task="easy"):
        self.task=task
        self.current_state = None

    def reset(self):
        self.current_state = self._get_task_state()
        return self.current_state
    
    def state(self):
        return self.current_state

    def step(self, action):
        default = self._simulate_default(self.current_state)

        if action == "approve":  #1
            reward = 1.0 if not default else 0.0
        elif action == "reject": #0
            reward = 0.7 if default else 0.3
        else:
            return self.current_state, 0.0, True, {"error": "invalid_action"}
        done = True
        return self.current_state, reward, done, {}

    def _simulate_default(self, state):
        # Simple logic for default probability
        score = 0

        if state["income_stability"] == "stable":
            score += 1
        if state["credit_history"] == "":
            score += 1
        if state["employment_type"] == "salaried":
            score += 1
        if state["loan_amount"] < 50000:
            score += 1
            
        return score < 2
    
    def _get_task_state(self):
        if self.task == "easy":
            return {
                "income_stability": "stable",
                "credit_history": "good",
                "employment_type": "salaried",
                "loan_amount": 20000
            }
        elif self.task == "medium":
            return {
                "income_stability": "stable",
                "credit_history": "bad",
                "employment_type": "self-employed",
                "loan_amount": 70000
            }
        else:
            return {
                "income_stability": "unstable",
                "credit_history": "good",
                "employment_type": "self-employed",
                "loan_amount": 120000
            }