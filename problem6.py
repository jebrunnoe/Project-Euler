#PROBLEM:
#  6
#
#NAME:
#  "Sum Square Difference"
#
#PROMPT:
#  The sum of the squares of the first ten natural numbers is,
#  1^2 + 2^2 + ... + 10^2 = 385. The square of the sum of the first 
#  ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
#  Hence the difference between the sum of the squares of the first 
#  ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#  Find the difference between the sum of the squares of the first 
#  one hundred natural numbers and the square of the sum.
#
#LINK:
#  https://projecteuler.net/problem=6

sum_of_squares = 0
sum = 0
# Iterate through the first 100 natural numbers
for n in range(1, 101):
   sum_of_squares += n * n # Accumulate the square of each number
   sum += n # Keep a running sum to be squared afterward
print sum * sum - sum_of_squares # Print the difference
