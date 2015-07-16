# wrapper for easy downloading data

def download_data(filename):
  f = open(filename,"r")
  s = f.readline()
  n_vertex, n_edge = s.split(' ',2);
  n_vertex = int(n_vertex)
  n_edge = int(n_edge)
  edgelist = [];
  for i in range(n_edge):
    s = f.readline()
    vertex1, vertex2 = s.split(' ',2);
    vertex1 = int(vertex1)-1
    vertex2 = int(vertex2)-1
    edgelist.append([vertex1, vertex2, 1])       
  return [n_vertex, edgelist]

def download_answer(filename):
  f = open(filename,"r")
  labels = [];
  s = f.readline()
  while s:
    labels.append(int(s));
    s = f.readline()
  return labels