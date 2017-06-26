'''
Testes com objetos 3D
'''

import sys
from modules.Initializate import *
from modules.PrimitivesClass import *
from modules.Projection3D import *
	
def main():
	print("Objects with planar polygons:\n")
	object3d = Object3D()
	object3d.inputObject3D()
	print("\nEnd of Program")	
	Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption('Objects with planar polygons')
	main()