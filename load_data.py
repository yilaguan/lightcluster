# wrapper for easy downloading data


#TODO: weighted graph processing

def download_graph(filename):

  f = open(filename, "r")
  s = f.readline()
  n_vertex, n_edges = s.split(' ');
  n_vertex = int(n_vertex)
  n_edges = int(n_edges)
  edge_list = []

  for i in xrange(n_edges):
    s = f.readline()
    if s.count(' ') == 1:
      vertex1, vertex2 = s.split(' ');
      vertex1 = int(vertex1) - 1
      vertex2 = int(vertex2) - 1
      edge_list.append([vertex1, vertex2, 1]) 
    else:
      vertex1, vertex2, weight = s.split(' ', 2);
      vertex1 = int(vertex1) - 1
      vertex2 = int(vertex2) - 1
      weight = float(weight)
      edge_list.append([vertex1, vertex2, weight])

  f.close()

  return [n_vertex, edge_list]


def download_labels(filename):

  f = open(filename, "r")
  labels_true = []
  s = f.readline()

  while s:
    labels_true.append(int(s));
    s = f.readline()

  f.close()

  return labels_true


def download_clusters(filename):

  f = open(filename, "r")
  clusters = []

  s = f.readline()

  while s:
    cnt = s.count(' ')
    cluster_str = ()    #set of strings
    cluster = ()        #set of numbers
    cluster_str = s.split(' ', cnt)
    for string in cluster_str:       #transform  strings into numbers
      vertex = int(string) - 1
      cluster = cluster + (vertex,)

    clusters.append(cluster)
    s = f.readline()

  f.close()

  return clusters
