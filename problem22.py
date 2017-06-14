raw = open("p022_names.txt", "r").read()
names = raw.replace('"', '').split(',')
names.sort()
score = 0

def value(name):
    value = 0
    for i in range(len(name)):
	value += ord(name[i]) % 32
    return value

for i in range(len(names)):
    score += value(names[i]) * (i + 1)

print score
