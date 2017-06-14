f1 = 1
f2 = 1
fib = 1
i = 2
while(len(str(fib)) < 1000):
    fib = f1 + f2
    f1 = f2
    f2 = fib
    i += 1
print len(str(fib)), i
