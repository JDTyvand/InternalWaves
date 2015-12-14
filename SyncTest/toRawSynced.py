import numpy as np

names = ['default','nonZeroViscosity','variableTime']

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
		if time == 89.1:
			for l in range(len(u)):
				f.write(str(u[l]) + '\n')
		
	file.close()
	f.close()
