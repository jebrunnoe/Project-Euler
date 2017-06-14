from math import sqrt 

def prime(n):
    for i in range(2, int(sqrt(n) + 1)):
	if n % i == 0: return False
    return True
count = 1 
i = 1
while count < 10001:
    i += 2
    if prime(i): count += 1
print count, i
