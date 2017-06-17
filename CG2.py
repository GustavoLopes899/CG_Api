'''
Tests with 2D and 3D transformations
'''

import sys
from modules.AntiAliasing import *
from modules.Initializate import *
from modules.PrimitivesClass import *
from modules.PolygonManager import *
from modules.Transformations_2D import *
from modules.Transformations_3D import *
	
def main():
	print("Transformations 2D & 3D:\n")
	choice = int(input(" Enter 1 to 2D image or 2 to 3D projection: "))
	while choice != 1 and choice != 2:
		choice = int(input(" Enter 1 to 2D image or 2 to 3D projection: "))
	polygonList = inputPolygon()
	if choice == 1:
		InputTransformation2D(polygonList)
	else:	
		InputTransformation3D(polygonList)
	choice = int(input(" Enter 1 to apply anti-aliasing or 2 to continue: "))
	if choice == 1:
		antiAliasing(windowSurface)
	print("\nEnd of Program")
	Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption("Transformations 2D & 3D")
	main()