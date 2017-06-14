from itertools import permutations
from math import sqrt
 
def prime(n):
   if n < 2 or any(n % i == 0 for i in range(2, int(sqrt(n)) + 1)): return False
   return True
 
for n in range(1000, 9999):
   if  prime(n):
      p4 = ("".join(x) for x in permutations(str(n)))
      pSet = set()
      for p in p4:
         pInt = int(p)
         if pInt > 1000 and prime(pInt):
            pSet.add(pInt)
      sSet=sorted(pSet)
      sList = list(sSet)
      for i in range(len(sList)):
         for j in range(i + 1, len(sList)):
            element3 = sList[j] * 2  - sList[i]
            if element3 in pSet:
               print sList[i], sList[j], element3
        
