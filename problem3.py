#PROBLEM: 
#  3
#
#NAME: 
#  "Largest Prime Factor"
#
#PROMPT:
#  The prime factors of 13195 are 5, 7, 13 and 29. 
#  What is the largest prime factor of the number 600851475143 ?
#
#LINK:
#  https://projecteuler.net/problem=3

num = 600851475143

def get_prime_factors(n):
   factor = 2
   prime_factors = []
   while n >= factor:
      while n % factor == 0:	
	 prime_factors.append(factor) #'factor' is a prime factor of n, save it
	 n = n / factor   # repeatedly divide n by factor until n is no longer divisible by it
      factor += 1
   return prime_factors

print max(get_prime_factors(num)) 
