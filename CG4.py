import sys
from Clipping import *
from Initializate import *
from PrimitivesClass import *
from PolygonManager import *
	
def main():
	print("Clipping Algorithms:\n")
	x = Polygon()
	inputPolygon(x)
	# drawRectangleWindow(window)
	# CohenSutherlandLineClipAndDraw(x, window)
	SutherlandHodgemanClip(x)
	Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption('Clipping Algorithms')
	main()