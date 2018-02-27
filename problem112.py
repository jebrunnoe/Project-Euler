#PROBLEM:
#  112
#
#NAME:
#  "Bouncy Numbers"
#
#PROMPT:
#  
#  Working from left-to-right if no digit is exceeded by the digit to its 
#  left it is called an increasing number; for example, 134468. Similarly 
#  if no digit is exceeded by the digit to its right it is called a decreasing 
#  number; for example, 66420. We shall call a positive integer that is 
#  neither increasing nor decreasing a "bouncy" number; for example, 155349.
#  Clearly there cannot be any bouncy numbers below one-hundred, but just over 
#  half of the numbers below one-thousand (525) are bouncy. In fact, the least 
#  number for which the proportion of bouncy numbers first reaches 50% is 538.
#  Surprisingly, bouncy numbers become more and more common and by the time we 
#  reach 21780 the proportion of bouncy numbers is equal to 90%. Find the 
#  least number for which the proportion of bouncy numbers is exactly 99%.
#
#LINK:
#  https://projecteuler.net/problem=112

import time
start_time = time.time()
target = 0.99

def bouncy(n):
   pos_delta = False # Positive change between consecutive digits.
   neg_delta = False # Negaitve change between consecutive digits.
   for i in range(len(n) - 1):
      if n[i] > n[i + 1]: 
	 neg_delta = True
      if n[i] < n[i + 1]: 
	 pos_delta = True
      if pos_delta and neg_delta: return True # n is bouncy.
   return False 

n = 100 
b = float(0) # Use float to avoid rounding down to zero.
while b / n < target:
   n = n + 1
   if bouncy(str(n)): 
      b = b + 1

print n
print "Runtime: %.2fs" % (time.time() - start_time)
