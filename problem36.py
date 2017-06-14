def palindrome(s):
   if s == s[::-1]:
      return True
   return False
 
sum = 0
for i in range(1, 1000000):
   if palindrome(str(i)) and palindrome(str(bin(i))[2:]):
      sum += i
print sum 
