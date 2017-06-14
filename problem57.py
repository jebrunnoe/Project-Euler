import sys
sys.setrecursionlimit(1001)

def expand(depth):
   if depth == limit: return [1, 2]
   fraction = expand(depth + 1)
   num = fraction[0]
   den = fraction[1]
   return [den, (2 * den + num)]

count = 0
for limit in range(1000):
   fraction = expand(0)
   num = fraction[0] + fraction[1]
   den = fraction[1]
   if len(str(num)) > len(str(den)): count += 1
print count

