import random
from .agent import Agent

class RandomAgent(Agent):
    def get_action(state_idx):
        return random.randint(0,8)

    def update_weights(self, state, action, new_state, reward):
        return