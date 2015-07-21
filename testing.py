
from bench import make_experiment
algorithms = ['CFinder']
datasets = ['nested.txt']
result = make_experiment(algorithms, datasets, similarity_threshold=0.7, n_steps=4, neighbours_threshold=2, n_clusters=6, clique_size=13)

from load_data import write_result
write_result(algorithms, datasets, result, 'result.xls')
for key in sorted(result):
	print key, result[key]
