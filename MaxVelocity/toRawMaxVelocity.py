import numpy as np

names = ['184_01_filteredLinear','184_01_linearUpwind','184_01_QUICK','184_01_upwind','184_03_filteredLinear','184_03_linearUpwind','184_03_QUICK', 
'184_03_upwind','368_01_filteredLinear','368_01_linearUpwind','368_01_QUICK','368_01_upwind','368_03_filteredLinear','368_03_linearUpwind','368_03_QUICK','368_03_upwind']


for i in range(len(names)):
	file = open(names[i])
	f_5 = open(str(names[i] + '_min5.txt'), 'a')
	f_1 = open(str(names[i] + '_min1.txt'), 'a')
	f0 = open(str(names[i] + '_0.txt'), 'a')
	f3 = open(str(names[i] + '_3.txt'), 'a')
	for j in range(78):
		line = file.readline()
	
	u_matrix = []
	max_index = 0
	max_u = np.zeros(76)
	for line in file.readlines():
		string = line.replace('(', '')
		string = string.replace(')', '')
		time = float(string.split()[0])
		vals = string.split()[1:]
		vals = np.array(map(float, vals))
		u = []
		for k in range(0,len(vals),3):
			u.append(vals[k])
		u_matrix.append(u)
		if max(u) > max(max_u):
			max_u = u
			max_index = len(u_matrix) - 1

	for l in range(len(max_u)):
		f_5.write(str(u_matrix[max_index-50][l]) + '\n')
		f_1.write(str(u_matrix[max_index-10][l]) + '\n')
		f0.write(str(u_matrix[max_index][l]) + '\n')
		f3.write(str(u_matrix[max_index+30][l]) + '\n')
	file.close()
	f_5.close()
	f_1.close()
	f0.close()
	f3.close()

