import numpy as np 
from math import pow, sqrt

def mean(dlist):
	return sum(dlist) / len(dlist)

def median(dlist):
	dlist = sorted(dlist)
	mid_idx = len(dlist) // 2
	
	if len(dlist)%2 == 0: # even
		return (dlist[mid_idx-1]+dlist[mid_idx]) / 2
	else: # odd
		return dlist[mid_idx]

def variance(dlist):
	x_mean = mean(dlist)

	return sum(pow(x - x_mean, 2) for x in dlist) / len(dlist)

def standard_deviation(dlist):
	return sqrt(variance(dlist))	

def covariance(x, y):
	x_mean = mean(x)
	y_mean = mean(y)
	
	d = 0.0
	for i,_ in enumerate(x):
		d += (x[i] - x_mean) * (y[i] - y_mean)

	return d / len(x)	



########## test ############
a = list(range(1, 20, 2))

b = [1,1,3,3,3,3,9,9,9,15]

print(a)
print(b)

print(covariance(a,b))
print(np.cov(a,b))
print(np.mean(np.cov(a,b)))
print(np.correlate(a,b))

