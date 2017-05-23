from BresenhamLine import *
from Constants import *
from Initializate import *
from PolygonClass import *

def inputPolygon(x):
	pygame.event.get()
	print("Algorithm to draw polygons:")
	x.ch = int(input(("\nChoose the option (1) for polygon, (2) for circles and (0) to exit: ")))
	while x.ch != 0:
		#x.color = int(input("\nChoose color: 1-Black; 2-Blue; 3-Gray; 4-Green; 5-Orange; 6-Pink; 7-Purple; 8-Red; 9-White; 10-Yellow: "))
		#while x.color < 1 or x.color > 10:
		#	x.color = int(input("Choose color: 1-Black; 2-Blue; 3-Gray; 4-Green; 5-Orange; 6-Pink; 7-Purple; 8-Red; 9-White; 10-Yellow: "))
		#x.color = x.color - 1
		x.color = 8	
		if x.ch == 1:	
			#x.vertices = int(input("\nEnter the number of vertices of the polygon: "))
			x.vertices = 3
			if x.vertices > 2:
				for i in range(0, x.vertices):
					x.p[i] = Point()
					print("\nEnter the coordinate ", i+1, ": ")
					# x.p[i].x = int(input("x = "))
					# x.p[i].y = int(input("y = "))
					x.p[0].x = 100
					x.p[0].y = 100
					x.p[1].x = 200
					x.p[1].y = 100
					x.p[2].x = 100
					x.p[2].y = 200
					if i == 0:
						x.xmin = x.xmax = x.p[i].x
						x.ymin = x.ymax = x.p[i].y
					else:
						if x.xmin > x.p[i].x:
							x.xmin = x.p[i].x
						else:	
							if x.xmax < x.p[i].x:
								x.xmax = x.p[i].x
						if x.ymin > x.p[i].y:
							x.ymin = x.p[i].y
						else:	
							if x.ymax < x.p[i].y:
								x.ymax = x.p[i].y	
				x.p[i+1].x = x.p[0].x
				x.p[i+1].y = x.p[0].y
			else:
				print("Number of vertices invalid")
		elif x.ch == 2:
			x.p[0].x = input("\nEnter the x coordinate of the center: ")
			x.p[0].y = input("Enter the y-coordinate of the center: ")
			x.radius = int(input("Enter radius value: "))
		if x.ch != 1 and x.ch != 2:
			print("Invalid choice")
			print("End of program")
			break
		else:	
			x.drawPolygon()
			x.InputTransformation()
			pygame.event.get()
			x.ch = int(input(("\nChoose the option (1) for polygon, (2) for circles and (0) to exit: ")))