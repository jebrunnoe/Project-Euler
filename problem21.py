def factor(n):
    factors = [1]
    for i in range(2, int(n ** 0.5) + 1):
	if n % i == 0:
	    factors.append(i)
	    if n / i != i: factors.append(n / i)
    return factors

a = []
d = [0, 1]
for n in range(2, 10001): 
    d.append(sum(factor(n)))
	
for n in range(10001):
   if d[n] < 10000 and d[n] != n and d[d[n]] == n: a.append(n)
    
print sum(a)
