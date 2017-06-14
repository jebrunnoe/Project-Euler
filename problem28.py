width = 1001
x = 1
for n in range(2, (width + 1)/2 + 1):
    a = 4 * pow(n, 2) - (10 * n) + 7
    b = 4 * pow(n, 2) - (8 * n) + 5
    c = 4 * pow(n, 2) - (6 * n) + 3
    d = 4 * pow(n, 2) - (4 * n) + 1
    x += a + b + c + d
print x

