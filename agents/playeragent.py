from .agent import Agent

class PlayerAgent(Agent):
    def get_action(state_idx):
        return int(input("Choose an action(0 - 8):"))

    def update_weights(self, state, action, new_state, reward):
        return