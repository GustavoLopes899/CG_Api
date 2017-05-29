import sys
from Clipping import *
from Initializate import *
from PolygonClass import *
from PolygonManager import *
	
def main():
	print("Clipping Algorithms:\n")
	x = Polygon()
	inputPolygon(x)
	window = Polygon()
	drawRectangleWindow(window)
	# CohenSutherlandLineClipAndDraw(x, window)
	SutherlandHodgemanClip(x, window)
	Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption('Clipping Algorithms')
	main()