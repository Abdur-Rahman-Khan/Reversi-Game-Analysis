import core
import copy
def minimax(board, depth, player, alpha, beta, maximizing_player):
    if depth == 0:
        return None, core.get_score(board)[player]
    # print("depth is: ",depth)
    valid_moves = core.get_valid_moves(board, player)
    
    if len(valid_moves) == 0:
        if len(core.get_valid_moves(board, core.get_opponent(player))) == 0:
            return None, core.get_score(board)[player]
        else:
            return minimax(board, depth-1, core.get_opponent(player), alpha, beta, maximizing_player)
    
    if maximizing_player:
        max_score = float('-inf')
        best_move = None
        for move in valid_moves:
            new_board = core.make_move(copy.deepcopy(board), move[0], move[1], player)
            _, score = minimax(new_board, depth-1, core.get_opponent(player), alpha, beta, False)
            if score > max_score:
                max_score = score
                best_move = move
            alpha = max(alpha, max_score)
            if alpha >= beta:
                break
        return best_move, max_score
    
    else:
        min_score = float('inf')
        best_move = None
        for move in valid_moves:
            new_board = core.make_move(copy.deepcopy(board), move[0], move[1], player)
            _, score = minimax(new_board, depth-1, core.get_opponent(player), alpha, beta, True)
            if score < min_score:
                min_score = score
                best_move = move
            beta = min(beta, min_score)
            if beta <= alpha:
                break
        return best_move, min_score
