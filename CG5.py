'''
Tests with 3D projection
'''

import sys
from modules.Initializate import *
from modules.PrimitivesClass import *
from modules.PolygonManager import *
from modules.Projection3D import *
	
def main():
	print("Projections 3D:\n")
	viewTransformation()
	polygonList = inputPolygon()
	if len(polygonList) != 0:
		matrixResult = perspectiveProjection_3D()
		applyProjection3D(polygonList, matrixResult)
	print("\nEnd of Program")	
	Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption('Projections 3D')
	main()