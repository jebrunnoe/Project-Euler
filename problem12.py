def factor(n):
    factors = []
    factors.append(1)
    for i in range(2, int(n ** 0.5) + 1):
	if n % i == 0:
	    factors.append(i)
	    factors.append(n / i)
    factors.append(n)
    return factors
i = 1
while len(factor((i * (i + 1)) / 2)) < 501: i = i + 1
print (i * (i + 1)) / 2



