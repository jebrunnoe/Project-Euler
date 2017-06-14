import numpy as np
from numpy.linalg import *

FITS = list()
degree = 10

sequence = list()
for n in range(1, degree + 1):
   pn = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10 
   sequence.append(pn)

def build_coefficient_matrix(k):
   matrix = list()
   for i in range(k):
      row = list()
      for j in range(k):
	 row.append(pow(i + 1, j))
      matrix.append(row)
   return matrix

def evaluate_polynomial(BOP_coefficients, x):
   px = 0
   for i in range(len(BOP_coefficients)):
      px += BOP_coefficients[i] * pow(x, i)
   return px

for k in range(1, degree + 1):
   matrix = build_coefficient_matrix(k)
   BOP_coefficients = solve(np.array(matrix), np.array(sequence[:k]))
   FIT = evaluate_polynomial(BOP_coefficients, k + 1)
   FITS.append(FIT)
   
print sum(FITS)
