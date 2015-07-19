#example

from load_data import download_graph
n_vertex, edge_list = download_graph('data\\protein_new.txt')

from load_data import download_labels
lbls_true = download_labels('data\\protein_new_labels.txt')

from transform_functions import compute_clusters_from_labels
clrs_true = compute_clusters_from_labels(lbls_true)

from transform_functions import compute_amount_of_communities_from_labels
#print compute_amount_of_communities_from_labels(lbls_true)

from model_builder import clustering
lbls0, clrs0 = clustering('Spectral', n_vertex, edge_list, similarity_threshold = 1.5, neighbours_threshold=0.5, n_clusters=5, n_steps=3)
lbls1, clrs1 = clustering('SCAN', n_vertex, edge_list, similarity_threshold = 1.5, neighbours_threshold=0.5, n_clusters=5, n_steps=3)
lbls2, clrs2 = clustering('GreedyNewman', n_vertex, edge_list, similarity_threshold = 1.5, neighbours_threshold=0.5, n_clusters=5, n_steps=3)
lbls3, clrs3 = clustering('Walktrap', n_vertex, edge_list, similarity_threshold = 1.5, neighbours_threshold=0.5, n_steps=3)
lbls4, clrs4 = clustering('LPA', n_vertex, edge_list, similarity_threshold = 1.5, neighbours_threshold=0.5, n_clusters=5, n_steps=3)
#lbls5, clrs5 = clustering('unknown', n_vertex, edge_list, similarity_threshold = 1.5, neighbours_threshold=0.5, n_clusters=5, n_steps=3)
#lbls6, clrs6 = clustering('Spectral', edge_list, similarity_threshold = 1.5, neighbours_threshold=0.5, n_clusters=5, n_steps=3)
#lbls7, clrs7 = clustering('Spectral', n_vertex, edge_list, similarity_threshold = 1.5, neighbours_threshold=0.5, n_steps=3)
#lbls8, clrs8 = clustering('SCAN', n_vertex, edge_list, n_clusters=5)
from transform_functions import compute_normal_labels
lbls0 = compute_normal_labels(lbls0)
lbls1 = compute_normal_labels(lbls1)
lbls2 = compute_normal_labels(lbls2)
lbls3 = compute_normal_labels(lbls3)
lbls4 = compute_normal_labels(lbls4)


print lbls0
print clrs0

from cluster_metrics import compute_my_modularity
print compute_my_modularity(lbls0, edge_list)

from cluster_metrics import compute_igraph_modularity
print compute_igraph_modularity(lbls0, edge_list)

from cluster_metrics import compute_avg_f1
print compute_avg_f1(clrs_true, clrs0)


