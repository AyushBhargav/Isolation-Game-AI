from minimax_helper import *

def minimax_decision(gameState, depth):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    """
    if gameState.player == 0:
        apply_func = min_value
        stat = 1
    else:
        apply_func = max_value
        stat = -1
    for move in gameState.get_legal_moves():
        n_gameState = gameState.forecast_move(move)
        status = apply_func(n_gameState, depth-1)
        if status == stat:
            return move
