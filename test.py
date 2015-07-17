import community
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import spectral_clustering

print nx.__version__
#better with karate_graph() as defined in networkx example.
#erdos renyi don't have true community structure
#G = nx.erdos_renyi_graph(30, 0.05)
G = nx.karate_club_graph()

#first compute the best partition
partition = community.best_partition(G)

#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for community in set(partition.values()) :
  count = count + 1.
  list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == community]
  list_nodes
  
#  nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20, node_color=str(count / size))

#nx.draw_networkx_edges(G, pos, alpha=0.5)
#plt.show()


adjacency_matrix = nx.adjacency_matrix(G)
predicted_labels = spectral_clustering(adjacency_matrix, n_clusters=4, n_components=None,
                                       eigen_solver=None, random_state=None, n_init=10,
                                       eigen_tol=0.0, assign_labels='kmeans')


size = float(len(set(predicted_labels)))
pos = nx.spring_layout(G)
count = 0.
for community in set(predicted_labels) :
  count = count + 1.
  list_nodes = [node for node in xrange(len(predicted_labels)) if predicted_labels[node] == community]

  nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20, node_color=str(count / size))

nx.draw_networkx_edges(G, pos, alpha=0.5)

plt.show()
