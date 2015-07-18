# wrapper for easy downloading data


#TODO: weighted graph processing

def download_graph(filename):

  f = open(filename,"r")
  s = f.readline()
  n_vertex, n_edge = s.split(' ');
  n_vertex = int(n_vertex)
  n_edge = int(n_edge)
  edge_list = []

  for i in xrange(n_edge):
    s = f.readline()
    if s.count(' ') == 1:
      vertex1, vertex2 = s.split(' ');
      vertex1 = int(vertex1)-1
      vertex2 = int(vertex2)-1
      edge_list.append([vertex1, vertex2, 1]) 
    else:
      vertex1, vertex2, weight = s.split(' ',2);
      vertex1 = int(vertex1)-1
      vertex2 = int(vertex2)-1
      weight = int(weight)
      edge_list.append([vertex1, vertex2, weight])

  f.close()

  return [n_vertex, edge_list]


def download_answer(filename):

  f = open(filename,"r")
  labels_true = []
  s = f.readline()

  while s:
    labels_true.append(int(s));
    s = f.readline()

  f.close()

  return labels_true

