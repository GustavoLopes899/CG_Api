import math
from modules.BasicFunctions import *
from modules.Constants import *
from modules.Initializate import *
from modules.PrimitivesClass import *
	
def translation_2D(tX, tY):				# TRANSLATION 2D #
	translationMatrix = [[1, 0, tX],
						 [0, 1, tY],
						 [0, 0,  1]]
	return translationMatrix
		
def scale_2D(sX, sY):					# SCALE 2D #
	scaleMatrix = [[sX , 0 , 0],
				   [ 0 ,sY , 0],
				   [ 0 , 0 , 1]]
	return scaleMatrix			   
		
def rotation_2D(degrees):				# ROTATION 2D #	
	rotationMatrix = [[math.cos(math.radians(degrees)), -math.sin(math.radians(degrees)), 0],
					  [math.sin(math.radians(degrees)),  math.cos(math.radians(degrees)), 0],
					  [				0				  ,					0				, 1]]
	return rotationMatrix				  
		
def shear(axis, sh):					# SHEAR 2D #
	if axis == 1:		# X axis
		shearMatrix = [[1, sh, 0],
					   [0, 1 , 0],
					   [0, 0 , 1]]
	elif axis == 2:		# Y axis	
		shearMatrix = [[1 , 0, 0],
					   [sh, 1, 0],
					   [0 , 0, 1]]
	return shearMatrix	

def applyTransformation(polygonList, matrixResult):		# METHOD TO APPLY TRANSFORMATION IN THE POLYGON #
	windowSurface.fill(BLACK)
	for i in range (0, len(polygonList)):
		for j in range (0, polygonList[i].vertices):
			matrixPoint = [[polygonList[i].p[j].x], [polygonList[i].p[j].y], [polygonList[i].p[j].z]]
			points = multiplyMatrix(matrixResult, matrixPoint, 3)
			polygonList[i].p[j].x = points[0][0]
			polygonList[i].p[j].y = points[1][0]
			polygonList[i].p[j].z = points[2][0]
		polygonList[i].calcMinMax()
		polygonList[i].drawPolygon()
		print("desenhou")
	return polygonList

def InputTransformation2D(polygonList):					# INPUT FOR ALL TRANSFORMATIONS IN 2D #
	matrixList = []
	matrixResult = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
	ch1 = 1
	print()
	while ch1 != 0:
		print("\tMENU TRANSFORMATION 2D:")
		print(" 1 . Translation ")
		print(" 2 . Scale ")
		print(" 3 . Rotation ")
		print(" 4 . Mirroring ")
		print(" 5 . Shear ")
		print(" 0 . Exit ")
		ch1 = int(input("\n Enter the option: "))
		if ch1 == 1:			# TRANSLATION #
			tX = int(input(" Enter the X offset: "))
			tY = int(input(" Enter the Y offset: "))
			matrixList.append(translation_2D(tX, tY))
		elif ch1 == 2: 			# SCALE #
			ch2 = int(input("Scale in relation: (1) the origin; (2) arbitrary point: "))
			if ch2 == 1:
				dX = 0
				dY = 0
			elif ch2 == 2:
				dX = int(input(" Enter the x coordinate of the arbitrary point: "))
				dY = int(input(" Enter the y coordinate of the arbitrary point: "))
				matrixList.append(translation_2D(dX, dY))
			else:
				print("\n Incorrect option")
				continue
			if polygonList[0].ch == 1:	
				sX = float(input(" Enter the scale at x: "))
				sY = float(input(" Enter the scale at y: "))
				matrixList.append(scale_2D(sX, sY))
			elif polygonList[0].ch == 2:
				sC = float(input(" Enter the scale of the circle: "))
				polygonList[0].radius = polygonList[0].radius * sC
				matrixList.append(scale_2D(sC, sC))
			if ch2 == 2:
				matrixList.append(translation_2D(-dX, -dY))
		elif ch1 == 3:			# ROTATION #
			ch2 = int(input(" Rotation in relation: (1) the origin; (2) arbitrary point: "))
			if ch2 == 1:
				dX = 0
				dY = 0
			elif ch2 == 2:
				dX = int(input(" Enter the x coordinate of the arbitrary point: "))
				dY = int(input(" Enter the y coordinate of the arbitrary point: "))
				matrixList.append(translation_2D(dX, dY))
			else:
				print("\n Incorrect option")
				continue
			degrees = float(input(" Enter the degrees for rotation: "))
			matrixList.append(rotation_2D(degrees))
			if ch2 == 2:
				matrixList.append(translation_2D(-dX, -dY))
		elif ch1 == 4:			# MIRRORING #
			mirror = int(input(" Enter the desired axis: 1) x; 2) y; 3) xy; 4) arbitrary line: "))
			if mirror == 1:
				matrixList.append(scale_2D(1, -1))
			elif mirror == 2:
				matrixList.append(scale_2D(-1, 1))
			elif mirror == 3:
				matrixList.append(scale_2D(-1, -1))
			elif mirror == 4:
				reta = Polygon()
				reta.vertices = 2
				for i in range(0, reta.vertices):
					reta.p[i] = Point()
					# print("Point ", i, ":")
					# reta.p[i].x = int(input(" Enter the x coordinate: "))
					# reta.p[i].y = int(input(" Enter the y coordinate: "))
					reta.p[i].z = 1
				#### TEST ####		
				reta.p[0].x = 200
				reta.p[0].y = 50
				reta.p[1].x = 400
				reta.p[1].y = 250
				##############
				if (reta.p[1].x - reta.p[0].x) == 0:
					theta = 0
				else:
					mReta = (reta.p[1].y - reta.p[0].y)/(reta.p[1].x - reta.p[0].x)
					theta = math.atan(mReta)
				### transladar lugar original ###
				matrixList.append(translation_2D(reta.p[0].x, reta.p[0].y))
				### rotacao 2 objetos, angulo -theta ###
				matrixList.append(rotation_2D(math.degrees(-theta)))
				### espelhar o objeto desejado ###
				matrixList.append(scale_2D(-1, 1))
				### rotacao 2 objetos, sendo reta paralela (em cima) de algum eixo (angulo theta) ###
				matrixList.append(rotation_2D(math.degrees(theta)))
				### transladar 2 objetos, sendo o ponto A da reta == 0 ###
				matrixList.append(translation_2D(-reta.p[0].x, -reta.p[0].y))
				polygonList.append(reta)	
				BresenhamLine(reta.p[0].x, reta.p[0].y, reta.p[1].x, reta.p[1].y, reta.color)			
			else:
				print("\nIncorrect option")
				continue
		elif ch1 == 5:			# SHEAR #
			if polygonList[0].ch == 1:
				axis = int(input(" Enter the desired axis to shear: 1)x; 2)y: "))
				if axis == 1:
					shearX = float(input(" Enter the value of the x-axis shear: "))
					matrixList.append(shear(axis, shearX))
				elif axis == 2:
					shearY = float(input(" Enter the value of the y-axis shear: "))
					matrixList.append(shear(axis, shearY))
			elif polygonList[0].ch == 2:
				print("\n Shear in the circle unavailable.")
		elif ch1 == 0:
			break
		else:
			print("\n Incorrect option")
			continue
		print()	
	while matrixList != []:
		matrixResult = multiplyMatrix(matrixResult, matrixList[0], 3)
		matrixList.pop(0)
	polygonList = applyTransformation(polygonList, matrixResult)