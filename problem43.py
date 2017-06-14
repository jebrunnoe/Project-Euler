from itertools import permutations
from math import sqrt

def prime(n):
    if n < 2 or any(n % i == 0 for i in range(2, int(sqrt(n)) + 1)): return False
    return True

primes = []
for i in range(18):
   if prime(i): primes.append(i)

def check(p):
   for digit in range(1, 8):
      s = ""
      for width in range(3):
	 s += p[digit + width]
      if int(s) % primes[digit - 1] != 0: return False
   return True

perms = ("".join(p) for p in permutations("0123456789"))

property = set()
for p in perms:
   if check(p): property.add(int(p))

for p in property: print p
print sum(property)

