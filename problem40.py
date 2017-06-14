digit_count = 0
product = 1
d = [1, 10, 100, 1000, 10000, 100000, 1000000]
for posInt in range(1, 981500):
   posInt_str = str(posInt)
   for i in range(len(posInt_str)):
      digit_count += 1
      if digit_count in d: product *= int(posInt_str[i])
print(product)
