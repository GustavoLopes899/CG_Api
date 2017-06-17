'''
Tests with line and circle drawing
'''

import sys
from modules.AntiAliasing import *
from modules.BresenhamCircle import *
from modules.BresenhamLine import *
from modules.Initializate import *

def main():
	print("Bresenham's Algorithm (Lines And Circles):\n")
	choice = int(input(" Enter 1 to line and 2 to circles: "))
	color = int(input("\n Choose color: 1-Black; 2-Blue; 3-Gray; 4-Green; 5-Orange; 6-Pink; 7-Purple; 8-Red; 9-White; 10-Yellow: "))
	while color < 1 or color > 10:
		color = int(input("\n Choose color: 1-Black; 2-Blue; 3-Gray; 4-Green; 5-Orange; 6-Pink; 7-Purple; 8-Red; 9-White; 10-Yellow: "))
	if choice == 1:
		x1 = input("\n Enter the coordinate x1: ")
		y1 = input(" Enter the coordinate y1: ")
		x2 = input(" Enter the coordinate x2: ")
		y2 = input(" Enter the coordinate y2: ")
		BresenhamLine(x1, y1, x2, y2, color-1)
	elif choice == 2:
		xCenter = input("\n Enter the coordinate x from the center: ")
		yCenter = input(" Enter the coordinate y from the center: ")
		radius = input(" Enter radius value: ")
		BresenhamCircle(xCenter, yCenter, radius, color-1)
	choice = int(input("\n Enter 1 to apply anti-aliasing or 2 to continue: "))
	if choice == 1:
		antiAliasing(windowSurface)
	print("\nEnd of program")
	Initializate.run()

if __name__ == "__main__":
	pygame.display.set_caption("Bresenham's Algorithm (Lines And Circles)")
	main()	