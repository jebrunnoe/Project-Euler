squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]
pairs = set()

def missing(l):
   m = list()
   for i in range(10):
      if i not in l:
	 m.append(i)
   return m

def fill(a, b):
   if len(a) == 6 and len(b) == 6:
      x = frozenset(sorted(a))
      y = frozenset(sorted(b))
      if (y, x) not in pairs:
	 pairs.add((x, y))
      return
   if len(a) < 6:
      missing_a = missing(a)
      for m in missing_a:
	 fill(a + [m], b)
   if len(b) < 6:
      missing_b = missing(b)
      for m in missing_b:
	 fill(a, b + [m])

def tree(a, b, i):
   if i > 8:
      x = set(a)
      y = set(b)
      if len(x) < 7 and len(y) < 7:
	 fill(list(x), list(y))
      return
   digit1 = squares[i][0]
   digit2 = squares[i][1]
   tree(a + [digit1], b + [digit2], i + 1)
   if digit1 == 6 or digit1 == 9:
      tree(a + [15 - digit1], b + [digit2], i + 1)
      tree(a + [digit2], b + [15 - digit1], i + 1)
   tree(a + [digit2], b + [digit1], i + 1)   
   if digit2 == 6 or digit2 == 9:
      tree(a + [digit1], b + [15 - digit2], i + 1)
      tree(a + [15 - digit2], b + [digit1], i + 1)

tree(list(), list(), 0)   

for p in pairs:
   print p[0]
   print p[1]
   print
print len(pairs)
