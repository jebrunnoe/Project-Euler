def palindrome(s):
   if s == s[::-1]:
      return True
   return False

lychrels = list()

for n in range(1, 10000):
   lychrel = True
   s = str(n) 
   iterations = 0
   result = n
   while lychrel and iterations <= 50:
      result = result + int(str(result)[::-1])
      if palindrome(str(result)): 
	 lychrel = False
      iterations += 1
   if lychrel: lychrels.append(s)
print lychrels, len(lychrels)
