romans = open("p089_roman.txt", "r").read().split()
val = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)
char = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

def read(numeral):
   dec = 0
   l = len(numeral)
   i = 0
   while i < l: 
      if i + 1 < l and val[numeral[i + 1]] > val[numeral[i]]:
	 dec += val[numeral[i + 1]] - val[numeral[i]]
	 i += 2
      else: 
	 dec += val[numeral[i]]
	 i += 1
   return dec

def trans(n):
   string = ""
   k = 100
   while k >= 1:
      while n >= 10 * k:
	 string += char[10 * k]
	 n -= 10 * k
      if n >= 9 * k:
	 string += char[9 * k]
	 n -= 9 * k
      if n >= 5 * k:
	 string += char[5 * k]
	 n -= 5 * k
      if n >= 4 * k:
	 string += char[4 * k]
	 n -= 4 * k
      k /= 10
   while n >= 1:
      string += char[1]
      n -= 1
   return string

decimals = list()
for numeral in romans:
   decimals.append(read(numeral))

minimals = list()
for dec in decimals:
   minimals.append(trans(dec))

before = 0
for r in romans:
   before += len(r)
after = 0
for m in minimals:
   after += len(m)

delta = after - before

print delta
