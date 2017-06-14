from math import sqrt
limit = 10000

def fract(S):
   terms = list()
   a0 = int(sqrt(S))
   m = 0
   d = 1
   a = a0
   while a != 2 * a0:
      m = d * a - m
      d = (S - m * m) / d
      a = int((sqrt(S) + m) / d)
      terms.append(a)
   return terms

odd_period = 0
for S in range(limit + 1):
   test = sqrt(S)
   if int(test) == test: continue
   if len(fract(S)) % 2 == 1: odd_period += 1

print odd_period
