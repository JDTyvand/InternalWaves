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
names = ['184_01_linearUpwind.txt','184_01_linearUpwind_convection.txt','184_01_QUICK.txt','184_01_QUICK_convection.txt','184_01_SFCD.txt','184_01_SFCD_convection.txt','184_03_linearUpwind.txt','184_03_linearUpwind_convection.txt','184_03_QUICK.txt', 
'184_03_QUICK_convection.txt','184_03_SFCD.txt','184_03_SFCD_convection.txt']

y = np.linspace(-0.61,0.14,76)

for fname in (names):
	data = np.loadtxt(fname)
	plt.plot(data/c,y/h2)
plt.legend([names[i].replace('.txt','') for i in range(len(names))], loc = 'lower right')
plt.title('Time = 92s')
plt.xlim(-0.6,1.2)
plt.savefig('time_0.png')

