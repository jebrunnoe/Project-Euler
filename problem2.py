fib  = 0
fib1 = 1
fib2 = 2
accum = 0
while fib1 <= 4000000: 
    if fib1 % 2 == 0:
	accum += fib1
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
print accum



	
