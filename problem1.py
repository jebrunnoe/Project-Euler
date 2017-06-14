#NAME: 
#  Problem 1 "Multiples of 3 and 5"
#
#PROMPT: 
#  If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#  we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of 
#  all the multiples of 3 or 5 below 1000.
#
#LINK:
#  https://projecteuler.net/problem=1

sum = 0	 # Initialize the sum to zero
for i in range(3, 1000):  
   if i % 3 == 0 or i % 5 == 0: # If i is a multiple of 3 or 5, add it to the sum
      sum += i
print sum	
