import pygame
SCREEN_W, SCREEN_H = 600, 600
TILE_WIDTH = SCREEN_W // 8
TILE_HEIGHT = SCREEN_W // 8


class Piece:
	
	def __init__(self, color, location):
		self.color = color
		self.location = location
		self.image = None
		self.initialise_image()
		
	def get_position(self):
		pass
		
	def get_potential_moves(self):
		pass
	def set_position():
		pass
	def set_image():
		pass
	def move_piece(self):
		pass
	def draw(self, screen):
		try:
			screen.blit(self.image, (self.location[0] * TILE_WIDTH,  self.location[1] * TILE_HEIGHT))

		except TypeError:
			print(f"TypeError: Y {self.location[0] * TILE_HEIGHT}, X {self.location[1] * TILE_WIDTH} ") 
class king(Piece):
	
	def __init__(self, color, location):
		super().__init__(color, location)
		
	def initialise_image(self):
		if self.color == 'white':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/white_king.png'), (SCREEN_W//8, SCREEN_H//8))
		elif self.color == 'black':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/black_king.png'), (SCREEN_W//8, SCREEN_H//8))
		
	def get_available_moves(self, board):
		result = [  (self.location[0] - 1,self.location[1]),     #top
					(self.location[0] + 1,self.location[1]),     #bottom
					(self.location[0], self.location[1]+1),      #Right
					(self.location[0], self.location[1] - 1),    #Left
					(self.location[0] - 1,self.location[1] - 1), #Top left 
					(self.location[0] - 1,self.location[1] + 1), #Top right
					(self.location[0] + 1,self.location[1] - 1), #Bottom Left
					(self.location[0] + 1,self.location[1] + 1) #Bottom Right
				 ]
				 
		result = [i for i in result if self.check_valid_move(i,board) == 1]

	def check_valid_move(self,location, board):
		y, x = location[0], location[1]
		if y > 7 or y < 0 or x > 7 or x < 0:
			return 0
		else:
			if board.tiles[y][x].is_occupied() == 1:
				return 0
			else:
				return 1

class queen(Piece):
	
	def __init__(self, color, location):
		super().__init__(color, location)
		
	def initialise_image(self):
		if self.color == 'white':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/white_queen.png'), (SCREEN_W // 8, SCREEN_H // 8))
		elif self.color == 'black':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/black_queen.png'), (SCREEN_W // 8, SCREEN_H // 8))
			
class castle(Piece):
	
	def __init__(self, color, location):
		super().__init__(color, location)
					
	def initialise_image(self):
		if self.color == 'white':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/white_rook.png'), (SCREEN_W // 8, SCREEN_H // 8))
		elif self.color == 'black':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/black_rook.png'), (SCREEN_W // 8, SCREEN_H //8))
			
class bishop(Piece):
	def __init__(self, color,location):
		super().__init__(color, location)
	
	def initialise_image(self):
		if self.color == 'white':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/white_bishop.png'), (SCREEN_W // 8, SCREEN_H // 8))
		elif self.color == 'black':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/black_bishop.png'), (SCREEN_W // 8, SCREEN_H // 8))
					
						
class knight(Piece):
	def __init__(self, color,location):
		super().__init__(color, location)
	
	def initialise_image(self):
		if self.color == 'white':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/white_knight.png'), (SCREEN_W // 8, SCREEN_H // 8))
		elif self.color == 'black':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/black_knight.png'), (SCREEN_W // 8, SCREEN_H // 8))
					
						
class pawn(Piece):
	
	def __init__(self, color, location):
		super().__init__(color, location)
	
	def initialise_image(self):
		if self.color == 'white':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/white_pawn.png'), (SCREEN_W //8, SCREEN_W // 8))
		elif self.color == 'black':
			self.image = pygame.transform.smoothscale(pygame.image.load('images/pieces/black_pawn.png'), (SCREEN_W // 8, SCREEN_W // 8))
	
			

		




if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
