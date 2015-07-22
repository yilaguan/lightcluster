
from bench import make_experiment
algorithms = ['CFinder']
datasets = ['cycles.txt', 'nested.txt']
result = make_experiment(algorithms, datasets, similarity_threshold=0.7, n_steps=4, neighbours_threshold=2, n_clusters=4, clique_size=14)

from load_data import write_result
write_result(algorithms, datasets, result, 'result.xls')
for key in sorted(result):
	print key, result[key]
