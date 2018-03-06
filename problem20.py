#PROBLEM:
#  20
#
#NAME:
#  "Factorial Digit Sum"
#
#LINK:
#  https://projecteuler.net/problem=20

import math
import time
start_time = time.time()

number = str(math.factorial(100))
digit_sum = 0
for i in range(len(number)):
    digit_sum += int(number[i])

print digit_sum
print "Runtime: %.5fs " % (time.time() - start_time)
