from math import log
from fractions import gcd

def sieve(limit):
   a = [True] * limit
   a[0] = a[1] = False
   for (i, isprime) in enumerate(a):
      if isprime:
	 yield i
         for n in xrange(i * i, limit, i):
	    a[n] = False

def factor(n):
   factors = set()
   for p in primes:
      if p > n: break
      if n % p == 0:
	 factors.add(p)
   return factors 

def phi(n):
   factors = factor(n)
   result = n
   for f in factors:
      result *= (1 - 1. / f)
   return int(result)

limit = 1000000
primes = list(sieve(limit))
phis = [None] * (limit + 1)

for p in primes:
   bound = int(log(limit, p))
   for exp in range(1, bound + 1):
      phis[p ** exp] = (p ** (exp - 1)) * (p - 1)
      
for i in range(6, limit + 1):
   if i % 1000 == 0: print i
   if not phis[i]:
      for p in primes:
	 if i % p == 0 and gcd(p, i / p) == 1:
	    phis[i] = phis[p] * phis[i / p]
	    break
      if not phis[i]: 
	 phis[i] = phi(i)

accum = 0
for phi in phis:
   if phi: accum += phi
print accum
