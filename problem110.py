#PROBLEM:
#  110
#
#NAME:
#  Diophantine Reciprocals II
#
#PROMPT:
#  In the following equation x, y, and n are positive integers.
#		  1/x + 1/y = 1/n
#  It can be verified that when n = 1260 there are 113 distinct solutions 
#  and this is the least value of n for which the total number of distinct 
#  solutions exceeds one hundred. What is the least value of n for which 
#  the number of distinct solutions exceeds four million?
#
#NOTE: 
#  This problem is a much more difficult version of Problem 108 and 
#  as it is well beyond the limitations of a brute force approach it 
#  requires a clever implementation.
#
#LINK:
#  https://projecteuler.net/problem=110

import time

start_time = time.time()
limit = 4000000
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

# Recursively generate the additive partitions of n. For example, the partitions of 
# 5 are [5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1] and [1, 1, 1, 1, 1]
def partitions(n):
   if n == 0:
      yield []
      return		
   for p in partitions(n - 1):
      yield [1] + p
      if p and (len(p) < 2 or p[1] > p[0]):
	 yield [p[0] + 1] + p[1:]

# Calculate the number of divisors that n^2 will have, if n has the 
# prime factorization with the given exponents. Note that if p0...pn 
# are prime and n = p0^a0 * p1^a1 * p2^a2 * ... * pn^an, the number 
# of divisors of n^2 will be the product (2a0 + 1)(2a1 + 1)(2a2 + 1)...(2an + 1)
def divisor_count(exponents):
   product = 1
   for a_n in exponents:
      product *= 2 * a_n + 1
   return product

# Find the smallest number that has the prime factorization with 
# the given exponents. Note that if p0...pn are prime and 
# n = p0^a0 * p1^a1 * p2^a2 * ... * pn^an, the number will occur when
# the primes are in ascending order and the exponents are in descending order.
def convert(exponents):
   number = 1
   for i in range(len(exponents)):
      number *= primes[i] ** exponents[i]
   return number

candidates = list()  # List of all n such that (divisor_count(n^2))/2 > limit
# A partition size of 14 is the minimum required. Note that the maximum divisor count
# occurs when the partition is such that a_n = 1 for all n. In this case, (2a_n + 1) = 3. 
# Solving 3^n = limit for n gives a lower bound of 14. 
for partition_size in range(14, len(primes)):
   # Iterate through each additive partition and use it, 
   # in descending order, as the exponents of the prime factorization.
   for p in list(partitions(partition_size)):
      exponents = p[::-1] # Put exponents in descending order.
      # If the exponent list is one that results in enough distict solutions,
      # save the smallest n that has that prime factorization to the candidate list.
      if divisor_count(exponents) > 2 * limit:
	 candidates.append(convert(exponents))

# Output the minimum candidate and the time of execution.
print min(candidates)
print("%s seconds" % (time.time() - start_time))
