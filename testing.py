
from bench import make_optimal_experiment, make_experiment
algorithms = ['Clauset-Newman']
datasets = ['protein_new.txt']
result = make_experiment(algorithms, datasets)

#for key in sorted(result):
#	print key, result[key]

from load_data import write_result
write_result(algorithms, datasets, result, 'result.xls')

