# lightcluster
Clustering lib by PreMoLab

1. Install all necessary libraries:

- 'igraph' (igraph.org) in 'lib'
   pip python_igraph-0.7.1.post6-cp27-none-win_amd64.whl install
- 'networkx' (networkx.github.io)
- 'scikit-learn' (scikit-learn.org)
- 'agglomcluster' (pypi.python.org/pypi/AgglomCluster/1.0.2) in 'lib'
   python setup.py install
- 'scan_by_enjoylife' will work automatically

2. Common names of variables:

- 'n_vertex' --- amount of vertex
- 'n_edges' --- amount of edges
- 'n_clusters' --- amount of clusters
- 'edge_list' --- list of edges, always weighted (if graph is unweighted, then weight = 1), e.g. [[0, 1, 0.5], [0, 2, 1], [1, 3, 100], ...]
- 'lbls' --- list of labels with length of 'n_vertex', i-th vertex belongs to cluster lbl[i], e.g. [0, 0, 0, 1, 1, 1, 0, 2, 0, 2, ...]; 'lbls_true' for ground-truth 
 (only for non-ovrlapping communities)
- 'clrs' --- list of clusters, i-th element of list contains vertices that belongs to i-th cluster, e.g. [(0,1,2,3), (0,2,4), (4), ...]; 'clrs_true' for ground-truth
 (for overlapping communities as well as for non_overlapping)

 3. Available algorithms:

 - 'Spectral' from sklearn, described in 'articles\spectral_clustering'.    Parameters: 'n_clusters'.
 - 'SCAN' by enjoylife, described in 'articles\scan'.     Parameters: 'neighbours_threshold', 'similarity_threshold'.
 - 'GreedyNewman' from networkx, described in 'articles\newman_greedy'.     Parameters: no.
 - 'Walktrap' from igraph, described in 'articles\walktrap'.     Parameters: 'n_steps' --- length of random walks.
 - 'LPA' from igraph, described in 'articles\lpa'.     Parameters: no.

4. Functions:
---------------------------------------------------------------------------------------------------
	*load_data.py

	  - download_graph
	    Parameter: 'filename'
	      in this file graph should be described in following  format:
	      "n_vertex n_edges
	       vertex11 vertex12 weight1
	       vertex21 vertex22 weight2
	       vertex31 vertex32 weight3
	       ..."
	       or
	      "n_vertex n_edges
	       vertex11 vertex12
	       vertex21 vertex22
	       vertex31 vertex32
	       ..."
	    Returns:  pair of 'n_vertex', 'edge_list'

	  - download_labels
	    Parameter: 'filename'
	      in this file labels should be described in following  format:
	      "0
	       0
	       1
	       1
	       0
	       2
	       ..."
	      i-th row corresponds to label of i-th vertex
	    Returns:  'labels'

	  - download_clusters
	    Parameter:  'filename'
	      in this file clusters should be described in following  format:
	      "0 1 2 3
	       0 2 4
	       4
	       ..."
	      i-th row corresponds to i-th cluster and contains vertices of this cluster
	    Return:  'clusters'
---------------------------------------------------------------------------------------------------
    *model_builder.py

      - clustering
        Necessary parameters: 
          algorithm: 'Spectral', 'SCAN', 'GreedyNewman', 'Walktrap', 'LPA'
          'n_vertex'
          'edge_list'
        Additional parameters:
          'n_clusters'
          'neighbours_threshold'
          'similarity_threshold'
          'n_steps'
        Returns:
          pair of 'labels' and 'clusters'

      - compute_spectral_clustering
        Necessary parameters: 
          'n_vertex'
          'edge_list'
          'n_clusters'
        Returns:
          pair of 'labels' and 'clusters'
       
      - compute_scan
        Necessary parameters: 
          'n_vertex'
          'edge_list'
          'neighbours_threshold'
          'similarity_threshold'
        Returns:
          pair of 'labels' and 'clusters'

      - compute_greedy_newman
        Necessary parameters: 
          'n_vertex'
          'edge_list'
        Returns:
          pair of 'labels' and 'clusters'

      - compute_walktrap
        Necessary parameters: 
          'n_vertex'
          'edge_list'
        Additional parameters (if not given - choosen automatically):
          'n_clusters'
        Returns:
          pair of 'labels' and 'clusters'

      - compute_lpa
        Necessary parameters: 
          'n_vertex'
          'edge_list'
        Returns:
          pair of 'labels' and 'clusters'
---------------------------------------------------------------------------------------------------
    *transform_functions.py

      - compute_adjacency_matrix
        Parameters: 'n_vertex', 'edge_list'
        Returns: 'adjacency_matrix'

      - compute_csr_form
        Parameters: 'edge_list'
        Returns: 'rows', 'columns', 'weights' for using scipy.sparse library

      - compute_networkx_form
        Parameters: 'n_vertex', 'edge_list'
        Returns: networkx.graph() for using networkx algorithms

      - compute_igraph_form
        Parameters: 'n_vertex', 'edge_list'
        Returns: igraph.Graph() and list of edge weights for using igraph algorithms

      - compute_normal_labels
        Parameters: 'labels'
        Returns: 'normal_labels'
        Example: labels = [1.5, 0, 1.5, 1, 1, 1.5] -> normal_labels = [0, 1, 0, 2, 2, 0]

      - compute_labels_from_clusters
        Parameters: 'n_vertex', 'clusters'
        Returns: 'labels'
        Example: n_vertex = 6, clusters = [[0, 2, 3], [1, 5], [4]] -> labels = [0, 1, 0, 0, 2, 1]
        (Possible only for non-overlapping clusters)

      - compute_clusters_from_labels
      	Parameters: 'labels'
      	Returns: 'clusters'
      	Example: labels = [0, 1, 0, 0, 2, 1] -> clusters = [[0, 2, 3], [1, 5], [4]]

      - compute_amount_of_communities_from_labels
        Parameters: 'labels'
        Return: 'n_clusters'

      - compute_amount_of_communities_from_clusters
        Parameters: 'clusters'
        Return: 'n_clusters'

      - extract_biggest_component
      	Parameters: 'filename'
      	Returns: nothing
      	Description: Checks if graph described in 'filename' is fully connected. If not, extracts biggest connected component and write it in 'fileame_new'.
      	             Besides, if file with answer exists, extracts corresponding labels and write it in 'filename_new_labels' or 'filename_new_clusters'

---------------------------------------------------------------------------------------------------
	*cluter_metrics.py