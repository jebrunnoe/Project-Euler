denom = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
matrix = {}
for row in range(target + 1):
    matrix[row, 0] = 1
for row in range(target + 1):
    print row, ':', 1, 
    for col in range(1, len(denom)):
	matrix[row, col] = 0
	if row >= denom[col]:
	    matrix[row, col] += matrix[row, col - 1] + matrix[row - denom[col], col]
	else:
	    matrix[row, col] = matrix[row, col - 1]
	print matrix[row, col],
    print
print matrix
