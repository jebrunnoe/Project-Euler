from math import sqrt

def is_pentagonal(p):
   n = (sqrt(24 * p + 1) + 1) / 6
   if int(n) == n: return True
   else: return False 

found = False
n = 1
pentagonal = []

while not found:
   p_j = (n * (3 * n - 1)) / 2
   pentagonal.append(p_j)
   for p_k in pentagonal:
      if is_pentagonal(p_j + p_k) and is_pentagonal(p_j - p_k): 
	 found = True
	 d = p_j - p_k
   n += 1

print d
