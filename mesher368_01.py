import numpy as np

f = open('mesher368_1.txt', 'a')
lscale = np.linspace(5, 72.95, 22)
rscale = np.linspace(5, 72.95, 65)
print lscale
print rscale
lcount = 1
rcount = 1
for i in range(144):
	print ('Line %d' % (i+1))
	if i < 28:
		print('Uniform lower temperature 5')
		for j in range(368):
			f.write(str(5))
			f.write('\n')
	elif 27 < i < 48:
		print lscale[lcount]
		print('Left stratification, 5 right')
		for j in range(10):
			f.write(str(lscale[lcount]))
			f.write('\n')
		lcount += 1
		for j in range(358):
			f.write(str(5))
			f.write('\n')
	elif 47 < i < 80:
		print('Fresh water left, 5 right')
		for j in range(10):
			f.write(str(72.95))
			f.write('\n')
		for j in range(358):
			f.write(str(5))
			f.write('\n')
	else:
		print rcount
		print('Fresh water left, stratification right')
		print rscale[rcount]
		for j in range(10):
			f.write(str(72.95))
			f.write('\n')
		for j in range(358):
			f.write(str(rscale[rcount]))
			f.write('\n')
		rcount += 1

f.close()
