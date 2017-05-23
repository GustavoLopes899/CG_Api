from Constants import *
from Initializate import *

def PlotPointsCircumference(xCenter, yCenter, x, y, color):
	pixArray[int(xCenter) + int(x)][int(yCenter) + int(y)] = color
	pixArray[int(xCenter) + int(y)][int(yCenter) + int(x)] = color
	pixArray[int(xCenter) + int(y)][int(yCenter) - int(x)] = color
	pixArray[int(xCenter) + int(x)][int(yCenter) - int(y)] = color
	pixArray[int(xCenter) - int(x)][int(yCenter) - int(y)] = color
	pixArray[int(xCenter) - int(y)][int(yCenter) - int(x)] = color
	pixArray[int(xCenter) - int(y)][int(yCenter) + int(x)] = color
	pixArray[int(xCenter) - int(x)][int(yCenter) + int(y)] = color
			
def BresenhamCircle(xCenter, yCenter, radius, colorAux):
	color = colors[colorAux]
	x = 0
	y = radius
	d = 1 - int(radius)
	PlotPointsCircumference(xCenter, yCenter, x, y, color)
	while int(x) < int(y):
		if d < 0:
			d = d + 2 * x + 3
		else:
			d = d + 2 * (int(x) - int(y)) + 5
			y = int(y) - 1
		x = int(x) + 1
		PlotPointsCircumference(xCenter, yCenter, x, y, color)
	pygame.display.update()	