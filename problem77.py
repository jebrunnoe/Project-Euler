def sieve(limit):
   a = [True] * limit
   a[0] = a[1] = False
   for (i, isprime) in enumerate(a):
      if isprime:
	 yield i
         for n in xrange(i * i, limit, i):
	    a[n] = False

table = {}

def initialize(n):
   for row in range(n + 1):
      if row % 2 == 0: table[row, 2] = 1
      else: table[row, 2] = 0
   for col in range(len(primes)):
      table[0, primes[col]] = 1


def build(n):
   initialize(n)
   for row in range(1, n + 1):
      for col in range(1, len(primes)):
	 table[row, primes[col]] = table[row, primes[col - 1]]
	 if row >= primes[col]:
	    table[row, primes[col]] += table[row - primes[col], primes[col]]
   return table[n, primes[len(primes) - 1]]

target = 10
primes = list(sieve(target))
while build(target) <= 5000:
   target += 1
   primes = list(sieve(target))
print target

