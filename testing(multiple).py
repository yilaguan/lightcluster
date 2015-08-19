from functions.bench import make_optimal_experiment, make_experiment

"""
Specify the algorithms that you want to launch.
Available algorithms are: 'Spectral', 'SCAN', 'GreedyNewman', 'Walktrap', 'LPA', 'CFinder', 'Clauset-Newman', 'Bigclam'.
"""
#example: algorithms = ['Clauset-Newman', 'LPA', 'Bigclam']

algorithms = ['Clauset-Newman', 'LPA', 'Bigclam']

"""
Specify the datasets that you want to use.
Available datasets are: 'football.txt', 'polbooks.txt', 'protein_new.txt', 'amazon.txt', 'scientists_new.txt', 
						'karate.txt', 'facebook.txt', 'cliques.txt', 'nested.txt', 'stars.txt', 'cycles.txt'.
"""
#example: datasets = ['protein_new.txt', 'karate.txt', 'stars.txt']

datasets = ['karate.txt', 'stars.txt', 'football.txt']


"""
if you want to test the algorithms on the datasets with optimal (chosen by us) parameters, use 'make_optimal_experiment'
"""
#result = make_optimal_experiment(algorithms, datasets)

"""
if you want to test algorithms on datasets with your own parameters, use 'make_experiment'
Available parameters are: 'n_clusters', 'neighbours_threshold', 'similarity_threshold', 'n_steps', 'clique_size'
If you don't specify some parametr, the default value will be chosen or you'll get an error message.
"""
#example: result = make_experiment(algorithms, datasets, n_clusters=5, clique_size=4)

result = make_experiment(algorithms, datasets, n_clusters=5, clique_size=4)


"""Print results in console, if you wish"""
#for key in sorted(result):
#	print key, result[key]

"""Print results in file 'result.xls' """
from functions.load_data import write_result
write_result(algorithms, datasets, result, 'result.xls')

