raw = open("p067_triangle.txt", "r")
string = raw.read().split()
print string
rows = 100
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
