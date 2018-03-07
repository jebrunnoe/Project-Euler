#PROBLEM:
#  115
#
#NAME:
#
#  "Counting Block Combinations II"
##
#LINK:
#  https://projecteuler.net/problem=115
#
#APPROACH:
#  The function F(m, n) uses a dynamic programming solution that generates and 
#  references a table. The columns of the table represent the rows number of units 
#  in length. The tables rows represent the color the row begins with. With this 
#  representation, the entry of the table at (0, i) stores the number of 'i' unit 
#  long rows that begin with a black unit. Likewise, the entry (1, i) holds the number 
#  of i unit long rows that begin with a red unit. The table is generatated until 
#  the number of possible arrangements for given row unit number is found. F(m, n)
#  is called with increasing values of n until the limit is exceeded.

import time
start_time = time.time()

limit = pow(10, 6) # Upper limit from prompt.
m = 50 # Minimum block length.

def F(m, n):
   # Initialize the table.
   table = [[0 for unit in range(n + 1)] for row in range(2)] 
   table[0][m] = 1 # There is one m unit row that starts with black: 'BBB...'.
   table[1][m] = 1 # There is one m unit row that starts with red: 'RRR...'.
   # Generate the table.
   for row_unit_count in range(m + 1, n + 1):
      # The number of i digit rows that start with a black is the same as the total
      # number of i - 1 digit rows because any valid row can have a black inserted at the front.
      table[0][row_unit_count] = table[0][row_unit_count - 1] + table[1][row_unit_count - 1]
      # There will be 'row_unit_count -(m - 1)' arrangements that begin with some number of reds, followed
      # by all blacks. Note that rows beginning with less than m reds are invalid which is why m - 1 must be subtracted.
      count = row_unit_count - (m - 1)
      # Rows beginning with red with that take the form 'RRR...B...[    ]', can have the number
      # of possible arrangements that could fill in the brackets looked up.
      for i in range(m, row_unit_count - (m + 1) + 1):
	 count = count + table[0][i] + table[1][i] - 1 # The instance ending in all blacks has already been counted. Subtract 1.
      table[1][row_unit_count] = count 
   return table[0][n] + table[1][n]

n = m # No row can have less units than the minimum block length.
while F(m, n) <= limit:
   n = n + 1

print n
print "Runtime: %.5fs" % (time.time() - start_time)
