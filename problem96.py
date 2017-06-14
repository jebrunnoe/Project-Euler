import copy, random

class Cell(): 
	def __init__(self, value, fixed, peers, possible, focus):
		self.value = value    
		self.fixed = fixed
		self.peers = peers
		self.possible = possible
		self.notes = ' '

	def is_possible(self, value):
		if value in self.possible: return True
		else: return False

	def is_present(self, value):
		for cell in self.peers:
			if value == cell.value: return True
		return False

	def revise(self):
		del self.possible[:]
		for value in range(9):
			if not self.is_present(value + 1): self.possible.extend([value + 1])


class Board():
	def __init__(self):
		self.board = [[Cell(0, False, [], range(1, 10), False) for row in range(9)] for col in range(9)]
		self.cells = []
		for row in range(9):
			for col in range(9):
				self.cells.extend([self.board[row][col]])
				for run in range(9):
					if run != row: self.board[row][col].peers.extend([self.board[run][col]])
					if run != col: self.board[row][col].peers.extend([self.board[row][run]])    
				for r in range(row - (row % 3), row - (row % 3) + 3):
					for c in range(col - (col % 3), col - (col % 3) + 3):
						if r != row and c != col: self.board[row][col].peers.extend([self.board[r][c]])

	def display(self):
		print 'Sudoku'.center(24)
		line = '+-------+-------+-------+'
		for row in range(9):
			if row in [0, 3, 6, 9]: print line
			for col in range(9):
				print ('| ' + '{:1}' if col in [0, 3, 6, 9] else '{}').format(
					  (self.board[row][col].value if self.board[row][col].value != 0 else '.')),
			print '|'
		print line

	def designate(self):
		for row in range(9):
			for col in range(9):
				if self.board[row][col].value > 0: self.board[row][col].fixed = True

	def is_done(self):
		for row in range(9):
			for col in range(9):
				if self.board[row][col].value == 0: return False
		return True

	def solve(self, depth):
		if depth == 81: return True
		cell = self.cells[depth]
		if cell.fixed: return self.solve(depth + 1)
		cell.revise()
		while cell.possible:
			p = random.choice(cell.possible)
			cell.value = p
			cell.possible.remove(p)
			if self.solve(depth + 1): return True
		cell.value = 0
		return False

	def conceal(self, difficulty): 
		self.designate()
		for cell in random.sample(self.cells, difficulty):
			if self.is_unique(cell): 
				cell.value = 0
				cell.fixed = False

	def is_unique(self, cell):
		cell.revise()
		for p in cell.possible:
			if p != cell.value:
				save = cell.value
				cell.value = p
				result = copy.deepcopy(self).solve(0) 
				cell.value = save
				if result: return False
		return True

raw = open("p096_sudoku.txt", "r").read()
string = raw.split()
string = [s for s in string if len(s) == 9]

sudokus = list()
i = 0
while i < len(string):
	sudoku = list()
	while len(sudoku) < 9:
		sudoku.append(string[i])
		i += 1
	sudokus.append(sudoku)

def load(puzzle):
	for row in range(9):
		for col in range(9):
			value = int(puzzle[row][col])
			main.board[row][col].value = value
			if value > 0: main.board[row][col].fixed = True
			else: main.board[row][col].fixed = False

result = 0

for sudoku in sudokus:
	main = Board()
	load(sudoku)
	main.solve(0)
	result += int(str(main.board[0][0].value) + str(main.board[0][1].value) + str(main.board[0][2].value))
print result
		
