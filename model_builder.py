#algorithm wrapper to have the same interface for all the libraries

#TODO: remake using *parameters


def clustering(algorithm, n_vertex, edge_list, n_clusters, neighbours_threshold, similarity_threshold, n_steps):

  if algorithm == 'Spectral':
    return compute_spectral_clustering(n_vertex, edge_list, n_clusters)
  elif algorithm == 'SCAN':
    return compute_scan(n_vertex, edge_list, neighbours_threshold, similarity_threshold)
  elif algorithm == 'GreedyNewman':
    return compute_greedy_newman(n_vertex, edge_list)
  elif algorithm == 'Walktrap':
    return compute_walktrap(n_vertex, edge_list, n_clusters, n_steps)
  elif algorithm == 'LPA':
    return compute_lpa(n_vertex, edge_list)


def independent_clustering(algorithm, n_vertex=None, edge_list=None, **kwargs): 


  if n_vertex == None or edge_list == None:
    raise TypeError("Arguments n_vertex and edge_list must be given!\n")

  recognized = ['n_clusters', 'neighbours_threshold', 'similarity_threshold', 'n_steps']

  n_clusters=None
  neighbours_threshold=None
  similarity_threshold=None
  n_steps=None

  for key, value in kwargs.items():
    if key not in recognized:
       raise TypeError(("Keyword argument '%s' is not recognized!\nAvailable keywords are:\n'"
                         + "', '".join(recognized)  + "'") % key)

    if key == recognized[0]:
      n_clusters = value
    elif key == recognized[1]:
      neighbours_threshold = value
    elif key == recognized[2]:
      similarity_threshold = value
    elif key == recognized[3]:
      n_steps = value


  if algorithm == 'Spectral':
    if n_clusters == None:
      raise TypeError("Argument n_clusters must be given for Srectral algorithm!\n")
    if neighbours_threshold != None:
      print "Argument neighbours_threshold is ignored for Spectral algorithm.\n"
    if similarity_threshold != None:
      print "Argument similarity_threshold is ignored for Spectral algorithm.\n"
    if n_steps != None:
      print "Argument n_steps is ignored for Spectral algorithm.\n"

    return compute_spectral_clustering(n_vertex, edge_list, n_clusters)

  elif algorithm == 'SCAN':
    if n_clusters != None:
      print "Argument n_clusters is ignored for SCAN algorithm.\n"
    if neighbours_threshold == None:
      print "Argument neighbours_threshold was not given for SCAN algorithm. Launching with default neighbours_threshold=0.7.\n"
      neighbours_threshold = 0.7
    if similarity_threshold == None:
      print "Argument similarity_threshold was not given for SCAN algorithm. Launching with default similarity_threshold=2.0.\n"
      similarity_threshold = 2.0
    if n_steps != None:
      print "Argument n_steps is ignored for SCAN algorithm.\n"
    return compute_scan(n_vertex, edge_list, neighbours_threshold, similarity_threshold)

  elif algorithm == 'GreedyNewman':
    if n_clusters != None:
      print "Argument n_clusters is ignored for GreedyNewman algorithm.\n"
    if neighbours_threshold != None:
      print "Argument neighbours_threshold is ignored for GreedyNewman algorithm.\n"
    if similarity_threshold != None:
      print "Argument similarity_threshold is ignored for GreedyNewman algorithm.\n"
    if n_steps != None:
      print "Argument n_steps is ignored for GreedyNewman algorithm.\n"

    return compute_greedy_newman(n_vertex, edge_list)

  elif algorithm == 'Walktrap':
    if n_clusters == None:
      print "Argument n_clusters will be choosen automatically for Walktrap algorithm.\n"
    if neighbours_threshold != None:
      print "Argument neighbours_threshold is ignored for Walktrap algorithm.\n"
    if similarity_threshold != None:
      print "Argument similarity_threshold is ignored for Walktrap algorithm.\n"
    if n_steps == None:
      print "Argument n_steps was not given for Walktrap algorithm. Launching with default n_steps=4.\n"
      n_steps = 4

    return compute_walktrap(n_vertex, edge_list, n_clusters, n_steps)

  elif algorithm == 'LPA':
    if n_clusters != None:
      print "Argument n_clusters is ignored for LPA algorithm!\n"
    if neighbours_threshold != None:
      print "Argument neighbours_threshold is ignored for LPA algorithm.\n"
    if similarity_threshold != None:
      print "Argument similarity_threshold is ignored for LPA algorithm.\n"
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

  from transform_functions import compute_clusters_from_labels
  clusters = compute_clusters_from_labels(labels)

  return [labels, clusters]


def compute_scan(n_vertex, edge_list, neighbours_threshold, similarity_threshold):

  from transform_functions import compute_csr_form
  rows, columns, weights = compute_csr_form(edge_list)

  from scipy.sparse import csr_matrix
  G = csr_matrix((weights,(rows,columns)),shape=(n_vertex,n_vertex))

  from lib.scan_by_enjoylife import scan_by_enjoylife_algo
  labels = scan_by_enjoylife_algo(G, neighbours_threshold, similarity_threshold)

  from transform_functions import compute_clusters_from_labels
  clusters = compute_clusters_from_labels(labels)

  return [labels, clusters]


def compute_greedy_newman(n_vertex, edge_list):

  import networkx as nx
  from transform_functions import compute_networkx_form
  graph = compute_networkx_form(n_vertex, edge_list)

  from agglomcluster import NewmanGreedy
  cls = NewmanGreedy(graph)
  clusters = cls.get_clusters()

  from transform_functions import compute_labels_from_clusters
  labels = compute_labels_from_clusters(n_vertex, clusters)

  return [labels, clusters]

def compute_walktrap(n_vertex, edge_list, n_clusters, n_steps):

  import igraph as ig
  from transform_functions import compute_igraph_form
  graph, weights = compute_igraph_form(n_vertex, edge_list)

  dendrogram = graph.community_walktrap(weights, n_steps)
  clusters = dendrogram.as_clustering(n=n_clusters)

  from transform_functions import compute_labels_from_clusters
  labels = compute_labels_from_clusters(n_vertex, clusters)

  return [labels, clusters]


def compute_lpa(n_vertex, edge_list):

  import igraph as ig
  from transform_functions import compute_igraph_form
  graph, weights = compute_igraph_form(n_vertex, edge_list);

  clusters = graph.community_label_propagation(weights=weights, initial=None, fixed=None)

  from transform_functions import compute_labels_from_clusters
  labels = compute_labels_from_clusters(n_vertex, clusters)

  return [labels, clusters]

