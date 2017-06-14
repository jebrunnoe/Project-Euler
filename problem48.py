sum = 0
for n in range(1, 1001):
   sum += n**n
print str(sum)[len(str(sum))-10:]
