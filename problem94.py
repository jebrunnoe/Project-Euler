L = 10**9
x = 2
y = 1
result = 0

while True:
   a = (2 * x + 1) / 3.
   b = a + 1
   if 2 * a + b > L: break
   A = ((x + 2) * y) / 3.
   if int(a) == a and int(A) == A and A > 0:
      result += 2 * a + b
   a = (2 * x - 1) / 3.
   b = a - 1
   A = ((x - 2) * y) / 3.
   if 2 * a + b > L: break
   if int(a) == a and int(A) == A and A > 0:
      result += 2 * a + b
   nextx = 2 * x + 3 * y
   nexty = x + 2 * y   
   x = nextx
   y = nexty   

print result
