limit = 10000000
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
destination = [None] * 568
count = 0

def expand(n):
   s = str(n)
   a = 0
   for i in range(len(s)):
      a += squares[int(s[i])]
   return a

for start in range(1, 568):
   n = start
   while n != 1 and n != 89: n = expand(n)
   if n == 89:
      destination[start] = 89
      count += 1

for start in range(568, limit + 1):
   e = expand(start)
   if destination[e] == 89: count += 1

print count
