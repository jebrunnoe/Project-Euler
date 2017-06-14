figurates = list()

def calculate(n, order):
   if order == 3: return (n * (n + 1)) / 2
   if order == 4: return n * n
   if order == 5: return (n * (3 * n - 1)) / 2
   if order == 6: return n * (2 * n - 1)
   if order == 7: return (n * (5 * n - 3)) / 2
   if order == 8: return n * (3 * n - 2)

def build(order):
   polygon = list()
   term = 0
   n = 1
   while term < 10000:
      term = calculate(n, order)
      if len(str(term)) == 4: polygon.append(str(term))
      n += 1
   return polygon

for order in range(3, 9):
   figurates.append(build(order))

def search(digits, pool):
   for polygon in pool:
      for item in polygon:
	 if item[:2] == digits:
	    if len(pool) == 1: return [item]
	    chain = search(item[2:], [p for p in pool if p != polygon])
	    if chain:
	       chain.insert(0, item)
	       return chain
   return None

for polygon in figurates:
   for term in polygon:
      chain = search(term[2:], [x for x in figurates if x != polygon])
      if chain:
	 chain.insert(0, term)
	 if chain[0][:2] == chain[5][2:]: 
	    print chain, sum(int(x) for x in chain)
   
