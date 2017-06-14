from math import sqrt
from itertools import combinations 

def prime(p):
   if p < 2 or any(p % i == 0 for i in range(2, int(sqrt(p)) + 1)): return False
   return True

prime_list = list()
for i in range(56003, 1000000, 2):
   if prime(i): prime_list.append(i)
prime_set = set(prime_list)
 
def search(target):
   for p in prime_list:
      if p in prime_set:
         n_str = str(p)
         n_len = len(n_str)
	 available_indices = ""
	 for i in range(n_len): available_indices += str(i)
	 for replace_count in range(1, n_len):
	    replace_indices = combinations(available_indices, replace_count)
	    for replace_scheme in replace_indices:
	       family = list()
	       for digit in range(10):
		  temp_str = n_str
		  for i in range(len(replace_scheme)):
		     index = int(replace_scheme[i])
		     temp_str = temp_str[:index] + str(digit) + temp_str[index + 1:]
		  temp = int(temp_str)
		  if temp >= p and temp in prime_set: family.append(temp_str)
		  if len(family) == target: return family	     
family_size = 8
print search(family_size)
