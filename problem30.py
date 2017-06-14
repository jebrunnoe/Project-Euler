accum = 0
for i in range(2, 355000):
    n = str(i)
    s = 0
    for j in range(len(n)):
    	s += pow(int(n[j]), 5)
    if i == s: accum += i
print accum
