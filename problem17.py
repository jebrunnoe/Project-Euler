#PROBLEM:
#  17
#
#NAME:
#  "Number Letter Counts"
#
#PROMPT:
#  If the numbers 1 to 5 are written out in words: one, two, three, four, 
#  five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#  If all the numbers from 1 to 1000 (one thousand) inclusive were written 
#  out in words, how many letters would be used? NOTE: Do not count spaces 
#  or hyphens. For example, 342 (three hundred and forty-two) contains 23 
#  letters and 115 (one hundred and fifteen) contains 20 letters. The use 
#  of "and" when writing out numbers is in compliance with British usage.
#
#LINK:
#  https://projecteuler.net/problem=17

import time
start_time = time.time()

# Lookup tables.
ones  = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens  = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
words = [""]
count = 0

for n in range(1, 1001):
   if n < 1000:
      if n < 100:
	 if n < 20:
	    if n < 10: 
	       word = ones[int(str(n)[0])] # 1-9.
	    else: 
	       word = teens[int(str(n)[1])] # 10-19.	    
	 elif n % 10 == 0: 
	    word = tens[int(str(n)[0])] # 20, 30, 40,...,90.
	 else: 
	    word = tens[int(str(n)[0])] + ones[int(str(n)[1])]
	 words.append(word) # Save words for 1-99 to be recycled.
      elif n % 100 == 0: 
	 word = ones[int(str(n)[0])] + "hundred" # 100, 200,...,900.
      else: 
	 word = ones[int(str(n)[0])] + "hundredand" + words[n % 100] # Look up already written word.
   else: word = "onethousand"
   count = count + len(word)

print count
print "Runtime: %.5fs" % (time.time() - start_time)
