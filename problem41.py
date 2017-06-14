from math import sqrt
from itertools import permutations

def prime(n):
    if n < 2 or any(n % i == 0 for i in range(2, int(sqrt(n)) + 1)): return False
    return True

perms = []
max = 0

for p4 in ("".join(digit) for digit in permutations("1234")): perms.append(p4)
for p7 in ("".join(digit) for digit in permutations("1234567")): perms.append(p7)

for i in reversed(perms):
   if prime(int(i)): 
      max = i
      break

print max
