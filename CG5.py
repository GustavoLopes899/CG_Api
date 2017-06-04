import sys
from Clipping import *
from Initializate import *
from PrimitivesClass import *
from PolygonManager import *
from Projection3D import *
	
def main():
	print("Projections 3D:\n")
	viewTransformation()
	Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption('Projections 3D')
	main()