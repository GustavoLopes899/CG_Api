from BresenhamLine import *
from Constants import *
from Initializate import *
from PolygonClass import *
from Transformations_2D import *
from Transformations_3D import *

def inputPolygon(x):
	pygame.event.get()
	print("Algorithm to draw polygons:")
	choise = int(input(("\nChoose the option (1) for polygon, (2) for circles and (0) to exit: ")))
	while choise != 0:
		polygonList = []
		#x.color = int(input("\nChoose color: 1-Black; 2-Blue; 3-Gray; 4-Green; 5-Orange; 6-Pink; 7-Purple; 8-Red; 9-White; 10-Yellow: "))
		#while x.color < 1 or x.color > 10:
		#	x.color = int(input("Choose color: 1-Black; 2-Blue; 3-Gray; 4-Green; 5-Orange; 6-Pink; 7-Purple; 8-Red; 9-White; 10-Yellow: "))
		#x.color = x.color - 1
		x.color = 8	
		if choise == 1:
			x.ch = 1
			#x.vertices = int(input("\nEnter the number of vertices of the polygon: "))
			x.vertices = 3
			if x.vertices > 2:
				for i in range(0, x.vertices):
					x.p[i] = Point()
					print("\nEnter the coordinate ", i+1, ": ")
					# x.p[i].x = int(input("x = "))
					# x.p[i].y = int(input("y = "))
					# if polygon == 2d:
					# 	x.p[i].z = 1
					# else:
					# x.p[i].z = int(input("z = "))
					x.p[i].z = 1
					x.p[0].x = 100
					x.p[0].y = 100
					x.p[1].x = 200
					x.p[1].y = 100
					x.p[2].x = 200
					x.p[2].y = 200
				x.calcMinMax()
			else:
				print("Number of vertices invalid")
		elif choise == 2:
			x.ch = 2
			x.vertices = 1
			#x.p[0].x = input("\nEnter the x coordinate of the center: ")
			#x.p[0].y = input("Enter the y-coordinate of the center: ")
			x.p[0].z = 1
			# x.radius = int(input("Enter radius value: "))
			x.p[0].x = 100
			x.p[0].y = 100
			x.radius = 40
		if choise != 1 and choise != 2:
			print("Invalid choice")
			print("End of program")
			break
		else:
			print("\n\tMENU: ")
			print("1 . Not filled ")
			print("2 . Scan Line Fill ")
			print("0 . Exit ")
			ch1 = int(input("\nEnter the option: "))
			# NOT FILLED #
			if ch1 == 1:
				x.fill = 0
			# SCAN-LINE FILL #		
			elif ch1 == 2:
				x.fill = 1	
			# END OF PROGRAM #				
			elif ch1 == 0:		
				print("End Of Program")
				break
			x.drawPolygon()
			polygonList.append(x)
			InputTransformation2D(polygonList)
			# InputTransformation3D(polygonList)
			pygame.event.get()
			choise = int(input(("\nChoose the option (1) for polygon, (2) for circles and (0) to exit: ")))
			print("End of Program")
	return x		