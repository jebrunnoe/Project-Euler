table = {}
table[0, 0] = 0
table[1, 0] = 0
table[0, 1] = 1
table[1, 1] = 1

def partition(n):
   for row in range(n):
      table[row, n] = table[row, n - 1]
   table[n, 0] = 0
   for col in range(1, n + 1):
      table[n, col] = table[n, col - 1] + table[n - col, col]
   return table[n, n]

n = 2
while partition(n) % 1000000 != 0:
   if n % 1000 == 0: print n
   n += 1
print n

