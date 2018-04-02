def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    legal_moves = gameState.get_legal_moves()
    if len(legal_moves) == 0:
        return True
    return False


def min_value(gameState, depth):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if depth == 0:
        return 0
    v = 1
    for move in gameState.get_legal_moves():
        n_gameState = gameState.forecast_move(move)
        v = min(v, max_value(n_gameState, depth-1))
    return v


def max_value(gameState, depth):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if depth == 0:
        return 0
    v = -1
    for move in gameState.get_legal_moves():
        n_gameState = gameState.forecast_move(move)
        v = max(v, min_value(n_gameState, depth-1))
    return v
