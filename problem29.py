c = set()
for a in range(2, 101):
    for b in range(2, 101):
	c.add(pow(a, b))
print len(c)
