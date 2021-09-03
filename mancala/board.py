import pygame
from .constants import BLACK, BROWN, RED, SQUARE_SIZE, WHITE, WIDTH, HEIGHT, COLS

class Board:
    def __init__(self):
        self.board = [[100, 4, 4, 4, 4, 4, 4, 100], [100, 4, 4, 4, 4, 4, 4, 100]]
        self.user_score = 0
        self.other_score = 0
        self.free = 0
    
    def draw(self, win):
        win.fill(BROWN)
        pygame.draw.rect(win, BLACK, (100, 100, 600, 10))
        for col in range(COLS - 1):
            pygame.draw.rect(win, BLACK, ((col + 1) * SQUARE_SIZE, 0, 10, 200))
        
        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        stack_count = 0
        row_num = 0
        for row in self.board:
            col_num = 0
            for stack in row:
                if stack >= 100:
                    stack_count = stack - 100
                    x, y = 45 + (col_num // 7 * 700), 80
                else:
                    stack_count = stack
                    x, y = 45 + col_num * 100, 45 + row_num * 100

                self.draw_text(win, myfont, str(stack_count), x, y)
                col_num += 1
            row_num += 1
        
    def evaluate(self):
        return self.other_score - self.user_score
    
    def draw_text(self, win, myfont, text, x, y):
        textsurface = myfont.render(text, False, WHITE)
        win.blit(textsurface, (x, y))
    
    def winner(self):
        if (self.user_score + self.other_score) == 48:
            if self.user_score > self.other_score:
                return "User Wins!"
            elif self.user_score < self.other_score:
                return "Opponent Wins!"
            elif self.user_score < self.other_score:
                return "Draw!"
            else:
                return None

    def move(self, row, col):
        num_stack = 0
        if row == 0:
            return self.update_stacks(row, col , -1, 0)

        if row == 1:
            return self.update_stacks(row, col , 1, 1)
    
    def update_stacks(self, row, col, step, turn):
        num_stack = self.board[row][col]
        self.board[row][col] = 0
    
        for piece in range(num_stack):
            col += step
            if piece == num_stack - 1:
                if self.board[row][col] == 0:
                    if row == turn:
                        if row == 1:
                            if self.board[row - 1][col] != 0:
                                self.board[row][col] -= 1               
                                self.user_score += 1 + self.board[row - 1][col]
                                self.board[row - 1][col] = 0
                                self.update_score(row, 100 + self.user_score)
                        else:
                            if self.board[row + 1][col] != 0:
                                self.board[row][col] -= 1
                                self.other_score += 1 + self.board[row + 1][col]
                                self.board[row + 1][col] = 0
                                self.update_score(row, 100 + self.other_score)
  
            self.board[row][col] += 1
            if col == 0:
                step = 1
                row += 1
                if turn == 0:
                    self.board[row][col] += 1
                    self.other_score += 1
                else:
                    self.board[row - 1][col] -= 1
                    self.board[row][col + 1] += 1
                    col += 1

            if col == 7:
                step = -1
                row -= 1
                if turn == 1:
                    self.board[row][col] += 1
                    self.user_score += 1
                else:
                    self.board[row + 1][col] -= 1
                    self.board[row][col - 1] += 1
                    col -= 1
    

        self.check_empty()
        
        self.free = 1
        if col != 0 and col != 7:
            self.free = 0
            if turn == 0:
                turn = 1
            else:
                turn = 0
        
        return turn

    def check_empty(self):
        row_num = 0
        for row in self.board:
            empty_counter = 0
            
            for stack in row:
                if stack == 0:
                    empty_counter += 1
            if empty_counter == 6:
                if row_num == 0:
                    self.user_score = 48 - self.other_score
                    self.update_score(1, 100 + self.user_score)
                else:
                    self.other_score = 48 - self.user_score
                    self.update_score(0, 100 + self.other_score)
            
            row_num += 1
            
    def update_score(self, player, score):
        if player == 0:
            self.board[0][0] = score
            self.board[1][0] = score
        else:
            self.board[0][7] = score
            self.board[1][7] = score
    
    def get_all_stacks(self, row):
        stacks = []
        position = 0
        for stack in self.board[row]:
            if stack < 100 and stack != 0:
                stacks.append(position)
            position += 1
        
        return stacks
            
            
        
