#PROBLEM:
#  21
#
#NAME:
#  Amicable Numbers
#
#LINK:
#  https://projecteuler.net/problem=21

import time
start_time = time.time()

def get_divisors(n):
   divisors = [1]
   for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
	 divisors.append(i)
	 if n / i != i: 
	    divisors.append(n / i)
   return divisors # Return a list of the divisors of n.

# Populate a lookup table of the sum of the divisors of n. 
divisor_sums = [0, 1]
for n in range(2, 10001): 
    divisor_sums.append(sum(get_divisors(n)))

amicables = []
for n in range(10001):
   m = divisor_sums[n]
   # Check if both are within the limit, that they are not equal, and that they are amicable.
   if m < 10000 and m != n and divisor_sums[m] == n: 
      amicables.append(n)
    
print sum(amicables)
print "Runtime: %.5fs " % (time.time() - start_time)
