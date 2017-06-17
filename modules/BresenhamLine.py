from modules.Constants import *
from modules.Initializate import *

def BresenhamLine(x1, y1, x2, y2, colorAux):
	color = colors[colorAux]
	dx = abs(int(x2) - int(x1))
	dy = abs(int(y2) - int(y1))
	d = 2*dy - dx
	d2 = 2*dx - dy
	const1 = 2*dy
	const2 = 2 * (dy - dx)
	const3 = 2*dx
	const4 = 2*(dx - dy)
	if x1 > x2:
		x = x2
		y = y2
		xFinal = x1
		yFinal = y1
	else:
		x = x1
		y = y1
		xFinal = x2
		yFinal = y2	
	pixArray[int(x)][int(y)] = color
	if dx >= dy:
		if int(x) == int(xFinal):
			if int(y) < int(yFinal):
				while int(y) < int(yFinal):
					y = int(y) + 1
					pixArray[int(x)][int(y)] = color
			else:
				while int(y) > int(yFinal):
					y = int(y) - 1
					pixArray[int(x)][int(y)] = color
		while int(x) < int(xFinal):
			x = int(x) + 1
			if d < 0:
				d = d + const1
			else:
				if int(yFinal) < int(y):
					y = int(y) - 1
				else:	
					y = int(y) + 1
				d = d + const2
			pixArray[int(x)][int(y)] = color
	else:
		if int(y) == int(yFinal):
			if int(x) < int(xFinal):
				while int(x) < int(xFinal):
					x = int(x) + 1
					pixArray[int(x)][int(y)] = color
			else:
				while int(x) > int(xFinal):
					x = int(x) - 1
					pixArray[int(x)][int(y)] = color
		if int(y) < int(yFinal):		
			while int(y) < int(yFinal):
				y = int(y) + 1
				if d2 < 0:
					d2 = d2 + const3
				else:
					if int(xFinal) < int(x):
						x = int(x) - 1
					else:
						x = int(x) + 1
					d2 = d2 + const4
				pixArray[int(x)][int(y)] = color
		else:
			while int(y) > int(yFinal):
				y = int(y) - 1
				if d2 < 0:
					d2 = d2 + const3
				else:
					if int(xFinal) < int(x):
						x = int(x) - 1
					else:
						x = int(x) + 1
					d2 = d2 + const4
				pixArray[int(x)][int(y)] = color	
	pygame.display.update()	