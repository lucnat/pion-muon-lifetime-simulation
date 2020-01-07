
from pylab import *
import numpy as np
from globals import t_mu, t_pi 

# lifetimes from PDG
# from http://pdg.lbl.gov/2019/listings/rpp2019-list-muon.pdf
# and http://pdg.lbl.gov/2019/listings/rpp2019-list-pi-plus-minus.pdf

# lifetimes in 1e-6 s = microseconds

f = lambda t: 1/(t_mu - t_pi) * (exp(-t/t_mu))
p = lambda t: 1/(t_mu - t_pi) * (exp(-t/t_mu) - exp(-t/t_pi) )

x = linspace(0,50,1000)
plot(x,p(x))
plot(x,f(x))
show()