from itertools import combinations

def partition(l):
    n = len(l)
    for i in range(2 ** n):
        left = [e for b, e in enumerate(l) if i & 2 ** b]
        right = [e for b, e in enumerate(l) if not i & 2 ** b]
        yield left, right

def operate(x, y, operator):
   if y == 0 and operator == '/': return
   if operator == '+': return x + y
   if operator == '-': return x - y
   if operator == '*': return x * y
   if operator == '/': return x / y

def expressions(l):
    if len(l) == 1:
        yield l[0]
    else:    
        for left, right in partition(l):
            if not left or not right:
                continue
            for a in expressions(left):
                for b in expressions(right):
                    for operator in '+-*/':
			yield operate(float(a), float(b), operator)

def consecutive(s):
   t = 1
   while t in s:
      t += 1
   return t

digits = [''.join(c) for c in combinations('123456789', 4)]

consecutivity = dict()
max_c = 0
max_d = ''

for d in digits:
   target_set = set()
   for x in expressions(d):
      if x > 0 and int(x) == x:
	 target_set.add(x)
      c = consecutive(target_set)
      consecutivity[d] = c
      if c > max_c:
	 max_c = c
	 max_d = d

print consecutivity
print max_c, max_d
