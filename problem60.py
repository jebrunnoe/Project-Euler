from math import sqrt

def prime(p):
   if p < 2 or any(p % i == 0 for i in range(2, int(sqrt(p)) + 1)): return False
   return True

def sieve(limit):
   a = [True] * limit
   a[0] = a[1] = False
   for (i, isprime) in enumerate(a):
      if isprime:
	 yield i
         for n in xrange(i * i, limit, i):
	    a[n] = False
prime_set = set(sieve(100000000))
prime_lst = list(sieve(9999))
length = len(prime_lst)

def build_pairs(n):
   pairs = set()
   for m in range(n + 1, length):
      if int(str(prime_lst[n]) + str(prime_lst[m])) in prime_set and int(str(prime_lst[m]) + str(prime_lst[n])) in prime_set:
	 pairs.add(prime_lst[m])
   return pairs

pairs = [None]*length

for p1 in range(length):
   if pairs[p1] == None: pairs[p1] = build_pairs(p1)
   for p2 in range(p1 + 1, length):
      if prime_lst[p2] not in pairs[p1]: continue
      if pairs[p2] == None: pairs[p2] = build_pairs(p2)
      for p3 in range(p2 + 1, length):
	 if prime_lst[p3] not in pairs[p1] or prime_lst[p3] not in pairs[p2]: continue
	 if pairs[p3] == None: pairs[p3] = build_pairs(p3)
	 for p4 in range(p3 + 1, length):
	    if prime_lst[p4] not in pairs[p1] or prime_lst[p4] not in pairs[p2] or prime_lst[p4] not in pairs[p3]: continue
	    if pairs[p4] == None: pairs[p4] = build_pairs(p4)
	    for p5 in range(p4 + 1, length):
	       if prime_lst[p5] not in pairs[p1] or prime_lst[p5] not in pairs[p2] or prime_lst[p5] not in pairs[p3] or prime_lst[p5] not in pairs[p4]: continue
	       print prime_lst[p1], prime_lst[p2], prime_lst[p3], prime_lst[p4], prime_lst[p5]


 
