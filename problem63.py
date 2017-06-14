members = list()
for p in range(1, 100):
   for base in range(1, 10):
      n = pow(base, p)
      if len(str(n)) == p: members.append(n)
print len(members)
