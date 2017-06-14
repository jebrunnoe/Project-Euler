from math import sqrt

def prime(n):
    if n < 2 or any(n % i == 0 for i in range(2, int(sqrt(n)) + 1)): return False
    return True


found = False
primes = []
n = 3

def check(n):
   for p in primes:
	 root = sqrt((n - p) / 2)
	 if int(root) == root: return True
   return False
	 
while not found:
   if prime(n): primes.append(n)
   elif not check(n): 
      found = True
      print n
   n += 2
