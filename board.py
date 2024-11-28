



class Board:
	
	def __init__(self):
		self.width = 8
		self.height = 8
		self.grid = [[ [] for i in range(8)] for j in range(8)]
		self.initialise_grid()
	
	def initialise_grid(self):
		for i in range(8):
			for j in range(8):
				for k in range(2);
					
		
	def draw(self):
		pass
	def is_occupied(self, row, column):
		if self.grid[row][column] != ' ':
			return 1
		else:
			return 0
	def




if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
