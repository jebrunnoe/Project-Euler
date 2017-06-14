from math import sqrt

def prime(n):
    for i in range(2, int(sqrt(n)) + 1):
	if n % i == 0: return False
    return True

def cycle(s):
    l = len(s)
    c = []
    while len(c) < l:
	c.append(s)
	s = s[l-1] + s[0:l-1]
    return c

limit = 1000000
circ = set()

for i in range(2, limit):
    s = str(i)
    if all(prime(int(p)) for p in cycle(s)): circ.add(i)
print len(circ)
