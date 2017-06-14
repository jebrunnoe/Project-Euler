from math import sqrt

def prime(n):
    if n < 2 or any(n % i == 0 for i in range(2, int(sqrt(n)) + 1)): return False
    return True

primes = list()

def factor(n):
   factors = 0
   rem = n
   for p in primes:
      if p > sqrt(rem): return factors + 1
      if rem % p == 0: factors += 1
      while rem % p == 0: rem = rem / p
      if rem == 1: break
   return factors

count = 0
n = 1
limit = 4

while count < limit:
   if prime(n): primes.append(n)       
   if factor(n) == limit: count += 1
   else: count = 0
   n += 1
print n - count
