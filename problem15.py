#PROBLEM:
#  15
#
#NAME:
#  "Lattice Paths"
#
#PROMPT:
#  Starting in the top left corner of a 2x2 grid, and only being able to move to the 
#  right and down, there are exactly 6 routes to the bottom right corner. How many 
#  such routes are there through a 20x20 grid?
#
#APPROACH:
#  Any valid path in a 20x20 grid will consist of 40 moves, 20 right and 20 down. 
#  This problem is then equivalent to counting the number of 40 letter words made
#  from 20 R's and 20 D's. 

import math
import time
start_time = time.time()

print math.factorial(40) / math.factorial(20) / math.factorial(20)
print "Runtime: %.5fs" % (time.time() - start_time)
