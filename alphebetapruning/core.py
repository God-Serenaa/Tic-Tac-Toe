import pygame, sys
from ai import AlphaBeta
from constants import *

pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Tic Tac Toe')
screen.fill( BACKGROUND_COLOR )


class Board:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # Player X always plays first
        self.player_turn = 'X'
    
    def show_lines(self):
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)
    
    def draw_board(self):
        self.show_lines()

        for row in range(0, 3):
            for col in range(0, 3):
                if self.current_state[row][col] == 'X':

                    start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
                    end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                    pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

                    start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                    end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
                    pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
                
                if self.current_state[row][col] == 'O':
                    
                    center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.circle(screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)
                
    
    
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    
    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second diagonal win
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.current_state[i][j] == '.'):
                    return None

        # It's a tie!
        return '.'


class Game(Board, AlphaBeta):
    

    def print_result(self, player):
        font = pygame.font.Font('freesansbold.ttf', 32)
        if player:
            text = font.render('WINNER IS {}'.format(player), True, (255, 255, 255))
        else:
            text = font.render('IT IS A TIE', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (WIDTH//2, HEIGHT//2)
        screen.blit(text, textRect)
  
    def play(self):
        
        while True:
            self.draw_board()
            self.result = self.is_end()

            if self.result != None:
                if self.result == 'X':
                    self.print_result('X')
                elif self.result == 'O':
                    self.print_result('O')
                elif self.result == '.':
                    self.print_result(None)

                self.initialize_game()

            if self.player_turn == 'X':
                while True:
                    flag = 0
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = event.pos
                            px = pos[1] // SQSIZE
                            py = pos[0] // SQSIZE

                            (qx, qy) = (px, py)

                            if self.is_valid(px, py):
                                self.current_state[px][py] = 'X'
                                self.player_turn = 'O'
                                flag = 1
                            else:
                                print('The move is not valid! Try again.')
                    if flag == 1: break
                    pygame.display.update()

            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'

Game().play()
