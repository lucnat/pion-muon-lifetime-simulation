
from pylab import *
import numpy as np
from sample import sample_from_lifetime_dist
from globals import t_mu, dt_mu, t_pi, dt_pi
from binned_ML import binned_ML

def sample_with_background(M):
	# returns 10k values plus M background values
	x = sample_from_lifetime_dist(1000)
	background = rand(M)*5*t_mu
	x = np.append(x,background)
	x = x[x<5*t_mu] 	# cut values above 5*t_mu away since exercise asks to fit only in interval (0, 5*t_mu)
	return x

# x = sample_with_background(1000)
# hist(x,100)
# show()

# repeat until we have one that converges
for M in [1000,2000,10000]:	
	print('M =',M,'background events')
	print('-----------------------------------------------------------------------------------')
	count = 0
	while True: 
		x = sample_with_background(M)
		optimizer_res = binned_ML(x, 100, np.array([np.random.normal(3.0e3,1e3), np.random.normal(2.6e1,1.0e1)]))
		count += 1
		print('does simulation',count,'converge? ')
		if(optimizer_res.success):
			estimates = optimizer_res.x
			print('yes!')
			print('means',estimates,'uncertainties',optimizer_res.sigma)
			break
		else:
			print('no.')