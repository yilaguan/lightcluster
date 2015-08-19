
"""
Load a dataset.
Available datasets are: 'football.txt', 'polbooks.txt', 'protein_new.txt', 'amazon.txt', 'scientists_new.txt', 
						'karate.txt', 'facebook.txt', 'cliques.txt', 'nested.txt', 'stars.txt', 'cycles.txt'
"""
dataset = 'football.txt'
from load_data import download_graph
n_vertex, edge_list = download_graph('data\\'+dataset)

"""
Choose an algorithm.
Available algorithms are: 'Spectral', 'SCAN', 'GreedyNewman', 'Walktrap', 'LPA', 'CFinder', 'Clauset-Newman', 'Bigclam'
"""
algorithm = 'Walktrap'


"""
Use 'independent_clustering' for computing communities --- labels and clusters (see reference for details).
Specify some parameters (n_clusters, neighbours_threshold, similarity_threshold, n_steps, clique_size).
Unspecified parameters will be chosen automatically or you'll get an error message.
"""
from model_builder import clustering, independent_clustering
lbls_pred, clrs_pred, time = independent_clustering(algorithm, n_vertex, edge_list, n_clusters=15, 
													neighbours_threshold=2, similarity_threshold=0.5, n_steps=3)

#write communities into the console if you wish
print lbls_pred
print clrs_pred
print time

from load_data import write_labels, write_clusters
#write communities (labels) into 'data\\answers\\'+'labels_'+algorithm+'_'+dataset
write_labels(algorithm, dataset, lbls_pred)

#write communities (clusters) into 'data\\answers\\'+'clusters_'+algorithm+'_'+dataset
write_labels(algorithm, dataset, clrs_pred)

"""
You can calculate goodness (non ground-truth) metrics, such as: modularity, overlapping modularity, ratio cut, normalized cut.
"""

from cluster_metrics import compute_modularity, compute_overlapping_modularity, compute_ratio_cut, compute_normalized_cut
print "Modularity = " + str(compute_modularity(lbls_pred, edge_list))
print "Overlapping modularity = " + str(compute_overlapping_modularity(clrs_pred, n_vertex, edge_list))
print "RatioCut = " + str(compute_ratio_cut(lbls_pred, clrs_pred, edge_list))
print "NormalizedCut = " + str(compute_normalized_cut(lbls_pred, clrs_pred, edge_list))


"""
If ground-truth communities are known, you can load them.
After that you can calculate performance (ground-truth) metrics, such as: average F1-score, average recall, average precision, 
																		  normalized mutual information (NMI), adjusted_rand_score (ARS)
"""
#if true labels are known
from load_data import download_labels, download_clusters
lbls_true = download_labels('data\\'+dataset[:-4]+'_labels.txt')
from transform_functions import compute_clusters_from_labels
clrs_true = compute_clusters_from_labels(lbls_true)

#if only true clusters are known
#clrs_true = download_clusters('data\\'+dataset[:-4]+'_clusters.txt')

from cluster_metrics import compute_avg_f1, compute_recall, compute_precision, compute_nmi, compute_ars
print "Average F1-score = " + str(compute_avg_f1(clrs_true, clrs_pred))
print "Average recall = " + str(compute_recall(clrs_true, clrs_pred))
print "Average precision = " + str(compute_precision(clrs_true, clrs_pred))
print "NMI = " + str(compute_nmi(lbls_true, lbls_pred))
print "ARS = " + str(compute_ars(lbls_true, lbls_pred))




