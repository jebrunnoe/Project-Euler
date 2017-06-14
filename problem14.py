maxChain = 0
maxSeed = 0
bound = 1000000
for seed in range(1, bound):
    n = seed
    chain = 1
    while n > 1:
	if (n % 2) == 0: n = n / 2
	else: n = (3 * n) + 1 
	chain = chain + 1
    if chain > maxChain: 
	maxSeed = seed
	maxChain = chain
print maxSeed, maxChain
