#example

from load_data import download_graph
n_vertex, edge_list = download_graph('data\\football.txt')

from load_data import download_labels
lbl_true = download_labels('data\\football_labels.txt')

from transform_functions import compute_clusters_from_labels
clrs_true = compute_clusters_from_labels(lbl_true)

from transform_functions import compute_amount_of_communities
#print compute_amount_of_communities(lbl_true)

from model_builder import clustering
lbl0, clrs0 = clustering('Spectral', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
lbl1, clrs1 = clustering('SCAN', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
lbl2, clrs2 = clustering('GreedyNewman', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
lbl3, clrs3 = clustering('Walktrap', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
lbl4, clrs4 = clustering('LPA', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
#lbl5, clrs5 = clustering('unknown', n_vertex, edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
#lbl6, clrs6 = clustering('Spectral', edge_list, eps = 1.5, mu=0.5, n_clusters=5, n_steps=3)
#lbl7, clrs7 = clustering('Spectral', n_vertex, edge_list, eps = 1.5, mu=0.5, n_steps=3)
#lbl8, clrs8 = clustering('SCAN', n_vertex, edge_list, n_clusters=5)
from transform_functions import compute_normal_labels
lbl0 = compute_normal_labels(lbl0)
lbl1 = compute_normal_labels(lbl1)
lbl2 = compute_normal_labels(lbl2)
lbl3 = compute_normal_labels(lbl3)
lbl4 = compute_normal_labels(lbl4)


print lbl0
print clrs0

from cluster_metrics import compute_my_modularity
print compute_my_modularity(lbl0, edge_list)

from cluster_metrics import compute_igraph_modularity
print compute_igraph_modularity(lbl0, edge_list)

from cluster_metrics import compute_avg_f1
print compute_avg_f1(clrs_true, clrs0)


