#algorithm wrapper to have the same interface for all the libraries

#TODO: remake using *parameters


def clustering(algorithm, n_vertex=None, edge_list=None, n_clusters=None, mu=0.3, eps=1.0):

  if algorithm == 'Spectral':
    return compute_spectral_clustering(n_vertex, edge_list, n_clusters)

  elif algorithm == 'SCAN':
    return compute_scan(n_vertex, edge_list, mu, eps)

  elif algorithm == 'GreedyNewman':
    return compute_greedy_newman(n_vertex, edge_list)


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

  from scan_by_enjoylife import scan_by_enjoylife_algo
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

