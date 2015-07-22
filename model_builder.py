#algorithm wrapper to have the same interface for all the libraries

import time
import transform_functions as tf
import igraph as ig
import networkx as nx

from scipy.sparse import csr_matrix
from lib.scan_by_enjoylife import scan_by_enjoylife_algo
from itertools import combinations

def clustering(algorithm, n_vertex, edge_list, n_clusters, neighbours_threshold, similarity_threshold, n_steps, clique_size):

  if algorithm == 'Spectral':
    labels, clusters, exectime = compute_spectral_clustering(n_vertex, edge_list, n_clusters)
  elif algorithm == 'SCAN':
    labels, clusters, exectime = compute_scan(n_vertex, edge_list, neighbours_threshold, similarity_threshold)
  elif algorithm == 'GreedyNewman':
    labels, clusters, exectime = compute_greedy_newman(n_vertex, edge_list)
  elif algorithm == 'Walktrap':
    labels, clusters, exectime = compute_walktrap(n_vertex, edge_list, n_clusters, n_steps)
  elif algorithm == 'LPA':
    labels, clusters, exectime = compute_lpa(n_vertex, edge_list)
  elif algorithm == 'CFinder':
    labels, clusters, exectime = compute_cfinder(n_vertex, edge_list, clique_size)
  elif algorithm == 'Clauset-Newman':
    labels, clusters, exectime = compute_clauset_newman(n_vertex, edge_list, n_clusters)

  return labels, clusters, exectime

def independent_clustering(algorithm, n_vertex=None, edge_list=None, **kwargs): 
  if n_vertex == None or edge_list == None:
    raise TypeError("Arguments n_vertex and edge_list must be given!\n")

  recognized = ['n_clusters', 'neighbours_threshold', 'similarity_threshold', 'n_steps', 'clique_size']

  n_clusters=None
  neighbours_threshold=None
  similarity_threshold=None
  n_steps=None
  clique_size=None

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
    elif key == recognized[4]:
      clique_size = value

  if algorithm == 'Spectral':
    if n_clusters == None:
      raise TypeError("Argument n_clusters must be given for Srectral algorithm!\n")
    if neighbours_threshold != None:
      print "Argument neighbours_threshold is ignored for Spectral algorithm.\n"
    if similarity_threshold != None:
      print "Argument similarity_threshold is ignored for Spectral algorithm.\n"
    if n_steps != None:
      print "Argument n_steps is ignored for Spectral algorithm.\n"
    if clique_size != None:
      print "Argument clique_size is ignored for Spectral algorithm.\n"

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
    if clique_size != None:
      print "Argument clique_size is ignored for SCAN algorithm.\n"

    labels, clusters, exectime = compute_scan(n_vertex, edge_list, neighbours_threshold, similarity_threshold)

  elif algorithm == 'GreedyNewman':
    if n_clusters != None:
      print "Argument n_clusters is ignored for GreedyNewman algorithm.\n"
    if neighbours_threshold != None:
      print "Argument neighbours_threshold is ignored for GreedyNewman algorithm.\n"
    if similarity_threshold != None:
      print "Argument similarity_threshold is ignored for GreedyNewman algorithm.\n"
    if n_steps != None:
      print "Argument n_steps is ignored for GreedyNewman algorithm.\n"
    if clique_size != None:
      print "Argument clique_size is ignored for GreedyNewman algorithm.\n"

    labels, clusters, exectime = compute_greedy_newman(n_vertex, edge_list)

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
    if clique_size != None:
      print "Argument clique_size is ignored for Walktrap algorithm.\n"

    labels, clusters, exectime = compute_walktrap(n_vertex, edge_list, n_clusters, n_steps)

  elif algorithm == 'LPA':
    if n_clusters != None:
      print "Argument n_clusters is ignored for LPA algorithm!\n"
    if neighbours_threshold != None:
      print "Argument neighbours_threshold is ignored for LPA algorithm.\n"
    if similarity_threshold != None:
      print "Argument similarity_threshold is ignored for LPA algorithm.\n"
    if n_steps != None:
      print "Argument n_steps is ignored for LPA algorithm.\n"
    if clique_size != None:
      print "Argument clique_size is ignored for LPA algorithm.\n"

    labels, clusters, exectime = compute_lpa(n_vertex, edge_list)

  elif algorithm == 'CFinder':
    if n_clusters != None:
      print "Argument n_clusters is ignored for CFinder algorithm!\n"
    if neighbours_threshold != None:
      print "Argument neighbours_threshold is ignored for CFinder algorithm.\n"
    if similarity_threshold != None:
      print "Argument similarity_threshold is ignored for CFinder algorithm.\n"
    if n_steps != None:
      print "Argument n_steps is ignored for CFinder algorithm.\n"
    if clique_size == None:
      print "Argument clique_size was not given for CFinder algorithm. Launchibg with default clique_size=3.\n"
      clique_size = 3

    labels, clusters, exectime = compute_cfinder(n_vertex, edge_list, clique_size)

  elif algorithm == 'Clauset-Newman':
    if n_clusters == None:
      print "Argument n_clusters will be choosen automatically for Clauset-Newman algorithm.\n"
    if neighbours_threshold != None:
      print "Argument neighbours_threshold is ignored for Clauset-Newman algorithm.\n"
    if similarity_threshold != None:
      print "Argument similarity_threshold is ignored for Clauset-Newman algorithm.\n"
    if n_steps == None:
      print "Argument n_steps is ignored for Clauset-Newman algorithm.\n"
    if clique_size != None:
      print "Argument clique_size is ignored for Clauset-Newman algorithm.\n"

    labels, clusters, exectime = compute_clauset_newman(n_vertex, edge_list, n_clusters)

  else:
    raise TypeError(("Algorithm '%s' is not recognized!\nAvailable algorithms are: Spectral, SCAN, GreedyNewman, Walktrap, LPA, CFinder, Clauset-Newman\n") % algorithm)

  return labels, clusters, exectime

