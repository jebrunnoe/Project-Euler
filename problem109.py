limit = 100
result = 0
scores = list()
doubles = list()

for i in range(1, 21):
   scores.append(i)
   scores.append(2 * i)
   scores.append(3 * i)
scores.append(25)
scores.append(50)


for i in range(1, 21):
   doubles.append(2 * i)
doubles.append(50)

for third in doubles:
   if third < limit:
      result += 1

for i in range(len(scores)):
   for third in doubles:
      if scores[i] + third < limit:
	 result += 1

for i in range(len(scores)):
   for j in range(i, len(scores)):
      for third in doubles:
	 if scores[i] + scores[j] + third < limit:
	    result += 1
	 
print result
   
