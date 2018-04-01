from copy import deepcopy

class GameState:

    def __init__(self, board_height, board_width):
        self.board_height = board_height
        self.board_width = board_width
        self.board = [[0 for _ in range(0,board_width)] for _ in range(0,board_height)]
        # 1 denotes occupied cell
        self.board[-1][-1] = 1
        self.player = 0
        self.current_position = [None,None] # [plater1, player2]

    def get_legal_moves(self):
        if not self.current_position[self.player]: # Game is starting, so whole board is valid
            legal_moves = [(c,r) for c in range(0,self.board_width) for r in range(0,self.board_height) if self.board[r][c] == 0]
            return legal_moves
        r,c = self.current_position[self.player]
        legal_moves = []
        for h_move in [1,0,-1]:
            for v_move in [1,0,-1]:
                if h_move == 0 and v_move == 0:
                    continue
                y,x = r,c
                while (y+v_move) not in [-1, self.board_height] and (x+h_move) not in [-1, self.board_width] and self.board[y+v_move][x+h_move] != 1:
                    y += v_move
                    x += h_move
                    legal_moves.append((x,y))
        return legal_moves
    
    def forecast_move(self, move):
        x,y = move
        new_game_state = deepcopy(self)
        new_game_state.board[y][x] = 1
        new_game_state.current_position[self.player] = (y , x)
        new_game_state.player = not new_game_state.player
        return new_game_state
        
    