#PROBLEM:
#  111
#
#NAME:
#  "Primes with runs"
#
#PROMPT:
#  Considering 4-digit primes containing repeated digits it is clear that 
#  they cannot all be the same: 1111 is divisible by 11, 2222 is divisible 
#  by 22, and so on. But there are nine 4-digit primes containing three ones:
#	 1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
#  We shall say that M(n, d) represents the maximum number of repeated digits 
#  for an n-digit prime where d is the repeated digit, N(n, d) represents the 
#  number of such primes, and S(n, d) represents the sum of these primes.
#  So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime 
#  where one is the repeated digit, there are N(4, 1) = 9 such primes, and the 
#  sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is 
#  only possible to have M(4, 0) = 2 repeated digits, but there are 
#  N(4, 0) = 13 such cases.
#  In the same way we obtain the following results for 4-digit primes.
#
#  Digit, d    M(4, d)	   N(4, d)  S(4, d)
#     0	       2	   13	    67061
#     1	       3	   9	    22275
#     2	       3	   1	    2221
#     3	       3	   12	    46214
#     4	       3	   2	    8888
#     5	       3	   1	    5557
#     6	       3	   1	    6661
#     7	       3	   9	    57863
#     8	       3	   1	    8887
#     9	       3	   7	    48073
#
#  For d = 0 to 9, the sum of all S(4, d) is 273700.
#  Find the sum of all S(10, d).
#
#LINK:
#  https://projecteuler.net/problem=111

from math import sqrt
import itertools
import time

start_time = time.time()
n = 10
upper = 100000 # This is the upper bound for the sieve. 100,000 is the maximum needed because sqrt(10,000,000,000) = 10,0000.
minimum = 1000000000 # This is the minimum ten digit number.
S = list() # This is a list of all S(n, d) described in the prompt.

def sieve(upper):
   a = [True] * (upper + 1)
   a[0] = a[1] = False
   for (i, isprime) in enumerate(a):
      if isprime:
	 yield i
         for n in xrange(i * i, upper + 1, i):
	    a[n] = False

primes = list(sieve(upper)) # All prime numbers up to 100,000.

def is_prime(n):
   if n < 2: return False
   for p in primes:
      if p > int(sqrt(n)): # Note that the maximum possible sqrt(n) is 100,000.
	 break
      if n % p == 0: return False
   return True

# Example: [1, 2, 3, 4] --> 1,234.
def list_to_integer(l):
   n = ""
   for i in range(len(l)):
      n += str(l[i])
   return int(n)

def insert(skeletons, M):
   candidates = set()
   # If M digits are fixed, the other n - M are free to be varied.
   # Generate all possible (n - M)-tuples to insert into the non-fixed slots.
   inserts = list(itertools.product(range(10), repeat = n - M))
   # Plug each insert tuple into the free indices of each skeleton. 
   for insert in inserts:
      for skeleton in skeletons:
	 temp = list(skeleton)
	 insert_iter = 0
	 # Check each digit, if it is free, plug in the appropriate insert. 
	 for i in range(n):
	    if temp[i] == None: # This digit is not fixed. 
	       temp[i] = insert[insert_iter]
	       insert_iter = insert_iter + 1
	 candidates.add(tuple(temp)) # Use a tuple so temp can be added to a set.
   return candidates

for d in range(10): 
   for M in range(n - 1, 0, -1): # This is M(n, d) described in the prompt. Start at n - 1 and count down.
      fixed_indices_list = list(itertools.combinations(range(n), M)) 
      skeletons = list()
      # Set all the fixed indices to the digit d.
      # Non-fixed digits will be left as 'None' for now.
      for fixed_indices in fixed_indices_list:
	 skeleton = [None] * n 
	 for index in fixed_indices:
	    skeleton[index] = d 
	    skeletons.append(skeleton)
      candidates = insert(skeletons, M) # Build all potential primes with runs.
      primes_with_runs = list()	    
      # Check each candidate for leading zeros by checking against minimum, then check if it is prime.
      for candidate in candidates:
	 integer_candidate = list_to_integer(candidate)
      	 if integer_candidate >= minimum and is_prime(integer_candidate):  
	    primes_with_runs.append(integer_candidate) # Found an n digit prime with M(n, d) repeated digits. 
      # If true, at least one n digit prime was found with M repeated digits, 
      # no need to check smaller M(n, d). Move on to the next digit d.
      if len(primes_with_runs) > 0:  
	 S.append(sum(primes_with_runs)) # Save this S(n, d). 
	 break 

print sum(S)
print("Runtime: %s seconds" % (time.time() - start_time))
