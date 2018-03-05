#PROBLEM:
#  114
#
#NAME:
#
#  "Counting Block Combinations I"
#
#PROMPT:
#  A row measuring seven units in length has red blocks with a minimum length 
#  of three units placed on it, such that any two red blocks (which are allowed 
#  to be different lengths) are separated by at least one black square. There 
#  are exactly seventeen ways of doing this. How many ways can a row measuring 
#  fifty units in length be filled? NOTE: Although the example above does not 
#  lend itself to the possibility, in general it is permitted to mix block 
#  sizes. For example, on a row measuring eight units in length you could use 
#  red (3), black (1), and red (4).
#
#LINK:
#  https://projecteuler.net/problem=114
#
#APPROACH:
#  This is a dynamic programming solution that generates and references a table. 
#  The columns of the table represent the rows number of units in length. The
#  tables rows represent the color the row begins with. With this representation, 
#  the entry of the table at (0, i) stores the number of 'i' unit long rows 
#  that begin with a black unit. Likewise, the entry (1, i) holds the number of
#  i unit long rows that begin with a red unit. The table is generatated until 
#  the number of possible arrangements for given row unit number is found. 

import time
start_time = time.time()

row_unit_target = 50 

# Initialize the table.
table = [[0 for unit in range(row_unit_target + 1)] for row in range(2)] 
table[0][3] = 1 # There is one 3 unit row that starts with black: 'BBB'.
table[1][3] = 1 # There is one 3 unit row that starts with red: 'RRR'.

# Generate the table.
for row_unit_count in range(4, row_unit_target + 1):
   # The number of i digit rows that start with a black is the same as the total
   # number of i - 1 digit rows because any valid row can have a black inserted at the front. 
   table[0][row_unit_count] = table[0][row_unit_count - 1] + table[1][row_unit_count - 1]
   # There will be 'row_unit_count - 2' arrangements that begin with some number of reds, followed
   # by all blacks. Note that 'RBBB...' and 'RRBB...' are invalid which is why 2 must be subtracted.
   count = row_unit_count - 2
   # Rows beginning with red with 7 or more units will take the form 'RRR...B...[    ]' where the number
   # of possible arrangements that could fill in the brackets can be looked up. 
   for i in range(3, (row_unit_count - 4) + 1):
      count = count + table[0][i] + table[1][i] - 1 # The instance ending in all blacks has already been counted. Subtract 1.
   table[1][row_unit_count] = count 

print table[0][row_unit_target] + table[1][row_unit_target]
print "Runtime: %.5fs" % (time.time() - start_time)
