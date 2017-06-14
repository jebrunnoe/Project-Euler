from math import sqrt
from decimal import *

def prime(p):
   if p < 2 or any(p % i == 0 for i in range(2, int(sqrt(p)) + 1)): return False
   return True

count = 0
total = 1
percent = 1.0
n = 1
while percent >= 0.10:
   n += 1
   total += 4
   a = 4 * pow(n, 2) - (10 * n) + 7
   b = 4 * pow(n, 2) - (8 * n) + 5
   c = 4 * pow(n, 2) - (6 * n) + 3
   d = 4 * pow(n, 2) - (4 * n) + 1
   if prime(a): count += 1
   if prime(b): count += 1
   if prime(c): count += 1
   if prime(d): count += 1
   percent = Decimal(count) / Decimal(total)
   print n, count, total, percent
s = 2 * n - 1
print s
