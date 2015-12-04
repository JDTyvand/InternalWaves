import numpy as np

f = open('mesher.txt', 'a')
lscale = np.linspace(5, 72.95, 13)
rscale = np.linspace(5, 72.95, 25)
print len(rscale)
print rscale
lcount = 1
rcount = 1
for i in range(77):
	print i
	if i < 23:
		print('first loop', i)
		for j in range(184):
			f.write(str(5))
			f.write('\n')
	elif 21 < i < 34:
		print('second loop', i)
		for j in range(5):
			f.write(str(lscale[lcount]))
			f.write('\n')
		lcount += 1
		for j in range(179):
			f.write(str(5))
			f.write('\n')
	elif 33 < i < 54:
		print('third loop', i)
		for j in range(5):
			f.write(str(72.95))
			f.write('\n')
		for j in range(179):
			f.write(str(5))
			f.write('\n')
	else:
		print('fourth loop', i)
		print rscale[rcount]
		for j in range(5):
			f.write(str(72.95))
			f.write('\n')
		for j in range(179):
			f.write(str(rscale[rcount]))
			f.write('\n')
		rcount += 1

f.close()
