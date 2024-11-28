import pygame
SCREEN_W, SCREEN_H = 600, 600

class Piece:
	
	def __init__(self, color, location):
		self.color = color
		self.location = location
		self.image = None
		self.update_image()
		
	def get_position(self):
		pass
		
	def get_image(self):
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
		pass

class King(Piece):
	
	def __init__(self, color, location):
		super().__init__(color, location)
		
	def update_image(self):
		if self.color == 'white':
			self.image = pygame.transform.scale(pygame.image.load('images/pieces/white_king.png'), (SCREEN_W//8, SCREEN_W//8))
		elif self.color == 'black':
			self.image = pygame.image.load('images/pieces/black_king.png')
		
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
		print(result)
	def check_valid_move(self,location, board):
		y, x = location[0], location[1]
		if y > 7 or y < 0 or x > 7 or x < 0:
			return 0
		else:
			if board.is_occupied(y, x) == 1:
				return 0
			else:
				return 1

class queen(Piece):
	
	def __init__(self, color, location):
		super().__init__(self)
		
	def update_image(self):
		if self.color == white:
			self.image = pygame.image.load('images/pieces/white_queen')
		elif self.color == black:
			self.image = pygame.image.load('images/pieces/black_queen')
			
class castle(Piece):
	
	def __init__(self, color, location):
		super().__init__(self)
					
	def update_image(self):
		if self.color == white:
			self.image = pygame.image.load('images/pieces/white_castle')
		elif self.color == black:
			self.image = pygame.image.load('images/pieces/black_casltle')
			
class bishop(Piece):
	def __init__(self, color,location):
		super().__init__(self)
	
	def update_image(self):
		if self.color == white:
			self.image = pygame.image.load('images/pieces/white_bishop')
		elif self.color == black:
			self.image = pygame.image.load('images/pieces/black_bishop')
					
						
class pawn(Piece):
	
	def __init__(self, color, location):
		super().__init__(self)
	
	def update_image(self):
		if self.color == white:
			self.image = pygame.image.load('images/pieces/white_bishop')
		elif self.color == black:
			self.image = pygame.image.load('images/pieces/black_bishop')		

		




if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
