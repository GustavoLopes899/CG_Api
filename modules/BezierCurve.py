from modules.BasicFunctions import *
from modules.Constants import *
from modules.PrimitivesClass import *

def cubicBezier(straight):
	n = 20
	straightAux = Straight(n+1)
	pts = []
	for i in range(n+1):
		t = i / n
		a = (1.0 - t)**3
		b = 3.0 * t * (1. - t)**2
		c = 3.0 * t**2 * (1.0 - t)
		d = t**3
		straightAux.x[i] = float(a * straight.x[0] + b * straight.x[1] + c * straight.x[2] + d * straight.x[3])
		straightAux.y[i] = float(a * straight.y[0] + b * straight.y[1] + c * straight.y[2] + d * straight.y[3])
		pts.append((straightAux.x[i], straightAux.y[i]))
	for i in range(0, n):
		BresenhamLine(straightAux.x[i], straightAux.y[i], straightAux.x[i+1], straightAux.y[i+1], straightAux.color)
	for i in range(0, straight.size):
		pixArray[straight.x[i]-1][straight.y[i]-1] = RED
		pixArray[straight.x[i]-1][straight.y[i]+1] = RED
		pixArray[straight.x[i]+1][straight.y[i]-1] = RED
		pixArray[straight.x[i]+1][straight.y[i]+1] = RED
		pixArray[straight.x[i]][straight.y[i]] = RED
	return straightAux	
			