def fib(n):
   v1, v2, v3 = 1, 1, 0
   for rec in bin(n)[3:]:
      calc = v2 * v2
      v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
      if rec == '1':   
	 v1, v2, v3 = v1+v2, v1, v2
   return v2

Fn1 = 259695496911122585
Fn2 = 160500643816367088
k = 86
found = False
control = ['1', '2', '3', '4', '5', '6' , '7', '8' , '9']
while not found:
   Fn = (Fn1 + Fn2) % 10**9
   s = str(Fn)
   if len(s) == 9:
      if not any (c == '0' for c in s):
	 if sorted(s) == control:
	    F = fib(k)
	    if sorted(str(F)[:9]) == control:
	       result = k
	       found = True 
   Fn2 = Fn1 
   Fn1 = Fn
   k += 1

print result
