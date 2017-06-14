from itertools import chain, combinations

def powerset(iterable):
   s = list(iterable)
   return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def check(s):
   sums = list()
   subsets = list(powerset(s))
   for p in subsets:
      sm = sum(p)
      if sm in sums: return False
      else: sums.append(sm)
   for i in range(len(subsets)):
      for j in range(len(subsets)):
	 if i == j or len(subsets[i]) == len(subsets[j]): continue
	 if len(subsets[i]) > len(subsets[j]):
	    if sum(subsets[j]) > sum(subsets[i]): return False
	 elif sum(subsets[i]) > sum(subsets[j]): return False
   return True

d = 3
a0 = 20
result = [20, 31, 38, 39, 40, 42, 45]
minSum = sum(result)
for a1 in range(31 - d, 31 + d):
   for a2 in range(38 - d, 38 + d):
      for a3 in range(39 - d, 39 + d):
	 for a4 in range(40 - d, 40 + d):
	    for a5 in range(42 - d, 52 + d):
	       for a6 in range(45 - d, 45 + d):
		  s = [a0, a1, a2, a3, a4, a5, a6]
		  if check(s) and sum(s) < minSum:
		     result = s
st = ''
for r in result:
   st += str(r)
print st
