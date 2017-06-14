maxcount = 0
max_p = 0
for p in range(12, 1000):
   count = 0
   for b in range(1, p // 4): 
      a = (p ** 2 - 2. * p * b) / (2. * (p - b))
      if int(a) == a:
         count += 1
         if count > maxcount:
            max_p = p
            maxcount = count
print max_p    
