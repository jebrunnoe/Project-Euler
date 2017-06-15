#PROBLEM:
#  9
#
#NAME:
#  "Special Pythagorean Triplet"
#
#PROMPT:
#  A Pythagorean triplet is a set of three natural numbers, a < b < c, 
#  for which, a^2 + b^2 = c^2. For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#  Find the product abc.
#
#LINK:
#  https://projecteuler.net/problem=9

# Given the two equations, a^2 + b^2 = c^2 and a + b + c  = 1000, 
# solve for b and c as functions of a, then iterate through a and 
# check the two equations for truth. Note that, because a < b < c, 
# a must be less than 1000 / 3, so use 333 as an upper limit for a.  
for a in range(1, 334):
   b = (500000 - (1000 * a)) / (1000 - a)
   c = (a ** 2 - (1000 * a) + 500000) / (1000 - a)
   if a + b + c == 1000 and a * a + b * b == c * c:
      product = a * b * c
print product
