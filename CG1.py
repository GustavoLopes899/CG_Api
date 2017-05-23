import sys
from AntiAliasing import *
from BresenhamCircle import *
from BresenhamLine import *
from Initializate import *

def main():
	opcao = input("Enter 1 to line and 2 to circles: ")
	color = int(input("Choose color: 1-Black; 2-Blue; 3-Gray; 4-Green; 5-Orange; 6-Pink; 7-Purple; 8-Red; 9-White; 10-Yellow: "))
	while color < 1 or color > 10:
		color = int(input("Choose color: 1-Black; 2-Blue; 3-Gray; 4-Green; 5-Orange; 6-Pink; 7-Purple; 8-Red; 9-White; 10-Yellow: "))
	if opcao == "1":
		x1 = input("Enter the coordinate x1: ")
		y1 = input("Enter the coordinate y1: ")
		x2 = input("Enter the coordinate x2: ")
		y2 = input("Enter the coordinate y2: ")
		BresenhamLine(x1, y1, x2, y2, color-1)
	elif opcao == "2":
		xCenter = input("Enter the coordinate x from the center: ")
		yCenter = input("Enter the coordinate y from the center: ")
		radius = input("Enter radius value: ")
		BresenhamCircle(xCenter, yCenter, radius, color-1)
	#antiAliasing(windowSurface)	
	Initializate.run()

if __name__ == "__main__":
	pygame.display.set_caption("Bresenham's Algorithm (Lines And Circles)")
	main()	