from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    def get_action(state_idx):
        return -1
    
    def update_weights(self, state, action, new_state, reward):
        return