import pygame
import pieces


class Board:
	
	def __init__(self):
		
		self.tiles = self.create_board()
		self.initialise_board()
		
		
	def create_board(self):
		tiles = []
		color = None
		for row in range(8):
			tiles.append([])
			for col in range(8):
				if (row + col) % 2 == 0:
					color = 'light'
				else:
					color = 'dark'
				tiles[row].append(Tile(row, col, color))
				
		return tiles
	
	def initialise_board(self):
		for i in range(8):
			self.tiles[i][1].piece = pieces.pawn('white', (i, 1))
			self.tiles[i][6].piece = pieces.pawn('black', (i, 6)) 
		self.tiles[0][0].piece = pieces.castle('white', (0, 0) )
		self.tiles[7][0].piece = pieces.castle('white', (7, 0) )
		self.tiles[0][7].piece = pieces.castle('black', (0, 7) )
		self.tiles[7][7].piece = pieces.castle('black', (7, 7) )
		self.tiles[1][0].piece = pieces.knight('white', (1, 0) )
		self.tiles[6][0].piece = pieces.knight('white', (6, 0) )
		self.tiles[1][7].piece = pieces.knight('black', (1, 7) )
		self.tiles[6][7].piece = pieces.knight('black', (6, 7) )
		self.tiles[2][0].piece = pieces.bishop('white', (2, 0) )
		self.tiles[5][0].piece = pieces.bishop('white', (5, 0) )
		self.tiles[2][7].piece = pieces.bishop('black', (2, 7) )
		self.tiles[5][7].piece = pieces.bishop('black', (5, 7) )
		self.tiles[3][0].piece = pieces.queen('white', (3, 0) )
		self.tiles[3][7].piece = pieces.queen('black', (3, 7) )
		self.tiles[4][0].piece = pieces.king('white', (4, 0) )
		self.tiles[4][7].piece = pieces.king('black', (4, 7) )
				
	def draw(self, screen):
		
		for row in range(8):
			for col in range(8):
				self.tiles[row][col].draw(screen)
				if self.tiles[row][col].is_occupied() == 1:
					self.tiles[row][col].piece.draw(screen)
				

class Tile():
	
	def __init__(self, row, column, color, piece = None):
		self.row = row
		self.column = column
		self.color = color
		self.piece = piece
		self.tilesize = (600 // 8, 600 // 8)
		self.image = self.get_image()
		
	def is_occupied(self):
		if self.piece == None:
			return 0;
		else:
			return 1
			
	def get_image(self):
		if self.color == 'light':
			try:
				return pygame.transform.scale(pygame.image.load("images/tiles/square_light_brown.png"), (600 // 8, 600 // 8))
			except:
				print("exception")
		elif self.color == 'dark':
			try:
				return pygame.transform.scale(pygame.image.load("images/tiles/square_dark_brown.png"), (600 // 8, 600 // 8))
			except:
				print("exception")
		else:
			raise ValueError(f"Invalid color: {self.color}")
	
	def draw(self, screen):
		ypos,xpos = self.row*75, self.column*75
		screen.blit(self.image, (ypos, xpos) )


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
