#example

from load_data import download_graph
n_vertex, edge_list = download_graph('data\\football.txt')

from load_data import download_answer
lbl_true = download_answer('data\\football_ans.txt')

from model_builder import clustering
lbl0 = clustering('Spectral', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
lbl1 = clustering('SCAN', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
lbl2 = clustering('GreedyNewman', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
lbl3 = clustering('Walktrap', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
lbl4 = clustering('LPA', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
#lbl5 = clustering('unknown', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
#lbl6 = clustering('Spectral', edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
#lbl7 = clustering('Spectral', n_vertex, edge_list, eps = 1.5, mu=0.5, n_steps=3)
#lbl8 = clustering('SCAN', n_vertex, edge_list, n_clusters=5)
from transform_functions import compute_normal_labels
lbl0 = compute_normal_labels(lbl0)
lbl1 = compute_normal_labels(lbl1)
lbl2 = compute_normal_labels(lbl2)
lbl3 = compute_normal_labels(lbl3)
lbl4 = compute_normal_labels(lbl4)


#print lbl0
print lbl1
#print lbl2
#print lbl_true

from cluster_metrics import compute_my_modularity
#print compute_my_modularity(lbl0, edges)
print compute_my_modularity(lbl1, edge_list)
#print compute_my_modularity(lbl2, edges)

from cluster_metrics import compute_igraph_modularity
print compute_igraph_modularity(lbl1, edge_list)

from cluster_metrics import compute_avg_f1
#print compute_avg_f1(lbl_true, lbl0)
print compute_avg_f1(lbl_true, lbl1)
#print compute_avg_f1(lbl_true, lbl2)


