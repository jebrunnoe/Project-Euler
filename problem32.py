from itertools import permutations
prod = set()
digits = [str(i) for i in range(1, 10)]
p9 = permutations(digits)
for x in p9:
   if int(x[0]) * int(x[1] + x[2] + x[3]) == int(x[4] + x[5] + x[6] + x[7] + x[8]): prod.add(int(x[4] + x[5] + x[6] + x[7] + x[8]))
   if int(x[0]) * int(x[1] + x[2] + x[3] + x[4]) == int(x[5] + x[6] + x[7] + x[8]): prod.add(int(x[5] + x[6] + x[7] + x[8]))
   if int(x[0] + x[1]) * int(x[2] + x[3] + x[4]) == int(x[5] + x[6] + x[7] + x[8]): prod.add(int(x[5] + x[6] + x[7] + x[8]))
   if int(x[0] + x[1] + x[2]) * int(x[3] + x[4]) == int(x[5] + x[6] + x[7] + x[8]): prod.add(int(x[5] + x[6] + x[7] + x[8]))
   if int(x[0] + x[1] + x[2]) * int(x[3]) == int(x[4] + x[5] + x[6] + x[7] + x[8]): prod.add(int(x[4] + x[5] + x[6] + x[7] + x[8]))
   if int(x[0] + x[1] + x[2] + x[3]) * int(x[4]) == int(x[5] + x[6] + x[7] + x[8]): prod.add(int(x[5] + x[6] + x[7] + x[8]))
print(sum(prod))
