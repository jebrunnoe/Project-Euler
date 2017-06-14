from itertools import combinations
result = 0

def disjoint(a, b):
   for element in a:
      if element in b: return False
   return True

variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
subsets = list()
for size in range(1, len(variables)):
   for c in combinations(variables, size):
      subsets.append(c)

pairs = list(combinations(subsets,2))
disjoint_pairs = list()
for p in pairs:
   if disjoint(p[0], p[1]):
      disjoint_pairs.append(p)

substitution = dict()
substitution['a'] = ['k']
substitution['b'] = substitution['a'] + ['d0']
substitution['c'] = substitution['b'] + ['d1']
substitution['d'] = substitution['c'] + ['d2']
substitution['e'] = substitution['d'] + ['d3']
substitution['f'] = substitution['e'] + ['d4']
substitution['g'] = substitution['f'] + ['d5']
substitution['h'] = substitution['g'] + ['d6']
substitution['i'] = substitution['h'] + ['d7']
substitution['j'] = substitution['i'] + ['d8']
substitution['k'] = substitution['j'] + ['d9']
substitution['l'] = substitution['k'] + ['d10']


def compare(a, b):
   l1 = list()
   l2 = list()
   for element in a:
      for s in substitution[element]:
	 l1.append(s)
   for element in b:
      for s in substitution[element]:
	 l2.append(s)
   for element in sorted(l1):
      if element in sorted(l2):
	 l1.remove(element)
	 l2.remove(element)
   if len(l1) == 0 or len(l2) == 0: return False
   else: return True

for pair in disjoint_pairs:
   a = pair[0]
   b = pair[1]
   if len(a) > 1 and len(b) > 1 and len(a) == len(b):
      if compare(a, b): 
	 result += 1
print result
