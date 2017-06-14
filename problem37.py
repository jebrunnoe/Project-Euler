from math import sqrt

def prime(n):
    if n < 2 or any(n % i == 0 for i in range(2, int(sqrt(n)) + 1)): return False
    return True

def truncate(n):
    s = str(n)
    l = len(s)
    t = set()
    for i in range(l):
	t.add(s[0:l - i])
	t.add(s[i:l])
    return t

trunc = set()
i = 9

while len(trunc) < 11:
    if prime(i):
	if all(prime(int(p)) for p in truncate(i)): trunc.add(i)
    i += 2
print sum(trunc)


	
