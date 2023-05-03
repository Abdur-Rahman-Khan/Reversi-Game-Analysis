import core
import copy
import math
import random
import minmaxLogic

def get_move(board, player):
    # return get_move_random(board, player)
    # return get_move_min(board,player)
    # return get_move_max(board, player)
    # return get_move_minmax(board, player)
    if player == core.BLACK:
        return get_move_max(board, player)
        # return get_move_minmax(board, player)
        # return get_move_min(board,player)
    else:
        # return get_move_random(board, player)
        # return get_move_max(board, player)
        # return get_move_minmax(board, player,4)
        # return get_move_freys(board, player)
        return get_move_morbius(board, player)

freysMat = [[100, -50, 20, 10, 10, 20, -50, 100],
          [-50, -80, -1, -1, -1, -1, -80, -50],
          [20, -1, 5, 2, 2, 5, -1, 20],
          [10, -1, 2, 1, 1, 2, -1, 10],
          [10, -1, 2, 1, 1, 2, -1, 10],
          [20, -1, 5, 2, 2, 5, -1, 20],
          [-50, -80, -1, -1, -1, -1, -80, -50],
          [100, -50, 20, 10, 10, 20, -50, 100]]

morbiusMat = [
    [99, -27, 11, 6, 6, 11, -27, 99],
    [-27, -38, -3, -3, -3, -3, -38, -27],
    [11, -3, 5, 1, 1, 5, -3, 11],
    [6, -3, 1, 1, 1, 1, -3, 6],
    [6, -3, 1, 1, 1, 1, -3, 6],
    [11, -3, 5, 1, 1, 5, -3, 11],
    [-27, -38, -3, -3, -3, -3, -38, -27],
    [99, -27, 11, 6, 6, 11, -27, 99]
]




   
def get_move_max(board,player):
    # test.print_board(board)
    board_copy = copy.deepcopy(board)
    valid_moves = core.get_valid_moves(board_copy,player)
    if len(valid_moves) == 0:
        return "NO MOVES"
    else:
        #iterate on all moves
        bestMove = valid_moves[0]
        bestMoveArr=[]
        minScore=  core.get_score(board)[player]
        for move in valid_moves:
            board_copy = copy.deepcopy(board)
            core.make_move(board_copy,move[0],move[1],player)
            #check if move is better
            # print("move is: ",move," score is: ",core.get_score(board_copy)[player])
            if core.get_score(board_copy)[player] > minScore:
                # bestMoveArr=[]
                bestMove = move
                bestMoveArr.append(bestMove)
                minScore = core.get_score(board_copy)[player]
                # print("best move is: ",bestMove)
            elif core.get_score(board_copy)[player] == minScore:
                bestMoveArr.append(move)
                # print("Equal move is: ",bestMove)
            # else:
            #     bestMoveArr.append(move)
        if len(bestMoveArr) > 1:
            #choose random move
            bestMove = bestMoveArr[random.randint(0,len(bestMoveArr)-1)]
        bestMove = convertToTuple(bestMove)
        # print("best move is: ",bestMove)
        return bestMove
    
def get_move_min(board,player):
    # test.print_board(board)
    board_copy = copy.deepcopy(board)
    valid_moves = core.get_valid_moves(board_copy,player)
    if len(valid_moves) == 0:
        return "NO MOVES"
    else:
        #iterate on all moves
        bestMove = valid_moves[0]
        bestMoveArr=[]
        board_copy = copy.deepcopy(board)
        minScore=  core.get_score(board_copy)[player]+100
        for move in valid_moves:
            board_copy = copy.deepcopy(board)
            core.make_move(board_copy,move[0],move[1],player)
            #check if move is better
            # print("move is: ",move," score is: ",core.get_score(board_copy)[player])
            if core.get_score(board_copy)[player] < minScore:
                bestMoveArr=[]
                bestMove = move
                bestMoveArr.append(bestMove)
                minScore = core.get_score(board_copy)[player]
                # print("best move is: ",bestMove)
            elif core.get_score(board_copy)[player] == minScore:
                bestMoveArr.append(move)
                # print("Equal move is: ",bestMove)
        # print(len(bestMoveArr))
        if len(bestMoveArr) > 1:
            #choose random move
            bestMove = bestMoveArr[random.randint(0,len(bestMoveArr)-1)]
        bestMove = convertToTuple(bestMove)
        # print("best move is: ",bestMove)
        return bestMove
def get_move_random(board,player):
    # test.print_board(board)
    board_copy = copy.deepcopy(board)
    valid_moves = core.get_valid_moves(board_copy,player)
    if len(valid_moves) == 0:
        return "NO MOVES"
    else:
        #iterate on all moves
        bestMove = valid_moves[0]
        bestMoveArr=[]
        board_copy = copy.deepcopy(board)
        minScore=  core.get_score(board_copy)[player]
        for move in valid_moves:
            bestMoveArr.append(move)
                # print("Equal move is: ",bestMove)
        if len(bestMoveArr) > 1:
            #choose random move
            bestMove = bestMoveArr[random.randint(0,len(bestMoveArr)-1)]
        bestMove = convertToTuple(bestMove)
        # print("best move is: ",bestMove)
        return bestMove
    
#convert (2,2) to (c3)
def convertToTuple(move):
    x = chr(move[0]+97)
    y = move[1]+1
    return (x,str(y))
    # return x+str(y)


def get_move_minmax(board, player,depth=3):
    mover= minmaxLogic.minimax(board,depth, player, float('-inf'), float('inf'), True)[0]
    # print("mover is: ",mover)
    mover= convertToTuple(mover)
    return mover

def get_move_freys(board,player):
    board_copy = copy.deepcopy(board)
    valid_moves = core.get_valid_moves(board_copy,player)
    if len(valid_moves) == 0:
        return "NO MOVES"
    else:
        #iterate on all freys moves
        bestMove = valid_moves[0]
        bestMoveArr=[]
        maxScore=  freysMat[bestMove[0]][bestMove[1]]
        for move in valid_moves:
            if freysMat[move[0]][move[1]] > maxScore:
                bestMoveArr=[]
                bestMove = move
                bestMoveArr.append(bestMove)
                maxScore = freysMat[move[0]][move[1]]
            elif freysMat[move[0]][move[1]] == maxScore:
                bestMoveArr.append(move)
        if len(bestMoveArr) > 1:
            #choose random move
            bestMove = bestMoveArr[random.randint(0,len(bestMoveArr)-1)]
        bestMove = convertToTuple(bestMove)
        return bestMove
    
def get_move_morbius(board,player):
    board_copy = copy.deepcopy(board)
    valid_moves = core.get_valid_moves(board_copy,player)
    if len(valid_moves) == 0:
        return "NO MOVES"
    else:
        #iterate on all freys moves
        bestMove = valid_moves[0]
        bestMoveArr=[]
        maxScore=  morbiusMat[bestMove[0]][bestMove[1]]
        for move in valid_moves:
            if morbiusMat[move[0]][move[1]] > maxScore:
                bestMoveArr=[]
                bestMove = move
                bestMoveArr.append(bestMove)
                maxScore = morbiusMat[move[0]][move[1]]
            elif morbiusMat[move[0]][move[1]] == maxScore:
                bestMoveArr.append(move)
        if len(bestMoveArr) > 1:
            #choose random move
            bestMove = bestMoveArr[random.randint(0,len(bestMoveArr)-1)]
        bestMove = convertToTuple(bestMove)
        return bestMove
