import pygame
from board import Board
from pieces import *
from player import Player





def main(args):
	board = Board()
	player1 = Player()
	player2 = Player()
	players = [player1, player2]
	current_player = 0
	pygame.init()
	screen = pygame.display.set_mode((600,600))
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				
				
		king = King('white', (0,2))
		result = king.get_available_moves(board)
		
		screen.fill((255,255,255))
		screen.blit(king.image, (10, 10))
		pygame.display.flip()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
