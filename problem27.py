import math
maxprime = 0
product = 0

def prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
	if n % i == 0: return False
    return True

primes = []
for p in range(1, 1000):
    if prime(p): primes.append(p)

def counter(a, b):
    n = 0
    while True:
	p = pow(n, 2) + a * n + b
	if p > 0 and prime(p): n += 1
	else: break
    return n

for b in primes:
    for a in range(-999, 1000):
	count = counter(a, b)
	if count > maxprime:
	    maxprime = count
	    product = a * b
	
print product
