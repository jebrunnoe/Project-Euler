#PROBLEM:
#  22
#
#NAME:
#  "Name Scores"
#
#LINK:
#  https://projecteuler.net/problem=22

import time
start_time = time.time()

raw = open("p022_names.txt", "r").read()
names = raw.replace('"', '').split(',') # Get rid of spaces, and parse the names into a list.
names.sort()
name_scores = list()

def value(name):
    value = 0
    for i in range(len(name)):
	value += ord(name[i]) % 32 # Alphabetical value.
    return value

for i in range(len(names)):
    name_scores.append(value(names[i]) * (i + 1))

print sum(name_scores)
print "Runtime: %.5fs " % (time.time() - start_time)
