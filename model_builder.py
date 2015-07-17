#algorithm wrapper to have the same interface for all the libraries

#TODO: remake using *parameters


def clustering(algorithm, n_vertex=None, edge_list=None, n_clusters=None, mu=0.3, eps=1.0, steps=4):

  if algorithm == 'Spectral':
    return compute_spectral_clustering(n_vertex, edge_list, n_clusters)

  elif algorithm == 'SCAN':
    return compute_scan(n_vertex, edge_list, mu, eps)

  elif algorithm == 'GreedyNewman':
    return compute_greedy_newman(n_vertex, edge_list)

  elif algorithm == 'Walktrap':
    return compute_walktrap(n_vertex, edge_list, n_clusters, steps)

  elif algorithm == 'LPA':
    return compute_lpa(n_vertex, edge_list)


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

def compute_walktrap(n_vertex, edge_list, n_clusters, steps):

  import igraph as ig
  from transform_functions import compute_igraph_form
  graph, weights = compute_igraph_form(n_vertex, edge_list);

  dendrogram = graph.community_walktrap(weights, steps)
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

