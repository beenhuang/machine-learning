from math import pow

def Minkowski_Distance(x, y, p):
	xy = zip(x, y)

	return pow(sum(pow(abs(k[0]-k[1]), p) for k in xy), 1/p)