import fractions
 
target = 3./7.
min_delta = 1.
for den in range(1, 1000001):
   num = den * target  
   num = int(num)    
   delta = target - (num / den)
   if delta < min_delta and delta != 0.:
      min_delta = delta
      num_best = num
      den_best = den
     
my_gcd = fractions.gcd(num_best, den_best)
num_best /= my_gcd
den_best /= my_gcd
 
print min_delta, my_gcd, num_best, den_best

