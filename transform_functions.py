# here should go functions which transform one graph or answer representation into another


#computing adjacency matrix from amount of vertixes and list of edges
def compute_adjacency_matrix(n_vertex, edgelist):

  import numpy as np
  adjacency_matrix = np.zeros((n_vertex, n_vertex))
   
  for i in xrange(len(edgelist)):
    vertex1 = edgelist[i][0]
    vertex2 = edgelist[i][1]
    weight = edgelist[i][2]
    adjacency_matrix[vertex1, vertex2] = weight
    adjacency_matrix[vertex2, vertex1] = weight
       
  return adjacency_matrix


#computing compressed sparse row form from list of edges
def compute_csr_form(edge_list):
  
  rows = [];
  columns = [];
  weights = [];
  
  for i in xrange(len(edge_list)):
  	rows.append(edge_list[i][0])
  	columns.append(edge_list[i][1])
  	rows.append(edge_list[i][1])
  	columns.append(edge_list[i][0])
  	weights.append(edge_list[i][2])
  	weights.append(edge_list[i][2])
  
  return [rows, columns, weights]


def compute_networkx_form(n_vertex, edge_list):

  import networkx as nx
  graph = nx.Graph()
  graph.add_nodes_from(xrange(n_vertex))
  graph.add_weighted_edges_from(edge_list)

  return graph

def compute_igraph_form(n_vertex, edge_list):

  import igraph as ig
  g = ig.Graph()
  g.add_vertices(n_vertex)



#transforming original list of labels into list of labels with 0,1,2,...
def compute_normal_labels(labels):
  #new list
  normal_labels = []

  #dictionary for old and new labels
  biection = {}

  iid = 0;
  
  for i in xrange(len(labels)):
  
    if labels[i] in biection.keys():
      normal_labels.append(biection[labels[i]])
    else:
      biection[labels[i]] = iid
      normal_labels.append(biection[labels[i]])
      iid = iid + 1
  
  return normal_labels

#extracts biggest fully connected component of graph written in filename. creates new file with this component.
#if data with ground-truth, creates new file with answer for this component
#TODO??? automatically call download data from filename_new? or insert into download_data?
def extract_biggest_component(filename):

  from load_data import download_graph as dd
  n_vertex, edge_list = dd(filename)

  import networkx as nx
  from transform_functions import compute_networkx_form
  graph = compute_networkx_form(n_vertex, edge_list)
  components = list(nx.connected_component_subgraphs(graph))

  if len(components) > 1:
    components.sort(key = len, reverse = True)

    newgraph = components[0]
    n_vertex_new = len(newgraph.nodes())

    biection = {}
    for i in xrange(n_vertex_new):
      biection[newgraph.nodes()[i]] = i+1

    f = open(filename[:-4]+'_new.txt', "w")
    f.write(str(n_vertex_new)+' '+str(len(newgraph.edges()))+'\n')

    for i in xrange(len(edge_list)):
      if edge_list[i][0] in newgraph.nodes():
        if len(edge_list[0]) == 2:
          f.write(str(biection[edge_list[i][0]])+' '+str(biection[edge_list[i][1]])+'\n')
        else:
          f.write(str(biection[edge_list[i][0]])+' '+str(biection[edge_list[i][1]])+' '+str(edge_list[i][2])+'\n')

    f.close()

    import os
    if os.path.isfile(filename[:-4]+'_ans.txt'):
      f = open(filename[:-4]+'_ans.txt', "r")
      f1 = open(filename[:-4]+'_ans_new.txt', "w")

      for i in xrange(n_vertex):
        s = f.readline()
        if i in newgraph.nodes():
          f1.write(s)

      f.close()
      f1.close()

