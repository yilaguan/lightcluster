#example

from load_data import download_data as dd
n, edges = dd('karate.txt')

from model_builder import clustering
lbl0 = clustering('Spectral', n, edges, 3)
lbl1 = clustering('GreedyNewman', n, edges)
lbl2 = clustering('SCAN', n, edges, mu = 1.0, eps = 2.0)

from transform_functions import compute_normal_labels
lbl2 = compute_normal_labels(lbl2)

print lbl0
print lbl1
print lbl2

from cluster_metrics import compute_modularity
print compute_modularity(lbl0, edges)
print compute_modularity(lbl1, edges)
print compute_modularity(lbl2, edges)


