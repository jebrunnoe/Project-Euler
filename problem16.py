#PROBLEM:
#  16
#
#NAME:
#  "Power Digit Sum"
#
#PROMPT:
#  2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#  What is the sum of the digits of the number 2^1000?
#
#LINK:
#  https://projecteuler.net/problem=16

import time
start_time = time.time()

number = str(pow(2, 1000))
digit_sum = 0
for i in range(len(number)):
    digit_sum+= int(number[i])

print digit_sum
print "Runtime: %.5fs" % (time.time() - start_time)
