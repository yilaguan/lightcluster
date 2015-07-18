#here should go metrics implementation or their wrapper

#def compute_metric(metric = 'Modularity', ):
#TODO

def compute_nmi(labels_true, labels_pred):
  
  from sklearn.metrics import normalized_mutual_info_score
  
  return normalized_mutual_info_score(labels_true, labels_pred)


def compute_ars(labels_true, labels_pred):
  
  from sklearn.metrics import adjusted_rand_score
  
  return adjusted_rand_score(labels_true, labels_pred)


def match_straight(y1, y2):

  g = {}

  for i in set(y1):
    A = set(ii for ii in xrange(len(y1)) if y1[ii] == i)
    f1_max = -1000

    for j in set(y2):
      B = set(jj for jj in xrange(len(y2)) if y2[jj] == j)

      if (len(A & B) != 0):
        precision = 1.0 * len(A & B) / len(B)
        recall = 1.0 * len(A & B) / len(A)
        f1 = 2.0 * precision * recall / (precision + recall)

        if (f1 > f1_max):
          f1_max = f1
          g[i] = j
  
  return g


def match_reverse(y1, y2):

  g_ = {}

  for i in set(y2):
    A = set(ii for ii in xrange(len(y2)) if y2[ii] == i)
    f1_max = -1000

    for j in set(y1):
      B = set(jj for jj in xrange(len(y1)) if y1[jj] == j)

      if (len(A & B) != 0):
        precision = 1.0 * len(A & B) / len(A)
        recall = 1.0 * len(A & B) / len(B)
        f1 = 2.0 * precision * recall / (precision + recall)

        if (f1 > f1_max):
          f1_max = f1
          g_[i] = j
  
  return g_


def compute_recall(labels_true, labels_pred):

  res = 0.0
  g = match_straight(labels_true, labels_pred)

  for i in set(labels_true):
    A = set(ii for ii in xrange(len(labels_true)) if labels_true[ii] == i)       #C_i from C^*
    B = set(ii for ii in xrange(len(labels_pred)) if labels_pred[ii] == g(i))    #C^^_g(i) from C^^
    res = res + 1.0 * len(A & B) / len(A)
  
  recall = res / len(set(labels_true))
  return recall     


def compute_avg_f1(labels_true, labels_pred):
    
  res1 = 0.0
  res2 = 0.0
  g = match_straight(labels_true, labels_pred)
  g_ = match_reverse(labels_true, labels_pred)

  for i in set(labels_true):
    A = set(ii for ii in xrange(len(labels_true)) if labels_true[ii] == i)       #C_i from C^*
    B = set(ii for ii in xrange(len(labels_pred)) if labels_pred[ii] == g[i])    #C^^_g(i) from C^^
    precision = 1.0 * len(A & B) / len(B)
    recall = 1.0 * len(A & B) / len(A)
    f1 = 2.0 * precision * recall / (precision + recall)
    res1 = res1 + f1

  for i in set(labels_pred):
    A = set(ii for ii in xrange(len(labels_true)) if labels_true[ii] == g_[i])    #C^^_i from C^
    B = set(ii for ii in xrange(len(labels_pred)) if labels_pred[ii] == i)        #C^*_g_(i) from C^*
    precision = 1.0 * len(A & B) / len(B)
    recall = 1.0 * len(A & B) / len(A)
    f1 = 2.0 * precision * recall / (precision + recall)
    res2 = res2 + f1
  
  avg_f1 = 1 / 2.0 * (res1 / len(set(labels_true)) + res2 / len(set(labels_pred)))
  return avg_f1


def compute_my_modularity(labels_pred, edge_list):

  n_edges = len(edge_list)
  m = 0.0   #finally m = sum w_ij
  E = 0.0   #finally E/2m = sum e_ii
  A = [0.0] * len(set(labels_pred))
  res = 0.0

  for i in xrange(n_edges):
    m = m + edge_list[i][2];

    if (labels_pred[edge_list[i][0]] == labels_pred[edge_list[i][1]]):
      E = E + edge_list[i][2]        #finally E/2m = sum e_ii
    else:
      A[labels_pred[edge_list[i][0]]] = A[labels_pred[edge_list[i][1]]] + edge_list[i][2]
      A[labels_pred[edge_list[i][1]]] = A[labels_pred[edge_list[i][0]]] + edge_list[i][2]

  for i in set(labels_pred):
    res = res + A[i]*A[i]
    
  Q = E/(2.0*m) - res/(4.0*m*m)        #modularity
  
  return Q


def compute_igraph_modularity(labels_pred, edge_list):

	n_vertex = len(labels_pred)
	import igraph as ig
	from transform_functions import compute_igraph_form
	graph, weights = compute_igraph_form(n_vertex, edge_list);

	return graph.modularity(labels_pred, weights=weights)

