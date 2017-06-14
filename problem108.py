primes = [2, 3, 5, 7, 11, 13]

def divisors(n):
   exponents = list()
   count = 1
   remainder = n
   for p in primes:
      if p * p > n: break
      exp = 0
      while remainder % p == 0:
	 exp += 1
	 remainder = remainder / p
      if exp > 0: count *= exp + 1
   return count

n = 1
while True:
   if (divisors(n * n) + 1) / 2 > 1000: 
      print n
      break
   n += 1
