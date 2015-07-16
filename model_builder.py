#algorithm wrapper to have the same interface for all the libraries

#TODO: remake using *parameters


def clustering(algorithm, n_vertex = None, edge_list=None, n_clusters=None, mu = 0.3, eps = 1.0):

  if algorithm == 'Spectral':
    return spectral_clustering(n_vertex, edge_list, n_clusters)

  elif algorithm == 'SCAN':
    return scan(n_vertex, edge_list, mu, eps)

  elif algorithm == 'GreedyNewman':
    return greedy_newman(n_vertex, edge_list)


def spectral_clustering(n_vertex, edge_list, n_clusters):

  from sklearn.cluster import SpectralClustering
  cls = SpectralClustering(n_clusters, affinity = 'precomputed')

  from transform_functions import compute_adjacency_matrix
  labels = cls.fit_predict(compute_adjacency_matrix(n_vertex, edge_list), n_clusters)

  return labels


def scan(n_vertex, edge_list, mu, eps):

  from transform_functions import compute_csr_form
  rows, columns, weights = compute_csr_form(edge_list)

  from scipy.sparse import csr_matrix
  G = csr_matrix((weights,(rows,columns)),shape=(n_vertex,n_vertex))

  from scan_by_enjoylife import scan_by_enjoylife_algo
  labels = scan_by_enjoylife_algo(G, mu, eps)

  return labels


def greedy_newman(n_vertex, edge_list):

  import networkx as nx
  G = nx.Graph()
  G.add_nodes_from(range(n_vertex))
  G.add_weighted_edges_from(edge_list)

  from agglomcluster import NewmanGreedy
  cls = NewmanGreedy(G)
  tmp_list = cls.get_clusters()

  labels = [0]*n_vertex
  for id in range(len(tmp_list)):
    for j in tmp_list[id]:
      labels[j] = id;

  return labels