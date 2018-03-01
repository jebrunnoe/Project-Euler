#PROBLEM:
#  113
#
#NAME:
#  "Non-bouncy Numbers"
#
#PROMPT:
#  
#  Working from left-to-right if no digit is exceeded by the digit to its 
#  left it is called an increasing number; for example, 134468. Similarly 
#  if no digit is exceeded by the digit to its right it is called a decreasing 
#  number; for example, 66420. We shall call a positive integer that is 
#  neither increasing nor decreasing a "bouncy" number; for example, 155349.
#  As n increases, the proportion of bouncy numbers below n increases such 
#  that there are only 12951 numbers below one-million that are not bouncy 
#  and only 277032 non-bouncy numbers below 10^10. How many numbers below a 
#  googol (10^100) are not bouncy?
#
#LINK:
#  https://projecteuler.net/problem=113

import time
start_time = time.time()

#  This approach uses dynamic programming to build tables where an entry
#  at location (i, j) holds the number of increasing/decreasing j-digit numbers 
#  with i as the first digit. For example, the (3, 5) entry of the decreasing 
#  table holds the number of 5-digit decreasing numbers that begin with a 3. 

digit_count = 100
rows = 10 # Each table will have 10 rows representing starting digits 0 - 9.

def dynamic(cols):
   table = [[0 for col in range(cols)] for row in range(rows)] # Decreasing table.
   # Initialize the first row and column. 
   for row in range(rows):
      table[row][0] = 1 
   for col in range(cols):
      table[0][col] = 1 
   # Build the table.
   for row in range(1, rows):
      for col in range(1, cols):
	 local_sum = 0
	 for i in range(row + 1):
	    local_sum = local_sum + table[i][col - 1]
	 table[row][col] = local_sum
   return table

def get_decreasing(table, cols):
   decreasing = 0
   for row in range(1, rows): # Skip the first row.
      for col in range(cols):
	 decreasing = decreasing + table[row][col]
   return decreasing

def get_increasing(table, cols):
   increasing = 0
   for row in range(rows - 1): # Skip the last row.
      for col in range(cols):
	 increasing = increasing + table[row][col]
   return increasing   

# Numbers where every digit is the same, such as 5555, will be double counted. Subtract off
# 9 * digit_count from the result to correct it. 
table = dynamic(digit_count)
result = get_increasing(table, digit_count) + get_decreasing(table, digit_count) - (9 * digit_count)

print result
print "Runtime: %.5fs" % (time.time() - start_time)
