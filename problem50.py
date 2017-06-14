from math import sqrt
 
def prime(n):
   if n < 2 or any(n % i == 0 for i in range(2, int(sqrt(n)) + 1)): return False
   return True

bound = 100


