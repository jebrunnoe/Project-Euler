#PROBLEM:
#  10
#
#NAME:
#  "Summation of Primes"
#
#PROMPT:
#  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. 
#  Find the sum of all the primes below two million.
#
#LINK:
#  https://projecteuler.net/problem=10

from math import sqrt

def is_prime(n):
   for i in range(2, int(sqrt(n) + 1)):
      if n % i == 0: 
	 return False
   return True

sum = 2	 # Set sum equal to 2 to account for 2 being prime
# Increment up to the limit by 2 to skip even numbers
for i in range(3, 2000000, 2):
   if is_prime(i):
      sum += i
print sum
