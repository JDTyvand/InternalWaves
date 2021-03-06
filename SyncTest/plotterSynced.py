import numpy as np
import matplotlib.pyplot as plt
params = {'legend.fontsize': 8,
          'legend.linewidth': 2}
plt.rcParams.update(params)

g = 9.81
h1 = 0.62
h2 = 0.15
rho0 = 1000.
rho1 = 976.1
N0 = np.sqrt(((rho0-rho1)/rho0)*(g/h2))
c_0 = (N0*h2)/1.711 
c = c_0*1.6
print c_0
print c
names = ['default.txt','nonZeroViscosity.txt','variableTime.txt']

styles = ['b-','r-','g-','y-','b--','r--','g--','y--','bx','rx','gx','yx','b+','r+','g+','y+']
y = np.linspace(-0.61,0.14,76)

count = 0
for fname in (names):
	data = np.loadtxt(fname)
	plt.plot(data/c,y/h2, styles[count], markersize=3)
	count += 1
plt.legend([names[i].replace('.txt','') for i in range(len(names))], loc = 'lower right')
plt.title('Time = 89.1s')
plt.xlim(-0.6,1.2)
plt.xlabel('u/c')
plt.ylabel('y/h2')
plt.savefig('time_0.png')

