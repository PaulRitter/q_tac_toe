from q_algos.agents import playeragent
from .agents import Agent, RandomAgent, QAgent, PlayerAgent
import tic_tac_toe

def get_agent(choice: str) -> Agent:
    if choice == "random":
        return RandomAgent()
    if choice == "q":
        return QAgent(0.2, 0.7, len(tic_tac_toe.state_indices), 9)
    if choice == "player":
        return PlayerAgent()
    raise Exception("invalid agent")

print("Agent choices: (random/q/player)")
agent1 = get_agent(input("Agent1:"))
agent2 = get_agent(input("Agent2:"))

game = tic_tac_toe.TicTacToeGame()
while True:
    print("Starting new game...")
    game.reset()
    while True:
        state = game.get_state_idx()
        action = agent1.get_action(state)
        x = int(action / 3)
        y = action % 3
        new_state = game.get_state_idx()
        reward = 1
        if not game.make_move(x, y, 1):
            reward = -10
            print("Invalid move, you lost!")
            break
        if game.check_win(1):
            agent1.update_weights(state )

        agent1.update_weights(state, action, new_state, -10)