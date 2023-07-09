#! /usr/bin/env python

from scipy import integrate
from math import sqrt, exp, pi # scalar functions are enough here.


def pdf(t):
   return (1/sqrt(2*pi))*exp(-(1./2)*(t-7)**2)
pass

result, error =integrate.quad(pdf, 5, 6)
print result

