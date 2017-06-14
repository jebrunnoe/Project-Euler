import math
n = str(math.factorial(100))
f = 0
for i in range(len(n)):
    f += int(n[i])
print f
