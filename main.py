import pygame
from board import Board
from pieces import *
from player import Player
import time




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
				
				

		screen.fill((255,255,255))
		board.draw(screen)
		pygame.display.flip()
		pygame.time.delay(500)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
