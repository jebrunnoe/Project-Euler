#PROBLEM:
#  5
#
#NAME: 
#  "Smallest Multiple"
#
#PROMPT:
#  2520 is the smallest number that can be divided by each 
#  of the numbers from 1 to 10 without any remainder. What 
#  is the smallest positive number that is evenly divisible 
#  by all of the numbers from 1 to 20?

# For this problem, all that is to break down each number 
# 1-20 into it's prime factorization, noting the power on 
# prime. Then the product of each prime raised to the highest
# power that appears will produce the answer.

print 1 * 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
