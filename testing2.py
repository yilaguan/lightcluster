f = open('data\\amazon.txt', "r")
f1 = open('data\\tmp_new.txt', "w")
s = f.readline()
n_vertex, n_edges = s.split(' ');
n_vertex = int(n_vertex)
n_edges = int(n_edges)
edge_list = []

index = 0
d = {}

for i in xrange(n_edges):
  s = f.readline()
  vertex1, vertex2 = s.split(' ')
  vertex1 = int(vertex1)
  vertex2 = int(vertex2)
  if vertex1 in d.keys():
    vertex1 = d[vertex1]
  else:
    index = index + 1
    d[vertex1] = index
    vertex1 = index

  if vertex2 in d.keys():
    vertex2 = d[vertex2]
  else:
    index = index + 1
    d[vertex2] = index
    vertex2 = index
  
  f1.write(str(vertex1)+' '+str(vertex2)+'\n')

print index
f.close()
f1.close()