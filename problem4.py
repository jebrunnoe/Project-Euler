#PROBLEM:
#	4
#
#NAME:
#	"Largest Palindrome Product"
#
#PROMPT:
#	A palindromic number reads the same both ways. The largest palindrome 
#	made from the product of two 2-digit numbers is 9009 = 91 x 99.
#	Find the largest palindrome made from the product of two 3-digit numbers. 
#
#LINK:
#	https://projecteuler.net/problem=4

palindrome = 0
# Iterate through all pairs of 3 digit numbers and check for a palindrome
for i in range(100, 1000):
    for j in range(100, 1000):
	product = str(i * j)
	reverse = product[::-1]
	if product == reverse and int(product) > palindrome: # Make sure it's the largest palindrome
	    palindrome = int(product)
print palindrome
