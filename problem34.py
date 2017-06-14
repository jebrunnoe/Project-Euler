import math
match = set()
facts = []
for f in range(10): facts.append(math.factorial(f))
for i in range(3, 7 * facts[9]):
	s = str(i)
	a = 0
	for j in range(len(s)): a += facts[int(s[j])]
	if i == a: match.add(i)
print sum(match)
