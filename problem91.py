n = 50
coordinates = set()

def dot(x, y):
   dot = 0
   for i in range(len(x)):
      dot += x[i] * y[i]
   return dot

for x1 in range(n + 1):
   for y1 in range(n + 1):
      if x1 == 0 and y1 == 0: continue
      for x2 in range(n + 1):
	 for y2 in range(n + 1):
	    if x2 == 0 and y2 == 0: continue
	    if x1 == x2 and y1 == y2: continue	    
	    if dot([x1, y1], [x2, y2]) == 0 or dot([x1, y1], [x2 - x1, y2 - y1]) == 0:
	       coordinates.add(frozenset(((0, 0), (x1, y1), (x2, y2))))

for c in coordinates: print c
print len(coordinates)
