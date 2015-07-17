#example

from load_data import download_graph as dd
n, edges = dd('data\protein_new.txt')

from load_data import download_answer as da
lbl_true = da('data\protein_ans_new.txt')

from model_builder import clustering
lbl0 = clustering('Spectral', n, edges, 40)
lbl1 = clustering('GreedyNewman', n, edges)
lbl2 = clustering('SCAN', n, edges, mu = 0.3, eps = 1.0)

from transform_functions import compute_normal_labels
lbl2 = compute_normal_labels(lbl2)


print lbl0
print lbl1
print lbl2
#print lbl_true

from cluster_metrics import compute_modularity
print compute_modularity(lbl0, edges)
print compute_modularity(lbl1, edges)
print compute_modularity(lbl2, edges)

from cluster_metrics import compute_avg_f1
print compute_avg_f1(lbl_true, lbl0)
print compute_avg_f1(lbl_true, lbl1)
print compute_avg_f1(lbl_true, lbl2)


