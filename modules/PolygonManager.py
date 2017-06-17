from modules.BresenhamLine import *
from modules.Constants import *
from modules.Initializate import *
from modules.PrimitivesClass import *
from modules.Transformations_2D import *
from modules.Transformations_3D import *

def inputPolygon():
	polygonList = []
	print("\nAlgorithm to draw polygons:")
	choice = int(input(("\n Choose the option (1) for polygon, (2) for circles and (0) to exit: ")))
	x = Polygon()
	#x.color = int(input("\nChoose color: 1-Black; 2-Blue; 3-Gray; 4-Green; 5-Orange; 6-Pink; 7-Purple; 8-Red; 9-White; 10-Yellow: "))
	#while x.color < 1 or x.color > 10:
	#	x.color = int(input("Choose color: 1-Black; 2-Blue; 3-Gray; 4-Green; 5-Orange; 6-Pink; 7-Purple; 8-Red; 9-White; 10-Yellow: "))
	#x.color = x.color - 1
	x.color = 8	
	if choice == 1:
		x.ch = 1
		#x.vertices = int(input("\nEnter the number of vertices of the polygon: "))
		x.vertices = 3
		if x.vertices > 2:
			for i in range(0, x.vertices):
				x.p[i] = Point()
				print("\n Enter the coordinate ", i+1, ": ")
				# x.p[i].x = int(input("  x = "))
				# x.p[i].y = int(input("  y = "))
				# if polygon == 2d:
				# 	x.p[i].z = 1
				# else:
				# x.p[i].z = int(input("  z = "))
				x.p[i].z = 1
				x.p[0].x = 20
				x.p[0].y = 100
				x.p[1].x = 200
				x.p[1].y = 100
				x.p[2].x = 45
				x.p[2].y = 200
			x.calcMinMax()				
		else:
			print("\tNumber of vertices invalid")
	elif choice == 2:
		x.ch = 2
		x.vertices = 1
		#x.p[0].x = input("\nEnter the x coordinate of the center: ")
		#x.p[0].y = input("Enter the y-coordinate of the center: ")
		x.p[0].z = 1
		# x.radius = int(input("Enter radius value: "))
		x.p[0].x = 200
		x.p[0].y = 200
		x.radius = 40
	if choice != 1 and choice != 2:
		print(" Invalid choice")
		print(" End of program")
		exit()
	else:
		print("\n\tMENU: ")
		print(" 1 . Not filled ")
		print(" 2 . Scan Line Fill ")
		ch1 = int(input("\n Enter the option: "))
		while ch1 != 1 and ch1 != 2:
			ch1 = int(input("\n Enter the option: "))
		# NOT FILLED #
		if ch1 == 1:
			x.fill = 0
		# SCAN-LINE FILL #		
		elif ch1 == 2:
			x.fill = 1	
		x.drawPolygon()
		polygonList.append(x)
		# pygame.event.get()	
	# InputTransformation2D(polygonList)
	# InputTransformation3D(polygonList)
	return polygonList		