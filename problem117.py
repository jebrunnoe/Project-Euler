#PROBLEM:
#  117
#
#NAME:
#
#  "Red, Green, and Blue Tiles"
#
#LINK:
#  https://projecteuler.net/problem=117
#
#APPROACH:
#  A dynamic programming algorithm is used that builds and references a table.
#  The columns of the table represent row length, while the rows represent
#  the starting color (0: black, 1: red, 2: green, 3: blue). The table is generated
#  until the provided size is reached. 

import time
start_time = time.time()

n     = 50
black = 1 
red   = 2
green = 3
blue  = 4

def get_column_sum(table, col):
   column_sum = 0
   for row in range(len(table)):
      column_sum = column_sum + table[row][col]
   return column_sum

def F(n):
   # Initialize the table.
   table = [[0 for unit in range(n + 1)] for row in range(4)] 
   table[0][black] = 1 # 'B'.
   table[1][red]   = 1 # 'RR'.
   table[2][green] = 1 # 'GGG'.
   table[3][blue]  = 1 # 'BBBB'.
   for col in range(2, n + 1):
      # Count arrangements that begin with a black tile: B[...], where the 
      # value in the bracket is the total number of 'col - black' length arrangements.
      table[0][col] = get_column_sum(table, col - black)
      # Count arrangements that begin with a red tile: RR[...], where the 
      # value in the brack is the total number of 'col - red' length arrangements.
      table[1][col] = table[1][col] + get_column_sum(table, col - red)
      # Count arrangements that begin with a green tile: GGG[...], where the
      # value in the brack is the total number of 'col - red' length arrangements.
      if col >= green: # Check to avoid negative index.
	 table[2][col] = table[2][col] + get_column_sum(table, col - green)
      # Count arrangements that begin with a blue tile: BBBB[...], where the
      # value in the brack is the total number of 'col - red' length arrangements.
      if col >= blue: # Check to avoid negative index.
      	 table[3][col] = table[3][col] + get_column_sum(table, col - blue)
   return get_column_sum(table, n)

print F(n)
print "Runtime: %.5fs" % (time.time() - start_time)
