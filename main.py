import pygame, time
from mancala.constants import WIDTH, HEIGHT, SQUARE_SIZE
from mancala.game import Game
from minimax.algo import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mancala')
pygame.font.init() 

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False
            time.sleep(5)

        # Top Row is Ai
        if game.turn == 0 and run == True:
            value, new_board = minimax(game.get_board(), 5, float('-inf'), float('inf'), True, game)
            game.ai_move(new_board)
            # delay to visually see multiple moves being performed (optional)
            time.sleep(1.5)

        # Bottom Row is Ai (uncomment to implement)
        """ if game.turn == 1 and run == True:
            value, new_board = minimax(game.get_board(), 5, float('-inf'), float('inf'), False, game)
            game.ai_move(new_board)
            # delay to visually see multiple moves being performed (optional)
            time.sleep(1.5) """
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
        
    pygame.quit()

main()