
from pylab import *
import numpy as np
from sample import sample_from_lifetime_dist
from binned_ML import binned_ML

print('=========================================================')
print('Exercise 3b)')

while(True):
	x = sample_from_lifetime_dist(10000)
	res = binned_ML(x, 100, np.array([2.1e3, 2.6e1]))
	if(not res.success):
		print('did not converge, run again')
	else:
		mu = res.x
		sigma = res.sigma
		print('parameters =',mu, 'deviations =',sigma)
		break
