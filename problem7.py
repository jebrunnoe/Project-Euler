#PROBLEM:
#  7
#
#NAME:
#  "10001st Prime"
#
#PROMPT:
#  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#  we can see that the 6th prime is 13. What is the 10 001st prime number?
#
#LINK:
# https://projecteuler.net/problem=7

from math import sqrt 

# Check if n is prime by looking for divisors
def is_prime(n):
   for i in range(2, int(sqrt(n) + 1)):
      if n % i == 0: return False   # If i divides n, n is not prime
   return True

count = 1 # Start count at 1 to account for '2'
i = 1
while count < 10001:
   i += 2   # Iterate by 2 because no even numbers greater than 2 are prime
   if is_prime(i): count += 1
print count, i
