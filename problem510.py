#PROBLEM::
#  510
#
#NAME:
#  "Tangent Circles"
#
#PROMPT:
#  Circles A and B are tangent to each other and to line L at three distinct points.
#  Circle C is inside the space between A, B and L, and tangent to all three.
#  Let rA, rB and rC be the radii of A, B and C respectively.
#  Let S(n) = Sigma rA + rB + rC, for 0 < rA <= rB <= n where rA, rB and rC are integers. 
#  The only solution for 0 < rA <= rB <= 5 is rA = 4, rB = 4 and rC = 1, so S(5) = 4 + 4 + 1 = 9. 
#  You are also given S(100) = 3072. Find S(10^9).
#
#LINK:
#  https://projecteuler.net/problem=510

import time
from fractions import gcd

start_time = time.time()
N = pow(10, 9) # N is the given upper limit
S = long(0) # S is the sum defined in prompt. Use data type long to avoid truncating large numbers.

squares = [pow(i, 2) for i in range(1, 178)] # Upper limit of 178 found experimentally

pairs = list()
for i in range(len(squares)):
   for j in range(i, len(squares)): # start iterating j at i to avoid symmetric duplicates
      pair = [squares[i], squares[j]]
      pairs.append(pair)

for pair in pairs:
   square1 = pair[0]
   square2 = pair[1]
   square3 = int(pow(pow(square1, 0.5) + pow(square2, 0.5), 2))
   
   ra = square1 * square3
   rb = square2 * square3 # Largest radius
   rc = square1 * square2 

   if rb <= N: # Make sure it is not too large.
      if gcd(gcd(ra, rb), rc) == 1: # If the radii have a common divisor, then this triplet is a multiple of some more primitive triplet.
	 scalar_max = N // rb # This is the number of scalar multiples 
	 scalar_sum = scalar_max * (scalar_max + 1) // 2
	 S += scalar_sum * (ra + rb + rc)

print long(S)
print("%s seconds" % (time.time() - start_time))
