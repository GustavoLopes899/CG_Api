import sys
from Clipping import *
from Initializate import *
from PolygonClass import *
from PolygonManager import *
	
def main():
	x = Polygon()
	inputPolygon(x)
	window = Polygon()
	inputPolygon(window)
	windowSurface.fill(BLACK)
	drawRectangleWindow(window)
	CohenSutherlandLineClipAndDraw(x, window)
	Initializate.run()
'''	
	for i in range (0, x.vertices):
		if i == x.vertices-1:
			CohenSutherlandLineClipAndDraw(x, window, x.p[i].x, x.p[0].x, x.p[i].y, x.p[0].y)
		elif i != x.vertices:
			CohenSutherlandLineClipAndDraw(x, window, x.p[i].x, x.p[i+1].x, x.p[i].y, x.p[i+1].y)
'''			
	# Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption('Clipping Algorithms')
	main()