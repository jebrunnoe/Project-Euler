def partition(n):
   if partitions[n]: return partitions[n]
   p = list()
   for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
	 x = sorted([i, n / i])
	 if x not in p: p.append(x)
	 for j in partition(n / i):
	    y = sorted([i] + j)
	    if y not in p: p.append(y)
   partitions[n] = p
   return p

partitions = [None] * 13000
limit = 12000
result = set()

for k in range(2, limit + 1):
   target = k
   found = False
   while not found:
      for p in partition(target):
	 if sum(p) + k - len(p) == target:
	    result.add(target)
	    found = True
	    break	    
      target += 1
print result, sum(result)
