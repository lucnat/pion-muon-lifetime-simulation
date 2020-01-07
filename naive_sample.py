
from pylab import *
from globals import t_mu, dt_mu, t_pi, dt_pi

pdf = lambda t: 1/(t_mu - t_pi) * (exp(-t/t_mu) - exp(-t/t_pi) )

t_max = t_mu*5

# plot pdf
t = linspace(0,t_max,1000)
plot(t,pdf(t))

# generate data points
x = rand(10000)*t_max
y = rand(10000)*0.00045

samples = []

for i in range(0,1000):
	if(y[i] < pdf(x[i])):
		plot(x[i],y[i],'g.')
		samples.append(x[i])
	else:
		plot(x[i],y[i],'r.')

title('naive rejection method for decay time sampling')
xlabel('decay time [$ns$ ]')

show()