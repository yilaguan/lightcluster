#algorithm wrapper to have the same interface for all the libraries

#TODO: remake using *parameters


def clustering(algorithm, n_vertex=None, edge_list=None, **kwargs): #  n_clusters=None, mu=0.3, eps=1.0, steps=4):


  if n_vertex == None or edge_list == None:
    raise TypeError("Arguments n_vertex and edge_list must be given!\n")

  recognized = ['n_clusters', 'mu', 'eps', 'n_steps']

  n_clusters=None
  mu=None
  eps=None
  n_steps=None

  for key, value in kwargs.items():
    if key not in recognized:
       raise TypeError(("Keyword argument '%s' is not recognized!\nAvailable keywords are:\n'"
                         + "', '".join(recognized)  + "'") % key)

    if key == recognized[0]:
      n_clusters = value
    elif key == recognized[1]:
      mu = value
    elif key == recognized[2]:
      eps = value
    elif key == recognized[3]:
      n_steps = value


  if algorithm == 'Spectral':
    if n_clusters == None:
      raise TypeError("Argument n_clusters must be given for Srectral algorithm!\n")
    if mu != None:
      print "Argument mu is ignored for Spectral algorithm.\n"
    if eps != None:
      print "Argument eps is ignored for Spectral algorithm.\n"
    if n_steps != None:
      print "Argument n_steps is ignored for Spectral algorithm.\n"

    return compute_spectral_clustering(n_vertex, edge_list, n_clusters)

  elif algorithm == 'SCAN':
    if n_clusters != None:
      print "Argument n_clusters is ignored for SCAN algorithm.\n"
    if mu == None:
      print "Argument mu was not given for SCAN algorithm. Launching with default mu=0.7.\n"
      mu = 0.7
    if eps == None:
      print "Argument eps was not given for SCAN algorithm. Launching with default eps=2.0.\n"
    if n_steps != None:
      print "Argument n_steps is ignored for SCAN algorithm.\n"
    return compute_scan(n_vertex, edge_list, mu, eps)

  elif algorithm == 'GreedyNewman':
    if n_clusters != None:
      print "Argument n_clusters is ignored for GreedyNewman algorithm.\n"
    if mu != None:
      print "Argument mu is ignored for GreedyNewman algorithm.\n"
    if eps != None:
      print "Argument eps is ignored for GreedyNewman algorithm.\n"
    if n_steps != None:
      print "Argument n_steps is ignored for GreedyNewman algorithm.\n"

    return compute_greedy_newman(n_vertex, edge_list)

  elif algorithm == 'Walktrap':
    if n_clusters != None:
      print "Argument n_clusters is ignored for Walktrap algorithm.\n"
    if mu != None:
      print "Argument mu is ignored for Walktrap algorithm.\n"
    if eps != None:
      print "Argument eps is ignored for Walktrap algorithm.\n"
    if n_steps == None:
      print "Argument n_steps was not given for Walktrap algorithm. Launching with default n_steps=4.\n"
      n_steps = 4

    return compute_walktrap(n_vertex, edge_list, n_clusters, n_steps)

  elif algorithm == 'LPA':
    if n_clusters == None:
      print "Argument n_clusters is ignored for LPA algorithm!\n"
    if mu != None:
      print "Argument mu is ignored for LPA algorithm.\n"
    if eps != None:
      print "Argument eps is ignored for LPA algorithm.\n"
    if n_steps != None:
      print "Argument n_steps is ignored for LPA algorithm.\n"

    return compute_lpa(n_vertex, edge_list)

  else:
    raise TypeError(("Algorithm '%s' is not recognized!\nAvailable algorithms are: Spectral, SCAN, GreedyNewman, Walktrap, LPA\n") % algorithm)



def compute_spectral_clustering(n_vertex, edge_list, n_clusters):

  from sklearn.cluster import SpectralClustering
  cls = SpectralClustering(n_clusters, affinity = 'precomputed')

  from transform_functions import compute_adjacency_matrix
  adjacency_matrix = compute_adjacency_matrix(n_vertex, edge_list)
  labels = cls.fit_predict(adjacency_matrix, n_clusters)

  return labels


def compute_scan(n_vertex, edge_list, mu, eps):

  from transform_functions import compute_csr_form
  rows, columns, weights = compute_csr_form(edge_list)

  from scipy.sparse import csr_matrix
  G = csr_matrix((weights,(rows,columns)),shape=(n_vertex,n_vertex))

  from lib.scan_by_enjoylife import scan_by_enjoylife_algo
  labels = scan_by_enjoylife_algo(G, mu, eps)

  return labels


def compute_greedy_newman(n_vertex, edge_list):

  import networkx as nx
  from transform_functions import compute_networkx_form
  graph = compute_networkx_form(n_vertex, edge_list)

  from agglomcluster import NewmanGreedy
  cls = NewmanGreedy(graph)
  tmp_list = cls.get_clusters()

  labels = [0]*n_vertex
  for index in xrange(len(tmp_list)):
    for j in tmp_list[index]:
      labels[j] = index

  return labels

def compute_walktrap(n_vertex, edge_list, n_clusters, n_steps):

  import igraph as ig
  from transform_functions import compute_igraph_form
  graph, weights = compute_igraph_form(n_vertex, edge_list);

  dendrogram = graph.community_walktrap(weights, n_steps)
  clusters = dendrogram.as_clustering(n=n_clusters)

  from transform_functions import compute_labels_from_sets
  labels = compute_labels_from_sets(n_vertex, clusters)

  return labels


def compute_lpa(n_vertex, edge_list):

  import igraph as ig
  from transform_functions import compute_igraph_form
  graph, weights = compute_igraph_form(n_vertex, edge_list);

  clusters = graph.community_label_propagation(weights=weights, initial=None, fixed=None)

  from transform_functions import compute_labels_from_sets
  labels = compute_labels_from_sets(n_vertex, clusters)

  return labels

