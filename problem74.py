from math import factorial

limit = 1000000
result = 0
facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def facto(n):
   s = str(n)
   l = len(s)
   value = 0
   for i in range(l):
      value += facts[int(s[i])]
   return value

for start in range(limit):
   if start % 1000 == 0: print start
   terms = set()
   n = start
   while n not in terms:
      terms.add(n)
      n = facto(n)
   if len(terms) == 60: result += 1

print result

