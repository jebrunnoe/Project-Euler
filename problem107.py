network_file = open('p107_network.txt', 'r').read().split()  
data = list()
for row in network_file:
   data.append(row.split(','))

class Edge():
   def __init__(self, value, vertices):
      self.value = value
      self.vertices = vertices

def minimum(vertices):
   minimum = float('inf')
   return min(vertices, key=lambda x: x.value)   

size = 40
network = list()
for row in range(size):
   for col in range(row):
      edge = data[row][col]
      if edge != '-': network.append(Edge(int(edge), [row, col]))

initial_sum = sum(edge.value for edge in network)


remaining_vertices = range(size)
remaining_edges = list()
for edge in network:
   remaining_edges.append(edge)
connected_edges = list()

def connect(edge):
   connected_edges.append(edge)
   remaining_edges.remove(edge)
   for vertex in edge.vertices:
      if vertex in remaining_vertices: remaining_vertices.remove(vertex)


connect(minimum(network))

def build_accessible_edges(connected_edges):
   accessible_edges = list()
   for connected_edge in connected_edges:
      for vertex in connected_edge.vertices:
	 for edge in remaining_edges:
	    if vertex in edge.vertices:
	       if any(v in remaining_vertices for v in edge.vertices):
		  accessible_edges.append(edge)
   return accessible_edges

while len(remaining_vertices) > 0:
   least_edge = minimum(build_accessible_edges(connected_edges))
   connect(least_edge)      

optimal_sum = sum(edge.value for edge in connected_edges)
saving = initial_sum - optimal_sum
print saving
