'''
Testes com transformações 3D
'''

import sys
from AntiAliasing import *
from Initializate import *
from PrimitivesClass import *
from PolygonManager import *
	
def main():
	x = Polygon()					# File: PrimitivesClass.py
	inputPolygon(x)					# File: PolygonManager.py
	#antiAliasing(windowSurface)	# File: AntiAliasing.py
	Initializate.run()				# File: Initializate.py
	
if __name__ == "__main__":
	pygame.display.set_caption("Polygons")
	main()