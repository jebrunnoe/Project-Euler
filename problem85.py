from math import sqrt
M = 100

primatives = list()

def transform(a, b, c):
   x = min(a, b)
   if x == a: y = b
   else: y = a
   if x > M or y > 2 * M: return 
   primatives.append((a, b, c))
   transform( a - (2 * b) + (2 * c),  (2 * a) - b + (2 * c),  (2 * a) - (2 * b) + (3 * c))
   transform( a + (2 * b) + (2 * c),  (2 * a) + b + (2 * c),  (2 * a) + (2 * b) + (3 * c))
   transform(-a + (2 * b) + (2 * c), -(2 * a) + b + (2 * c), -(2 * a) + (2 * b) + (3 * c))

transform(3, 4, 5)

def scale(primatives):
   tuples = list()
   for p in primatives:
      a, b, c = p[0], p[1], p[2]
      k = 1
      x = min(a, b)
      if x == a: y = b
      else: y = a
      while (k * x) <= M and (k * y) <= 2 * M:
	 tuples.append((k * a, k * b, k * c))
	 k += 1
   return tuples

tuples = scale(primatives)
cuboids = set()

def decompose(a, b, c):
   x = max(a, b)
   y = min(a, b)
   for i in range(int(x / 2), x):
      if i > M: break
      cuboids.add((y, i, x - i, c))  

for t in tuples:
   decompose(t[0], t[1], t[2])

paths = set()

for c in cuboids:
   w = c[0] # width
   d = c[1] # depth
   h = c[2] # height
   p = c[3] # path
   path1 = sqrt(w**2 + (h + d)**2)
   path2 = sqrt(d**2 + (w + h)**2)
   path3 = sqrt(h**2 + (w + d)**2)
   if p == min(path1, path2, path3):
      paths.add(c)

for p in paths:
   print p

print len(paths)

#import itertools
#from math import sqrt
#count = 0
#limit = 99
#sizes = [i for i in range(1, limit+1)]
#minPaths = set()
#for cuboid in itertools.combinations_with_replacement(sizes, 3):  # replacement allows sizes with all 3 dimensions the same, like (1,1,1)
#   w = cuboid[0] # width
#   d = cuboid[1] # depth
#   h = cuboid[2] # height
#   path1 = sqrt(w**2 + (h + d)**2)
#   path2 = sqrt(d**2 + (w + h)**2)
#   path3 = sqrt(h**2 + (w + d)**2)
#   minPath = min(path1, path2, path3)
#   if minPath % 1 == 0:
#      minPaths.add(minPath)
#      count += 1
#print(count)
#print len(paths), paths, len(minPaths), minPaths    

