ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
lib = [""]
count = 0
for n in range(1, 1001):
    if n < 1000:
	if n < 100:
	    if n < 20:
		if n < 10: word = ones[int(str(n)[0])]
		else: word = teens[int(str(n)[1])]	    
	    elif n % 10 == 0: word = tens[int(str(n)[0])] 
	    else: word = tens[int(str(n)[0])] + "-" + ones[int(str(n)[1])]
	    lib.append(word)
	elif n % 100 == 0: word = ones[int(str(n)[0])] + " hundred "
	else: word = ones[int(str(n)[0])] + " hundred and " + lib[n % 100]
    else: word = "one thousand"
    for i in range(len(word)):
	if word[i] != "-" and word[i] != " ": count = count + 1
print count
    
