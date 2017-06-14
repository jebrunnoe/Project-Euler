from math import sqrt

def fract(S):
   terms = list()
   a0 = int(sqrt(S))
   m = 0
   d = 1
   a = a0
   while a != 2 * a0:
      m = d * a - m
      d = (S - m * m) / d
      a = int((sqrt(S) + m) / d)
      terms.append(a)
   return terms

def check(x, y):
   if x * x - D * y * y == 1: return True
   else: return False

values = {}

for D in range(2, 1001):
   if int(sqrt(D)) == sqrt(D): continue
   a = fract(D)
   b = int(sqrt(D))
   num = [b, b * a[0] + 1]
   den = [1, a[0]] 
   if check(num[0], den[0]): values[D] = (num[0], den[0])
   elif check(num[1], den[1]): values[D] = (num[1], den[1])
   else:
      n = 2
      while True:
	 index = (n - 1) % len(a)
	 x = a[index] * num[n-1] + num[n-2]
	 y = a[index] * den[n-1] + den[n-2]
	 num.append(x)
	 den.append(y)
	 if check(x, y): 
	    values[D] = (x, y) 
	    break
	 n += 1

max_x = 0
max_d = 0
for key in values:
   if values[key][0] > max_x: 
      max_x = values[key][0]
      max_d = key
print max_d

