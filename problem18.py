raw = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 69 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 69 04 23"""

string = raw.split()
rows = 15
i = 0
tri = []

class Node():
    def __init__(self, value, local):
        self.value = value
	self.local = local

for row in range(rows):
    r = []
    for col in range(row + 1):
	r.append(Node(int(string[i]), 0))
	i += 1
    tri.append(r)

for col in range(len(tri[len(tri) - 1])):
    tri[len(tri) - 1][col].local = tri[len(tri) - 1][col].value

for row in range(len(tri) - 2, -1, -1):
    for col in range(len(tri[row]) - 1, -1, -1):
	if tri[row + 1][col + 1].local > tri[row + 1][col].local:
	    tri[row][col].local = tri[row][col].value + tri[row + 1][col + 1].local
	else: tri[row][col].local = tri[row][col].value + tri[row + 1][col].local

def path(row, col, total):
    total += tri[row][col].value
    if row == len(tri) - 1: return total
    if tri[row + 1][col + 1].local > tri[row + 1][col].local: col += 1
    total = path(row + 1, col, total)
    return total

print path(0, 0, 0)
