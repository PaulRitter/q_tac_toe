from .randomagent import RandomAgent
import numpy as np
from random import uniform

class QAgent(RandomAgent):
    def __init__(self, eps, lr, state_len, action_len) -> None:
        self.eps = eps
        self.lr = lr
        self.Q = np.zeros((state_len, action_len))

    def get_action(self, state_idx):
        if(uniform(0,1) < self.eps):
            return super().get_action(state_idx)
        else:
            return np.argmin(self.Q[state_idx, :])

    def update_weights(self, state, action, new_state, reward):
        self.Q[state, action] = self.Q[state, action] + self.lr * ( reward + np.max(self.Q[new_state, :]) — self.Q[state, action] )