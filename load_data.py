# wrapper for easy downloading data

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


def write_result(all_algorithms, all_datasets, result, filename):
  import pandas as pd
  all_measures = ['My modularity', 'Modularity', 'RatioCut', 'NormCut', 'NMI', 'ARS', 'Recall', 'Precision', 'Average F1', 'Time']

  writer = pd.ExcelWriter(filename)
  row = 1
  for dataset in all_datasets:
    res_dict = {}

    for measure in all_measures:
      pred_dict = {}

      for algorithm in all_algorithms:
        if (algorithm, dataset, measure) in result.keys():
          pred_dict[algorithm] = result[algorithm, dataset, measure]
      res_dict[measure] = pred_dict

    final_dict = {}
    for measure in all_measures:
      final_dict[measure] = res_dict[measure]
    
    df = pd.DataFrame(final_dict)
    df.to_excel(writer, startrow=row, float_format = '%11.3f')
    writer.save()
    row = row + 7



