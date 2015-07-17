from load_data import download_graph as dd
n, edges = dd('data\karate.txt')

from transform_functions import compute_igraph_form
g, weights = compute_igraph_form(n, edges)

print g.edges()