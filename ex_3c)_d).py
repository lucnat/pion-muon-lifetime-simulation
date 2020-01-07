
from pylab import *
import numpy as np
from sample import sample_from_lifetime_dist
from binned_ML import binned_ML

# Do simulation N times
N = 100

mu_estimates = []
pi_estimates = []

count = 0

print('=========================================================')
print('Exercise 3c and d)')

while True:
	x = sample_from_lifetime_dist(10000)
	res = binned_ML(x, 100, np.array([2.1e3, 2.6e1]))
	# add only if converged
	if(res.success):
		mu_estimates.append(res.x[0])
		pi_estimates.append(res.x[1])
		count += 1
		print(count,'successful simulations')
	if(count == N):
		break


print('t_mu estimate', np.mean(mu_estimates), '+-', np.std(mu_estimates))
print('t_pi estimate', np.mean(pi_estimates), '+-', np.std(pi_estimates))

mu_pulls = (np.array(mu_estimates) - 2191.9) / 22.1
pi_pulls = (np.array(pi_estimates) - 26.1) / 5.9

print('pull_mu estimate', np.mean(mu_pulls), '+-', np.std(mu_pulls))
print('pull_pi estimate', np.mean(pi_pulls), '+-', np.std(pi_pulls))

# plot distributions
subplot(2,2,1)
hist(mu_estimates,10)
title('histogram of $τ_\mu$ estimates')
subplot(2,2,2)
title('histogram of $τ_\pi$ estimates')
hist(pi_estimates,10)

# plot pulls
subplot(2,2,3)
hist(mu_pulls)
title('pull distribution of $τ_\mu$ ')
subplot(2,2,4)
hist(pi_pulls)
title('pull distribution of $τ_\pi$')
show()

