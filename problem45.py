from math import sqrt

def pentagonal(p):
   n = (sqrt(24 * p + 1) + 1) / 6
   if int(n) == n: return True
   else: return False

def hexagonal(h):
   n = (sqrt(8 * h + 1) + 1) / 4 
   if int(n) == n: return True
   else: return False

found = False
n = 40756

while not found:
   t = (n * (n + 1)) / 2
   if pentagonal(t) and hexagonal(t):
      found = True
      print t
   n += 1
