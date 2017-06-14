L = 1500000

primatives = list()
perims = [0] * (L + 1)

def transform(a, b, c):
   if a + b + c > L: return
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
      while (k * a) + (k * b) + (k * c) <= L:
	 tuples.append((k * a, k * b, k * c))
	 k += 1
   return tuples

tuples = scale(primatives)

for t in tuples:
   index = t[0] + t[1] + t[2]
   perims[index] += 1

result = 0

for p in perims:
   if p == 1: result += 1

print result


