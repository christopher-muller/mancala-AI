from mancala.constants import RED, SQUARE_SIZE, WHITE, BLUE
from mancala.board import Board
import pygame

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def _init(self):
        self.board = Board()
        self.turn = 1

    def winner(self):
        return self.board.winner()

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()
    
    def reset(self):
        self._init()

    def get_board(self):
        return self.board

    def select(self, row, col):
        if col > 0 and col < 7:
            if self.turn == 0 and row == 0:
                self.turn = self.board.move(row, col)
            if self.turn == 1 and row == 1:
                self.turn = self.board.move(row, col)

    def ai_move(self, board):
        self.board = board
        if board.free == 0:
            self.change_turn()

    def change_turn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0