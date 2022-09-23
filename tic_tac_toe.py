state_indices = dict()
idx = 0
def generate_state_indices(vec, i):
    if i > len(vec):
        return []
    res = list()
    for v in range(3):
        vec[i] = v
        state_indices[vec.copy()] = idx
        idx += 1
        res.extend(generate_state_indices(vec, i+1))

generate_state_indices([0]*9, 0)

def get_action_idx(x,y):
    return x * 3 + y

class TicTacToeGame():
    def __init__(self) -> None:
        self.field = [[0,0,0],[0,0,0],[0,0,0]]

    def make_move(self, x, y, id):
        if self.field[x][y] != 0:
            return False
        
        self.field[x][y] = id
        return True

    def check_win(self, id):
        for roworcolumn in range(3):
            if self.field[roworcolumn][0] == self.field[roworcolumn][1] == self.field[roworcolumn][2] == id:
                return True
            
            if self.field[0][roworcolumn] == self.field[1][roworcolumn] == self.field[2][roworcolumn] == id:
                return True

        if self.field[0][0] == self.field[1][1] == self.field[2][2] == id:
            return True
        
        if self.field[0][2] == self.field[1][1] == self.field[2][0] == id:
            return True

        return False

    def reset(self):
        for x in range(3):
            for y in range(3):
                self.field[x][y] = 0

    def get_state_idx(self):
        vec = [0]*9
        for x in range(3):
            for y in range(3):
                vec[x*3+y] = self.field[x][y]

