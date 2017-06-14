n = 600851475143
f = 2
factors = []
while n >= f:
    while n % f == 0:
	factors.append(f)
	n = n / f
    f += 1
print max(factors)
