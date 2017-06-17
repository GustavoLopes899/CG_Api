'''
Tests with 3D projection
'''

import sys
from modules.Clipping import *
from modules.Initializate import *
from modules.PrimitivesClass import *
from modules.PolygonManager import *
from modules.Projection3D import *
	
def main():
	print("Projections 3D:\n")
	#viewTransformation()
	matrix = perspectiveProjection_3D()
	print("\nEnd of Program")	
	Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption('Projections 3D')
	main()