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

sets = list()
raw = open("p105_sets.txt", "r").read().split()
for r in raw:
   sets.append(r.split(','))
for s in sets:
   for i in range(len(s)):
      s[i] = int(s[i])

result = 0
for s in sets:
   if check(s):
      result += sum(s)
print result
