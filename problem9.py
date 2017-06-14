for a in range(1, 334):
	b = (500000 - (1000 * a)) / (1000 - a)
	c = (a ** 2 - (1000 * a) + 500000) / (1000 - a)
	if a + b + c == 1000:
		product = a * b * c
print product
