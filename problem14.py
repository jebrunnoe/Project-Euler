#PROBLEM:
#  14
#
#NAME:
#  "Largest Collatz Sequence"
#
#PROMPT:
#  The following iterative sequence is defined for the set of positive integers:
#	 n -> n/2    (n is even)
#	 n -> 3n + 1 (n is odd)
#  Using the rule above and starting with 13, we generate the following sequence:
#	 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#  It can be seen that this sequence (starting at 13 and finishing at 1) contains 
#  10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
#  that all starting numbers finish at 1. Which starting number, under one million,
#  produces the longest chain_length? NOTE: Once the chain_length starts the terms are allowed 
#  to go above one million.
#
#LINK:
#  https://projecteuler.net/problem=14

max_chain = 0
max_seed = 0
limit = 1000000

# Iterate through starting numbers, or 'seeds' 
for seed in range(1, limit):
   n = seed
   chain_length = 1
   # Generate the collatz sequence until the chain_length ends in 1,
   # keeping track of the chain_length length  
   while n > 1:
      if (n % 2) == 0: 
	 n = n / 2
      else: 
	 n = (3 * n) + 1 
      chain_length = chain_length + 1 
   # If the current chain_length is the longest, save it and the seed that started it
   if chain_length > max_chain: 
      max_seed = seed
      max_chain = chain_length

print max_seed, max_chain
