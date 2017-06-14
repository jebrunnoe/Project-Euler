import re
 
def digital(base, multi):
   if len(base) == len(multi) and all(re.search(digit, multi) for digit in base): return True
   return False

limit = 6
found = False
n = 1

while not found:
   if all(digital(str(n), str(m * n)) for m in range(2, limit + 1)): 
      found = True
   else: n += 1   
print n
