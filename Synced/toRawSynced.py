import numpy as np

names = ['184_01_linearUpwind','184_01_linearUpwind_convection','184_01_QUICK','184_01_QUICK_convection','184_01_SFCD','184_01_SFCD_convection','184_03_linearUpwind','184_03_linearUpwind_convection','184_03_QUICK', 
'184_03_QUICK_convection','184_03_SFCD','184_03_SFCD_convection']

for i in range(len(names)):
	file = open(names[i])
	f = open(str(names[i] + '.txt'), 'a')
	for j in range(78):
		line = file.readline()

	for line in file.readlines():
		string = line.replace('(', '')
		string = string.replace(')', '')
		time = float(string.split()[0])
		vals = string.split()[1:]
		vals = np.array(map(float, vals))
		u = []
		for k in range(0,len(vals),3):
			u.append(vals[k])
		if time == 92:
			for l in range(len(u)):
				f.write(str(u[l]) + '\n')
		
	file.close()
	f.close()

