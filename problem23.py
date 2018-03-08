#PROBLEM:
#  23
#
#NAME:
#  "Non-abundant Sums"
#
#LINK:
#  https://projecteuler.net/problem=23
#

import time
start_time = time.time()

def factor(n):
   factors = list() 
   factors.append(1)
   for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
	 factors.append(i)
	 if n / i != i: 
	    factors.append(n / i)
   return factors

abundant_numbers = set()
non_abundant_sum = list()

for i in range(1, 28124): # Upper limit provided in prompt.
   if sum(factor(i)) > i: # If true, i is abundant.
      abundant_numbers.add(i)
   # Suppose 'a' is an abundant number. If 'i - a' is also abundant, than
   # i is the sum of the two abundant numbers 'a' and 'i - a'. 
   if not any((i - a in abundant_numbers) for a in abundant_numbers):
      non_abundant_sum.append(i)

print sum(non_abundant_sum)
print "Runtime: %.5fs " % (time.time() - start_time)
