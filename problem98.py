from operator import itemgetter

def find_anagrams(words_orig):
   words_sort = []
   word_numbr = 1
   for w in words_orig:
      wordS = sorted(w)
      wordS = "".join(wordS)
      words_sort.append([wordS, word_numbr, w])
      word_numbr += 1
   words_sort = sorted(words_sort, key=itemgetter(0)) 
   lastw= [""]
   anagrams = []
   for w in words_sort:
      if w[0] == lastw[0] and w[2] != lastw[2][::-1]:   # watch out for palindromes
	 #print(lastw[0], " ", lastw[1], " ", lastw[2], "\n",w[0]," ",w[1]," ", w[2], "\n")
	 anagrams.append([lastw[2], w[2]])
      lastw = w
   return anagrams

raw = open("p098_words.txt", "r").read()
anagrams = find_anagrams(raw.replace('"', '').split(','))

squares = [[], [], [], [], [], [], [], [], [], []]

for n in range(10, 31427):
   s = n*n
   l = len(''.join(set(str(s))))
   if len(str(s)) - len(''.join(set(str(s)))) < 2:
      squares[l].append(s)

def rep(n):
   for i in range(len(n)):
      for j in range(len(n)):
	 if i == j: continue
	 if n[i] == n[j]:
	    return (i, j)
   return None

result = list()
for an in anagrams:
   a = an[0]
   b = an[1]
   for s in squares[len(''.join(set(a)))]:
      ss = str(s)
      if len(ss) == len(a):
	 if rep(a) == rep(ss):
	    scheme = dict()
	    for i in range(len(a)):
	       scheme[a[i]] = ss[i]
	    t = ''
	    for d in b:
	       t += scheme[d]
	    if t[0] == '0': continue
	    t = int(t)
	    sr = t**0.5
	    if int(sr) == sr:
	       result.append(t)
	       result.append(s)

print result, max(result)

