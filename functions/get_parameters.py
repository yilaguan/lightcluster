
def get_optimal_parameters(dataset, recompute=False):

	parameters = {}
	if recompute == True:
		optimal_n_clusters = get_optimal_n_clusters(dataset)
		optimal_neighbours_threshold, optimal_similarity_threshold = get_optimal_thresholds(dataset)
		optimal_n_steps = get_optimal_n_steps(dataset)
		optimal_clique_size = get_optimal_clique_size(dataset)
	else:
		if dataset == 'amazon.txt':
			optimal_n_clusters = 0                         #???????There are just clusters
			optimal_neighbours_threshold = 0
			optimal_similarity_threshold = 0
			optimal_n_steps = 0
			optimal_clique_size = 0
		elif dataset == 'cliques.txt':
			optimal_n_clusters = 2                         #
			optimal_neighbours_threshold = 2               #
			optimal_similarity_threshold = 0.5             #
			optimal_n_steps = 2                            #
			optimal_clique_size = 27                       #
		elif dataset == 'cycles.txt':
			optimal_n_clusters = 4                         #
			optimal_neighbours_threshold = 2               #
			optimal_similarity_threshold = 0.6             #
			optimal_n_steps = 5                            #
			optimal_clique_size = 3                        #
		elif dataset == 'facebook.txt':
			optimal_n_clusters = 12                        #
			optimal_neighbours_threshold = 0
			optimal_similarity_threshold = 0
			optimal_n_steps = 25                           #
			optimal_clique_size = None                     #
		elif dataset == 'football.txt':
			optimal_n_clusters = 12                        #
			optimal_neighbours_threshold = 2               #
			optimal_similarity_threshold = 0.4             #
			optimal_n_steps = 2                            #
			optimal_clique_size = 4                        #
		elif dataset == 'karate.txt':
			optimal_n_clusters = 2                         #
			optimal_neighbours_threshold = 2               #
			optimal_similarity_threshold = 0.5             #
			optimal_n_steps = 9                            #
			optimal_clique_size = 3                        #
		elif dataset == 'nested.txt':
			optimal_n_clusters = 6                         #or 2?????
			optimal_neighbours_threshold = 5               #
			optimal_similarity_threshold = 0.8             #
			optimal_n_steps = 2                            #
			optimal_clique_size = 4                        #
		elif dataset == 'polbooks.txt':
			optimal_n_clusters = 3                         #
			optimal_neighbours_threshold = 2               #
			optimal_similarity_threshold = 0.4             #
			optimal_n_steps = 11                           #
			optimal_clique_size = 3                        #
		elif dataset == 'protein_new.txt':
			optimal_n_clusters = 13                        #
			optimal_neighbours_threshold = 1               #
			optimal_similarity_threshold = 0.5             #
			optimal_n_steps = 11                           #
			optimal_clique_size = 3                        #
		elif dataset == 'scientists_new.txt':
			optimal_n_clusters = 325                       #
			optimal_neighbours_threshold = 0
			optimal_similarity_threshold = 0
			optimal_n_steps = 20                           #
			optimal_clique_size = None                     #
		elif dataset == 'stars.txt':
			optimal_n_clusters = 5                         #
			optimal_neighbours_threshold = 1               #
			optimal_similarity_threshold = 0.4             #
			optimal_n_steps = 2                            #
			optimal_clique_size = 3                        #

	parameters['n_clusters'] = optimal_n_clusters
	parameters['neighbours_threshold'] = optimal_neighbours_threshold
	parameters['similarity_threshold'] = optimal_similarity_threshold
	parameters['n_steps'] = optimal_n_steps
	parameters['clique_size'] = optimal_clique_size
	return parameters


from bench import make_experiment
from load_data import write_choice

all_measures = ['Modularity', 'RatioCut', 'NormCut', 'NMI', 'ARS', 'Recall', 'Precision', 'Average F1', 'Time']

