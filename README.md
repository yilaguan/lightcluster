# lightcluster
Clustering lib (Python) by PreMoLab

1. Install all necessary libraries:

- 'igraph' (igraph.org) in 'lib'
   pip python_igraph-0.7.1.post6-cp27-none-win_amd64.whl install
- 'networkx' (networkx.github.io)
- 'scikit-learn' (scikit-learn.org)
- 'agglomcluster' (pypi.python.org/pypi/AgglomCluster/1.0.2) in 'lib'
   python setup.py install
- 'scan_by_enjoylife' will work automatically

2. Use 'testing(multiple).py' or 'testing(single).py'.
   Follow the instructions given there.

3. Available algorithms:

 - 'Spectral' from sklearn, 
	described in 'articles\spectral_clustering'.    	Parameters: 'n_clusters'.
 - 'SCAN' by enjoylife, 
	described in 'articles\scan'.
	Parameters: 'neighbours_threshold', 							 'similarity_threshold'.
 - 'GreedyNewman' from networkx, 
	described in 'articles\newman_greedy'.
	Parameters: no.
 - 'Walktrap' from igraph, 
	described in 'articles\walktrap'.
	Parameters: 'n_steps' --- length of random walks.
 - 'LPA' from igraph, 
	described in 'articles\lpa'.
	Parameters: no.
 - 'CFinder' from 	stackoverflow.com/questions/20063927/overlapping-	community-detection-with-igraph-or-other-libaries,
	described in 'articles\CFinder'.
	Parameters: 'clique_size' --- size of cliques
 - 'ClausetNewman' from igraph,
	described in 'articles\clauset-newman-moore'
	Parameters: no
 - 'Bigclam' from snap.stanford.edu,
	described in \articles\bigclam'
	Parameters: 'n_clusters'

4. Available datasets:
	'football.txt', 'polbooks.txt', 'protein_new.txt', 	'scientists_new.txt', 'karate.txt', 'facebook.txt', 	'cliques.txt', 'nested.txt', 'stars.txt', 'cycles.txt'.

5. Available metrics:
	modularity, overlapping modularity, ratio cut, normalized 	cut, average F1-score, average recall, average precision,  	normalized mutual information (NMI), adjusted_rand_score 	(ARS)
