
from pylab import *
import numpy as np
from globals import t_mu, dt_mu, t_pi, dt_pi

pdf = lambda t: 1/(t_mu - t_pi) * (exp(-t/t_mu) - exp(-t/t_pi) )	
f = lambda t: 1/(t_mu - t_pi) * (exp(-t/t_mu))	# comparison function

def sample_from_lifetime_dist(N):
	# samples N values from above pdf using the improved rejection method
	samples = []
	while True:
		x = np.random.exponential(t_mu)	
		y = rand()*f(x)
		if(y < pdf(x)):
			samples.append(x)
		if(len(samples) == N):
			return samples