def compute_spectral_clustering(n_vertex, edge_list, n_clusters):
  from sklearn.cluster import SpectralClustering
  clst = SpectralClustering(n_clusters, affinity = 'precomputed')

  adjacency_matrix = tf.compute_adjacency_matrix(n_vertex, edge_list)
  
  t = time.time()
  labels = clst.fit_predict(adjacency_matrix, n_clusters)
  exectime = time.time() - t

  labels = tf.compute_normal_labels(labels)

  clusters = tf.compute_clusters_from_labels(labels)

  return labels, clusters, exectime

def compute_scan(n_vertex, edge_list, neighbours_threshold, similarity_threshold):
  rows, columns, weights = tf.compute_csr_form(edge_list)

  G = csr_matrix((weights,(rows,columns)),shape=(n_vertex,n_vertex))
  
  t = time.time()
  labels = scan_by_enjoylife_algo(G, neighbours_threshold, similarity_threshold)
  exectime = time.time() - t

  labels = tf.compute_normal_labels(labels)

  clusters = tf.compute_clusters_from_labels(labels)

  return labels, clusters, exectime

def compute_greedy_newman(n_vertex, edge_list):
  from agglomcluster import NewmanGreedy
  graph = tf.compute_networkx_form(n_vertex, edge_list)
  
  t = time.time()
  clst = NewmanGreedy(graph)
  clusters = clst.get_clusters()
  exectime = time.time() - t

  labels = tf.compute_labels_from_clusters(n_vertex, clusters)

  return labels, clusters, exectime

def compute_walktrap(n_vertex, edge_list, n_clusters, n_steps):
  graph, weights = tf.compute_igraph_form(n_vertex, edge_list)
  
  t = time.time()
  dendrogram = graph.community_walktrap(weights, n_steps)
  clusters = dendrogram.as_clustering(n=n_clusters)
  exectime = time.time() - t

  labels = tf.compute_labels_from_clusters(n_vertex, clusters)

  return labels, clusters, exectime

def compute_lpa(n_vertex, edge_list):
  graph, weights = tf.compute_igraph_form(n_vertex, edge_list)

  t = time.time()
  clusters = graph.community_label_propagation(weights=weights, initial=None, fixed=None)
  exectime = time.time() - t

  labels = tf.compute_labels_from_clusters(n_vertex, clusters)

  return labels, clusters, exectime

def compute_cfinder(n_vertex, edge_list, clique_size):
  g, weights = tf.compute_igraph_form(n_vertex, edge_list);

  t = time.time()
  clst = map(set, g.maximal_cliques(min=clique_size))
  edgelist = []
  for i, j in combinations(range(len(clst)), 2):
    if len(clst[i].intersection(clst[j])) >= clique_size-1:
      edgelist.append((i, j))
  cg = ig.Graph()
  cg.add_vertices(len(clst))
  cg.add_edges(edgelist)

  components = cg.clusters()

  clusters = []
  for component in components:
    cluster = set()
    for i in component:
      cluster.update(clst[i])
    clusters.append(cluster)
  exectime = time.time() - t

  labels = None

  return labels, clusters, exectime

def compute_clauset_newman(n_vertex, edge_list, n_clusters):
  graph, weights = tf.compute_igraph_form(n_vertex, edge_list)
  
  t = time.time()
  dendrogram = graph.community_fastgreedy(weights)
  clusters = dendrogram.as_clustering(n=n_clusters)
  exectime = time.time() - t

  labels = tf.compute_labels_from_clusters(n_vertex, clusters)

  return labels, clusters, exectime
