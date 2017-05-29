import sys
from Initializate import *
from GeometricSolidClass import *
from ProjectionViewer import *
	
def main():
	cube = Wireframe()
	cube.addPoints([(x,y,z) for x in (50,250) for y in (50,250) for z in (50,250)])
	cube.addEdges([(n,n+4) for n in range(0,4)]+[(n,n+1) for n in range(0,8,2)]+[(n,n+2) for n in (0,1,4,5)])
	pv = ProjectionViewer(400, 300)
	pv.addWireframe('cube', cube)
	pv.run()

if __name__ == "__main__":
	pygame.display.set_caption('Wireframe Display')
	main()