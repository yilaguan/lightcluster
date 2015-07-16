# here should go functions which transform one graph or answer representation into another

#TODO maybe transforming into networkx representation (watch 'model_builder.py', def greedy_newman) should go here

#computing adjacency matrix from amount of vertixes and list of edges
def compute_adjacency_matrix(n_vertex, edgelist):

  import numpy as np
  adjacency_matrix = np.zeros((n_vertex, n_vertex))
   
  for i in range(len(edgelist)):
    vertex1 = edgelist[i][0]
    vertex2 = edgelist[i][1]
    weight = edgelist[i][2]
    adjacency_matrix[vertex1,vertex2] = weight
    adjacency_matrix[vertex2,vertex1] = weight
       
  return adjacency_matrix


#computing compressed sparse row form from list of edges
def compute_csr_form(edge_list):
  
  rows = [];
  columns = [];
  weights = [];
  
  for i in range(len(edge_list)):
  	rows.append(edge_list[i][0])
  	columns.append(edge_list[i][1])
  	rows.append(edge_list[i][1])
  	columns.append(edge_list[i][0])
  	weights.append(edge_list[i][2])
  	weights.append(edge_list[i][2])
  
  return [rows, columns, weights]


#transforming original list of labels into list of labels with 0,1,2,...
def compute_normal_labels(labels):
  #new list
  normal_labels = []

  #dictionary for old and new labels
  biection = {}

  id = 0;
  
  for i in range(len(labels)):
  
    if labels[i] in biection.keys():
      normal_labels.append(biection[labels[i]])
    else:
      biection[labels[i]] = id
      normal_labels.append(biection[labels[i]])
      id = id + 1
  
  return normal_labels
