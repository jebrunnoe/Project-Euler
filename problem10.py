import math

def prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
	if n % i == 0: return False
    return True
accum = 2
for i in range(3, 2*pow(10, 6), 2):
    if prime(i):
	accum += i
print accum
