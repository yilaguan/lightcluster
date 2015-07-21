from itertools import combinations

k=4
from load_data import download_graph
n_vertex, edge_list = download_graph('data\\polbooks.txt')

import igraph
from transform_functions import compute_igraph_form
g, weights = compute_igraph_form(n_vertex, edge_list);

clst = map(set, g.maximal_cliques(min=k))

edgelist = []
for i, j in combinations(range(len(clst)), 2):
    if len(clst[i].intersection(clst[j])) >= k-1:
        edgelist.append((i, j))

cg = igraph.Graph(edgelist, directed=False)
components = cg.clusters()

clusters = []
for component in components:
    cluster = set()
    for i in component:
        cluster.update(clst[i])
    clusters.append(cluster)

print clusters