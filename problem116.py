#PROBLEM:
#  116
#
#NAME:
#
#  "Red, Green, or Blue Tiles"
##
#LINK:
#  https://projecteuler.net/problem=116
#
#APPROACH:
#  The function F(m, n) uses a dynamic programming algorithm that generates and 
#  references a table. The columns of the table represent the rows number of units 
#  in length. The tables rows represent the color the row begins with. With this 
#  representation, the entry of the table at (0, i) stores the number of 'i' unit 
#  long rows that begin with a black unit. Likewise, the entry (1, i) holds the number 
#  of i unit long rows that begin with a colored unit. The table is generatated until 
#  the number of possible arrangements for given row unit number is found. F(m, n)
#  is called with different values of m given in the prompt. 

import time
start_time = time.time()

n = 50

def F(m, n): # 'm' represents the block size.
   # Initialize the table.
   table = [[0 for unit in range(n + 1)] for row in range(2)] 
   table[0][m] = 0 # At least one colored tile must be used.
   table[1][m] = 1 # This corresponds to the one way which is an 'm' length colored block.

   for row_unit_count in range(m + 1, n + 1):
      # The number of i digit rows that start with a black is the same as the total
      # number of i - 1 digit rows because any valid row can have a black inserted at the front.
      table[0][row_unit_count] = table[0][row_unit_count - 1] + table[1][row_unit_count - 1]
      # The 1 refers to the arrangement that begins with an m digit colored block followed by all black tiles.
      # The number of arrangements that can fit in the remaining space is looked up. 
      table[1][row_unit_count] = 1 + table[0][row_unit_count - m] + table[1][row_unit_count - m]

   return table[0][n] + table[1][n]

print F(2, n) + F(3, n) + F(4, n)
print "Runtime: %.5fs" % (time.time() - start_time)
