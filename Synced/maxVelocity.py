import matplotlib.pyplot as plt
import numpy as np

names = ['184_01_filteredLinear','184_01_linearUpwind','184_01_QUICK','184_01_upwind','184_03_filteredLinear','184_03_linearUpwind','184_03_QUICK', 
'184_03_upwind','368_01_filteredLinear','368_01_linearUpwind','368_01_QUICK','368_01_upwind','368_03_filteredLinear','368_03_linearUpwind','368_03_QUICK','368_03_upwind']

max_vals = []
max_times = []
for i in range(len(names)):
	file = open(names[i])
	for j in range(78):
		file.readline()
	max_u = 0
	max_time = 0
	for line in file.readlines():
		string = line.replace('(', '')
		string = string.replace(')', '')
		time = float(string.split()[0])
		vals = string.split()[1:]
		vals = np.array(map(float, vals))
		if vals.max() > max_u:
			max_u = vals.max()
			max_time = time
	max_vals.append(max_u)
	max_times.append(max_time)
	file.close()
print max_vals
print np.mean(max_times)

