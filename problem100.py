from math import sqrt

limit = 10**12
n = 1
b = 0
r = 0
while b + r < limit:
   b = (1/8.)*(2*pow(3-2*sqrt(2), n)+sqrt(2)*pow(3-2*sqrt(2),n)+2*pow(3+2*sqrt(2), n)-sqrt(2)*pow(3+2*sqrt(2), n) + 4)
   r = -(pow(3-2*sqrt(2),n-1) -pow(3+ 2*sqrt(2), n-1))/(4*sqrt(2))
   print b, r, b + r
   n += 1
