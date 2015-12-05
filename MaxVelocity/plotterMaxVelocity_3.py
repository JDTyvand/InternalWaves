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
names = ['184_03_default_3.txt','184_03_linearUpwind_3.txt','184_03_linearUpwind_convection_3.txt','184_03_QUICK_3.txt', \
	 '184_03_QUICK_convection_3.txt','184_03_SFCD_3.txt','184_03_SFCD_convection_3.txt']
y = np.linspace(-0.61,0.14,76)

for fname in (names):
	data = np.loadtxt(fname)
	plt.plot(data/c,y/h2)
	plt.legend([names[i].replace('_3.txt','') for i in range(len(names))], loc = 'lower right')
plt.title('Time = 3s')
plt.xlim(-0.5, 1)
plt.savefig('time_3.png')

