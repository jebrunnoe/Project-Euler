palindrome = 0
for i in range(1, 1000):
    for j in range(1, 1000):
	product = str(i * j)
	reverse = product[::-1]
	if product == reverse and int(product) > palindrome:
	    palindrome = int(product)
print palindrome
