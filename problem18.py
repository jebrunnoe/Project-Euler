#PROBLEM:
#  18
#
#NAME:
#  "Maximum Path Sum I"
#
#LINK:
#  https://projecteuler.net/problem=18

import time
start_time = time.time()

data_raw = """75 95 64 17 47 82 18 35 87 10 20 04 82 47 65
	 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 
	 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33
	 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 
	 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 
	 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 
	 48 63 66 04 68 69 53 67 30 73 16 69 87 40 31
	 04 62 98 27 23 09 70 98 73 93 38 53 69 04 23"""

data_string = data_raw.split()
data_iter = 0
rows = 15
nodes = []

class Node():
   def __init__(self, value, path_sum):
      self.value = value
      self.path_sum = path_sum # This is the maximum path sum to this node.

# Parse the data into rows of nodes.
for row in range(rows):
   node_row = list()
   for col in range(row + 1):
      node_row.append(Node(int(data_string[data_iter]), 0)) #
      data_iter += 1
   nodes.append(node_row)

# Initialize the last row of nodes, setting the path_sum value equal to the node value. 
for col in range(len(nodes[:-1])):
   nodes[len(nodes) - 1][col].path_sum = nodes[len(nodes) - 1][col].value

# Starting on the second to last row of nodes, calculate the maximum path to each node.
for row in range(len(nodes) - 2, -1, -1):
   for col in range(len(nodes[row]) - 1, -1, -1):
      # Set the path sum of the current node to the value of 
      # the current node plus the maximum path sum of the two nodes below it.
      nodes[row][col].path_sum = nodes[row][col].value + max(nodes[row + 1][col + 1].path_sum, nodes[row + 1][col].path_sum)

# Calculate the sum of the node values that trace the optimum path. 
def path(row, col, total):
   total += nodes[row][col].value
   if row == len(nodes) - 1: 
      return total # The bottom of the triangle has been reached.
   if nodes[row + 1][col + 1].path_sum > nodes[row + 1][col].path_sum: 
      col += 1
   total = path(row + 1, col, total)
   return total 

print path(0, 0, 0)
print "Runtime: %.5fs" % (time.time() - start_time)