def get_optimal_n_clusters(dataset):
	algorothms = ['Bigclam']
	datasets = [dataset]
	table = {}
	variants = []
	if dataset == 'amazon.txt':
		optimal_n_clusters = 0 #?????
	elif dataset == 'cliques.txt':
		optimal_n_clusters = 2
	elif dataset == 'cycles.txt':
		optimal_n_clusters = 4
	elif dataset == 'facebook.txt':
		variants = []
	elif dataset == 'football.txt':
		optimal_n_clusters = 12
	elif dataset == 'karate.txt':
		optimal_n_clusters = 2
	elif dataset == 'nested.txt':
		optimal_n_clusters = 6
	elif dataset == 'polbooks.txt':
		optimal_n_clusters = 3
	elif dataset == 'protein_new.txt':
		optimal_n_clusters = 13
	elif dataset == 'scientists_new.txt':
		variants = [250, 275, 300, 325, 350]
	elif dataset == 'stars.txt':
		optimal_n_clusters = 5

	for i in variants:
		result = make_experiment(algorothms, datasets, n_clusters=i)
		print result
		table[i, 'My modularity'] = result['Bigclam', dataset, 'My modularity']
		table[i, 'Time'] = result['Bigclam', dataset, 'Time']
	write_choice(table, variants, dataset, 'n_clusters')

all_measures = ['My modularity', 'RatioCut', 'NormCut', 'Recall', 'Precision', 'Average F1', 'Time']

def get_optimal_n_steps(dataset):
	algorothms = ['Walktrap']
	datasets = [dataset]
	table = {}
	variants = [45, 55]
	
	for i in variants:
		result = make_experiment(algorothms, datasets, n_steps=i)
		for measure in all_measures:
			table[i, measure] = result['Walktrap', dataset, measure]
	write_choice(table, variants, dataset, 'n_steps')

def get_optimal_n_clique_size(dataset):
	algorothms = ['CFinder']
	datasets = [dataset]
	table = {}
	variants = [3]
	
	for i in variants:
		result = make_experiment(algorothms, datasets, clique_size=i)
		for measure in all_measures:
			if ('CFinder', dataset, measure) in result.keys():
			  table[i, measure] = result['CFinder', dataset, measure]
	write_choice(table, variants, dataset, 'clique_size')

def get_optimal_thresholds(dataset):
	algorothms = ['SCAN']
	datasets = [dataset]
	table = {}
	#variants = [[1, 0.3], [1, 0.4], [1, 0.5], [1, 0.6], [1, 0.7], [1, 0.8], [2, 0.3], [2, 0.4], [2, 0.5], [2, 0.6], [2, 0.7], [2, 0.8], 
	# [3, 0.3], [3, 0.4], [3, 0.5], [3, 0.6], [3, 0.7], [3, 0.8]]
	#str_variants = ['1, 0.3', '1, 0.4','1, 0.5', '1, 0.6', '1, 0.7', '1, 0.8', '2, 0.3', '2, 0.4','2, 0.5', '2, 0.6', '2, 0.7', '2, 0.8',
  	#						'3, 0.3', '3, 0.4','3, 0.5', '3, 0.6', '3, 0.7', '3, 0.8']

	variants = [[2, 0.5]]
	str_variants = ['2, 0.5']
	for i in xrange(len(variants)):
		result = make_experiment(algorothms, datasets, neighbours_threshold=variants[i][0], similarity_threshold=variants[i][1])
		for measure in all_measures:
			table[str_variants[i], measure] = result['SCAN', dataset, measure]

	write_choice(table, str_variants, dataset, 'thresholds')

#######################################################################################################################################

"""
for dataset in ['scientists_new.txt']:
	get_optimal_n_clusters(dataset)
"""

"""
for dataset in ['facebook.txt', 'football.txt', 'polbooks.txt', 'protein_new.txt', 'scientists_new.txt', 'karate.txt', 
								'cliques.txt', 'nested.txt', 'stars.txt', 'cycles.txt']:
	get_optimal_n_steps(dataset)
"""

"""
for dataset in ['facebook.txt', 'football.txt', 'polbooks.txt', 'protein_new.txt', 'scientists_new.txt', 'karate.txt', 
								'cliques.txt', 'nested.txt', 'stars.txt', 'cycles.txt']:
	get_optimal_n_clique_size(dataset)
"""

"""
for dataset in ['facebook.txt', 'scientists_new.txt']:
	get_optimal_thresholds(dataset)
"""


