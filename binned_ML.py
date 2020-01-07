
# Example of a binned ML

from pylab import *
import numpy as np
import scipy
from scipy import optimize

def binned_ML(x,amount_bins,start_value):
	# performs binned ML on data x with amount_bins bins
	# returns result of optimizer

	h = histogram(x,amount_bins)			# compute histogram
	width = (max(x)-min(x))/amount_bins 	# bin width

	n_i = np.array(h[0])
	x_i = np.array(h[1])
	x_i = x_i[:-1] + width/2 # compute bin centers from edges

	# pdf = lambda t, t_mu, t_pi: 1/(t_mu - t_pi) * (exp(-t/t_mu) - exp(-t/t_pi) )
	cdf = lambda t, t_mu, t_pi: 1 + 1/(t_mu - t_pi) * ( -t_mu*exp(-t/t_mu) + t_pi*exp(-t/t_pi) )
	f_i = lambda t, t_mu, t_pi:  cdf(t+width/2, t_mu, t_pi) - cdf(t-width/2, t_mu, t_pi)
	
	def NNL(params):
		t_mu, t_pi = params
		res = -sum(n_i*log(f_i(x_i,t_mu,t_pi)) - f_i(x_i,t_mu,t_pi))
		return res

	res = scipy.optimize.minimize(NNL,start_value)
	
	if(res.success):
		# estimate error on params
		mean_mu, mean_pi = res.x
		f_mu = lambda sigma: NNL([mean_mu + sigma,mean_pi]) - NNL([mean_mu,mean_pi]) - 0.5
		f_pi = lambda sigma: NNL([mean_mu, mean_pi + sigma]) - NNL([mean_mu,mean_pi]) - 0.5
		sigma_mu = scipy.optimize.root(f_mu,20.0).x
		sigma_pi = scipy.optimize.root(f_pi,5.0).x
		res.sigma = [sigma_mu,sigma_pi]

	return res
