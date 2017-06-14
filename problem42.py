raw = open("p042_words.txt", "r").read()
words = raw.replace('"', '').split(',')
 
def value(name):
   value = 0
   for i in range(len(name)):
      value += ord(name[i]) - 64
   return value
 
triangles = set()
for n in range(1, 1000):
   triangles.add(int(n * (n + 1) / 2))
 
count = 0
for word in words:
   if value(word) in triangles:
      count += 1
 
print count
