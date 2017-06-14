max_digit_sum = 0
for a in range(100):
   for b in range(100):
      n = pow(a, b)
      s = str(n)
      digit_sum = 0
      for digit in range(len(s)): digit_sum += int(s[digit])
      if digit_sum > max_digit_sum: max_digit_sum = digit_sum
print max_digit_sum
