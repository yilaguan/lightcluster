#algorithm wrapper to have the same interface for all the libraries

def get_clusters(adjacency_matrix, algorithm='spectral', parameters=None):

  if algorithm == 'spectral':
    clustering = get_clusters_spectral(adjacency_matrix, parameters=None)

  return clustering


def get_clusters_spectral(adjacency_matrix, parameters=None):
  from sklearn.cluster import spectral_clustering

  #parameter conversion goes here

  for parameter in parameters.keys():
    if parameter == 'n_clusters':
      n_clusters = parameters[parameter]
    elif parameter == 'n_components':
      n_clusters = parameters[parameter]
    else:
      print "Warning. Parameter " + parameter + "unknown for algorithm spectral_clustering!"

  clustering = spectral_clustering(adjacency_matrix, n_clusters=4, n_components=None,
                                         eigen_solver=None, random_state=None, n_init=10,
                                         eigen_tol=0.0, assign_labels='kmeans')

  return clustering