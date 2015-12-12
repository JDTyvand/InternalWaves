import numpy as np

f = open('mesher184_01.txt', 'a')
lscale = np.linspace(5, 72.95, 13)
rscale = np.linspace(5, 72.95, 35)
print lscale
print rscale
lcount = 1
rcount = 1
for i in range(77):
	print ('Line %d' % (i+1))
	if i < 15:
		print('Uniform lower temperature 5')
		for j in range(184):
			f.write(str(5))
			f.write('\n')
	elif 14 < i < 26:
		print lscale[lcount]
		print('Left stratification, 5 right')
		for j in range(5):
			f.write(str(lscale[lcount]))
			f.write('\n')
		lcount += 1
		for j in range(179):
			f.write(str(5))
			f.write('\n')
	elif 25 < i < 43:
		print('Fresh water left, 5 right')
		for j in range(5):
			f.write(str(72.95))
			f.write('\n')
		for j in range(179):
			f.write(str(5))
			f.write('\n')
	else:
		print rcount
		print('Fresh water left, stratification right')
		print rscale[rcount]
		for j in range(5):
			f.write(str(72.95))
			f.write('\n')
		for j in range(179):
			f.write(str(rscale[rcount]))
			f.write('\n')
		rcount += 1

f.close()
