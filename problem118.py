#PROBLEM:
#  118
#
#NAME:
#  "Pandigital Prime Sets
#
#LINK:
#  https://projecteuler.net/problem=118

import math
import itertools
import time
start_time = time.time()

saved_primes = set()
upper = int(math.sqrt(987654321)) + 1 # Largest number needed for prime checking.

def sieve(upper):
   a = [True] * (upper + 1)
   a[0] = a[1] = False
   for (i, isprime) in enumerate(a):
      if isprime:
	 yield i
	 saved_primes.add(i)
         for n in xrange(i * i, upper + 1, i):
	    a[n] = False

primes = list(sieve(upper))

def prime(n):
   # Saved primes contains, at least, all primes up to 'upper'.
   if n in saved_primes: 
      return True
   # If n is not in saved primes, but it is less than 'upper', it cannot be prime. 
   if n < upper: 
      return False
   for p in primes:
      if n % p == 0: 
	 return False
      if p > math.sqrt(n): 
	 break
   saved_primes.add(n)
   return True

digits = range(1, 10)
permutation_size = len(digits)

def check(start, prev):
   count = 0
   for i in range(start, permutation_size):
      number = 0
      for j in range(start, i + 1):
	 number = number * 10 + permutation[j]
      # Only count increasing sets. Check this before primality to save time.
      if number < prev: 
	 continue
      if not prime(number): 
	 continue
      if i == permutation_size - 1: # The end of set is reached with increasing, prime members.
	 return count + 1
      # Recursion only happens if n is prime and greater than the previous value in the set.
      count = count + check(i + 1, number)
   return count

count = 0
for permutation in itertools.permutations(digits):
   count = count + check(0, 0)

print count
print "Runtime: %.5fs " % (time.time() - start_time)
