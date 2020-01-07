
from pylab import *
import numpy as np
from globals import t_mu, dt_mu, t_pi, dt_pi
from sample import sample_from_lifetime_dist, pdf

t_max = 5*t_mu
samples = sample_from_lifetime_dist(10000)
print(len(samples))
subplot(2,1,1)
hist(samples,300)
xlim([0,t_max])
title('sampled decay times')
grid()
x = linspace(0,t_max,1000)
subplot(2,1,2)
plot(x,pdf(x))
xlim([0,t_max])
title('pdf')
grid()
xlabel('decay time [$ns$ ]')
show()
