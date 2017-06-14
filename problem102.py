import numpy as np
from numpy.linalg import *

raw = open("p102_triangles.txt", "r").read().split()
triangles = list()
for r in raw:
   s = r.split(',')   
   triangles.append([[int(s[0]), int(s[1])], [int(s[2]), int(s[3])], [int(s[4]), int(s[5])]])

result = 0
for t in triangles:
   A = t[0]
   B = t[1]
   C = t[2]
   a = np.array([[C[0]-A[0], B[0]-A[0]],[C[1] - A[1], B[1]-A[1]]])
   b = np.array([-A[0], -A[1]])
   x = solve(a, b)
   c1 = x[0]
   c2 = x[1]
   if c1 >= 0 and c2 >= 0 and c1 + c2 <= 1: result += 1

print result
