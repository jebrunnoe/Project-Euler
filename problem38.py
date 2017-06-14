import re
 
def pandigital(s):
   for pattern in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      if not re.search(pattern, s ): return False
   return True
 
max = 0
for integer in range(1, 10000):
   n = 1
   concatInt = integer
   concat = str(concatInt)
   while concatInt <= 987654321:
      if pandigital(concat) and concatInt > max: max = concatInt
      n += 1
      concat += str(n * integer)  
      concatInt = int(concat)
print max
