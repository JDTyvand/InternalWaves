import matplotlib.pyplot as plt
import numpy as np

y = np.zeros(76)
file = open('rhok')
for i in range(76):
	line = file.readline()
	string = line.replace('(', '')
	string = string.replace(')', '')
	vals = string.split()
	y[i] = vals[4]
print y
file.readline()
file.readline()
j = 0
for line in file.readlines():
	string = line.replace('(', '')
	string = string.replace(')', '')
	time = float(string.split()[0])
	vals = string.split()[1:]
	vals = np.array(map(float, vals))
	if time > 100:
		plt.figure()
		plt.plot(vals, y)
		plt.title('Time = %s' % time)
		plt.xlabel('$rho$')
		plt.ylabel('$y$')
		plt.savefig('rho_%04d.png' % j)
	j += 1
file.close()

