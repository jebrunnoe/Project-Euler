table = {}
target = 100

def initialize(n):
   for row in range(n + 1):
      table[row, 0] = 0
   for col in range(1, n):
      table[0, col] = 1

def build(n):
   initialize(n)
   for row in range(1, n + 1):
      for col in range(1, n):
	 table[row, col] = table[row, col - 1]
	 if row >= col: 
	    table[row, col] += table[row - col, col]
   return table[n, n - 1]

print build(target)
