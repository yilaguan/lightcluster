def write_result(all_algorithms, all_datasets, result, filename):
	import pandas as pd
	all_measures = ['My modularity', 'Igraph modularity', 'NMI', 'ARS', 'Recall', 'Average F1']

	writer = pd.ExcelWriter(filename)
	column = 0
	for dataset in all_datasets:
		res_dict = {}

		for measure in all_measures:
			pred_dict = {}

			for algorithm in all_algorithms:
				if (algorithm, dataset, measure) in result.keys():
					pred_dict[algorithm] = result[algorithm, dataset, measure]
			res_dict[measure] = pred_dict

		final_dict = {}
		for measure in all_measures:
			final_dict[measure] = res_dict[measure]
		
		df = pd.DataFrame(final_dict)
		df.to_excel(writer, startcol=column, startrow=1, float_format = '%1.2f')
		writer.save()
		column = column + 8

from bench import make_experiment
from transform_functions import extract_biggest_component
#extract_biggest_component('data\\scientists.txt')
algorithms = ['Walktrap', 'LPA', 'Spectral', 'GreedyNewman', 'SCAN']
datasets = ['polbooks.txt', 'protein_new.txt', 'football.txt', 'karate.txt']
result = make_experiment(algorithms, datasets, similarity_threshold=0.7, n_steps=12, neighbours_threshold=2, n_clusters=12)
write_result(algorithms, datasets, result, 'result.xls')

#for key in sorted(result):
#	print key, result[key]



