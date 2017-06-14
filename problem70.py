from itertools import combinations
from decimal import Decimal

limit = 10000000

def sieve(limit):
   a = [True] * limit
   a[0] = a[1] = False
   for (i, isprime) in enumerate(a):
      if isprime:
	 if i > 2000: yield i
         for n in xrange(i * i, limit, i):
	    a[n] = False

primes = list(sieve(4000))

def factor(n):
   factors = list()
   for p in primes:
      if p > n: break
      if n % p == 0: factors.append(p)
   return factors

def is_permutation(n, m):
   if sorted(n) == sorted(m): return True
   else: return False

def phi(n):
   factors = factor(n)
   result = n
   for f in factors:
      result *= (1 - 1. / f)
   return result

def search(pairs):
   best_ratio = limit
   best_n = 0
   for pair in pairs:
      n = pair[0] * pair[1]
      if n > limit: return best_n
      p = int(phi(n))
      if is_permutation(str(n), str(p)): 
	 ratio = Decimal(n)/Decimal(p)
	 if ratio < best_ratio:
	    best_ratio = ratio
	    best_n = n
   
print search(combinations(primes, 2))
