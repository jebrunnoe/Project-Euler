limit = 1000000

def sieve(limit):
   a = [True] * limit
   a[0] = a[1] = False
   for (i, isprime) in enumerate(a):
      if isprime:
	 yield i
         for n in xrange(i * i, limit, i):
	    a[n] = False

primes = list(sieve(limit))

divSums = [0] * limit
for factor in range(1, limit / 2):
   for product in range(2 * factor, limit, factor):
      divSums[product] += factor

toOne = [False] * limit
used = [False] * limit

for p in primes: 
   toOne[p] = True
chains = list()

for start in range(limit):
   chain = [start]
   n = start
   while n < limit:
      if toOne[n]:
	 for c in chain:
	    toOne[c] = True
	 break
      if used[n]:
	 break
      n = divSums[n]
      if n in chain:
	 if n == start:
	    chains.append(chain)
	    for c in chain:
	       used[c] = True	 
	 break
      chain.append(n)

maxLen = 0
maxChain = []

for chain in chains: 
   if len(chain) > maxLen:
      maxLen = len(chain)
      maxChain = chain

print maxChain, min(maxChain)
