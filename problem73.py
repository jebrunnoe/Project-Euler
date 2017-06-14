limit = 12000
phi = range(0, limit + 1)
result = 0
for i in range(2, limit + 1):
   if phi[i] == i:
      for j in range(i, limit + 1, i):
	 phi[j] = (phi[j] / i) * (i - 1)
   result += phi[i]
print result
print int(result / 6)

#from fractions import Fraction
#limit = 12000
#included = set()

#for d in range(2, limit + 1):
#   if d % 1000 == 0: print d
#   lower = int(d / 3) + 1
#   upper = int((d - 1) / 2)
#   for n in range(lower, upper + 1):
#      included.add(Fraction(n, d))

#print included, len(included)
