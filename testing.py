from bench import make_experiment

al = ['Walktrap', 'LPA', 'Spectral', 'GreedyNewman', 'SCAN']
dt = ['football.txt', 'karate.txt', 'polbooks.txt']
result = make_experiment(al, dt, similarity_threshold=0.3, n_steps=2, neighbours_threshold=1.5)

for key in sorted(result):
	print key, result[key]