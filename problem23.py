def factor(n):
    factors = []
    factors.append(1)
    for i in range(2, int(n ** 0.5) + 1):
	if n % i == 0:
	    factors.append(i)
	    if n / i != i: factors.append(n / i)
    return factors

abn = set()
non = 0

for i in range(1, 20162): 
    if sum(factor(i)) > i: abn.add(i)
    if not any((i - a in abn) for a in abn): non += i

print non
