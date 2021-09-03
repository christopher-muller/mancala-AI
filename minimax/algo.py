from copy import deepcopy
from mancala.constants import RED, WHITE
import pygame

def minimax(position, depth, alpha, beta, turn, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if turn:
        maxEval = float('-inf')
        best_move = [None, None]
        for move in get_all_moves(position, 0, game):
            if move[1] == 1:
                evaluation = minimax(move[0], depth, alpha, beta, True, game)[0]
            else:     
                evaluation = minimax(move[0], depth-1, alpha, beta, False, game)[0]
            if evaluation > maxEval:
                best_move = move
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
            
        return maxEval, best_move[0]
    else:
        minEval = float('inf')
        best_move = [None, None]
        for move in get_all_moves(position, 1, game):
            if move[1] == 1:
                evaluation = minimax(move[0], depth, alpha, beta, False, game)[0]
            else:     
                evaluation = minimax(move[0], depth-1, alpha, beta, True, game)[0]
            if evaluation < minEval:
                best_move = move
            minEval = min(minEval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
            
        return minEval, best_move[0]

def simulate_move(board, row, col):
    turn = board.move(row, col)
    
    return board, turn


def get_all_moves(board, turn, game):
    moves = []

    for stack in board.get_all_stacks(turn):
        temp_board = deepcopy(board)
        new_board, free = simulate_move(temp_board, turn, stack)
        if free == turn:
            free = 1
        else:
            free = 0
        moves.append([new_board, free])
    
    return moves
