import math
from Constants import *
from Initializate import *
from PolygonClass import *
	
def translation_3D(tX, tY, tZ):
	print("Translation")
	translationMatrix = [[]]
	translationMatrix = [[1, 0, 0, tX],
						 [0, 1, 0, tY],
						 [0, 0, 1, tZ],
						 [0, 0, 0,  1]]
	return translationMatrix
		
def scale_3D(sX, sY, sZ):
	print("Scale")
	scaleMatrix = [[]]
	scaleMatrix = [[sX , 0 , 0 , 0],
				   [ 0 , sY, 0 , 0],
				   [ 0 , 0 , sZ, 0],
				   [ 0 , 0 , 0 , 1]]
	return scaleMatrix			   
		
def rotation_3D(axis, degrees):
	print("Rotation")
	rotationMatrix = [[]]
	if axix == 1:
		rotationMatrix = [[1, 			0					 , 				0				   , 0],
						  [0, math.cos(math.radians(degrees)), -math.sin(math.radians(degrees)), 0],
						  [0, math.sin(math.radians(degrees)),  math.cos(math.radians(degrees)), 0],
						  [0,			0				     ,				0				   , 1]]
	elif axis == 2:
		rotationMatrix = [[ math.cos(math.radians(degrees)), 0, math.sin(math.radians(degrees)), 0],
						  [				0				   , 1, 			0				   , 0],
						  [-math.sin(math.radians(degrees)), 0, math.cos(math.radians(degrees)), 0],
						  [				0			       , 0, 			0				   , 1]]
	elif axis == 3:
		rotationMatrix = [[math.cos(math.radians(degrees)), -math.sin(math.radians(degrees)), 0, 0],
						  [math.sin(math.radians(degrees)),  math.cos(math.radians(degrees)), 0, 0],
						  [				0				  ,					0				, 1, 0],
						  [				0				  ,					0				, 0, 1]]
		
	return rotationMatrix				  

def multiplyMatrix(matrix1, matrix2):
	matrixResult = [[0]*4 for i in range(4)]	
	for l in range(len(matrix1)):
	   for j in range(len(matrix2[0])):
		   for k in range(len(matrix2)):
			   matrixResult[l][j] += float(matrix1[l][k]) * float(matrix2[k][j])
	return matrixResult
	
def applyTransformation3D(polygonList, matrixResult):
	for i in range (0, len(polygonList)):
		for j in range (0, polygonList[i].vertices):
			matrixPoint = [[polygonList[i].p[j].x], [polygonList[i].p[j].y], [polygonList[i].p[j].z], [1]]
			print("Matrix Points: ", matrixPoint)
			points = multiplyMatrix(matrixResult, matrixPoint)
			print("Points: ", points)
			polygonList[i].p[j].x = points[0][0]
			polygonList[i].p[j].y = points[1][0]
			polygonList[i].p[j].z = points[2][0]
			print("Pontos: ", polygonList[i].p[j].x, polygonList[i].p[j].y, polygonList[i].p[j].z)
		polygonList[i].calcMinMax()
		polygonList[i].drawPolygon()
	return polygonList

def InputTransformation3D(polygonList):
	matrixList = []
	matrixResult = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
	ch1 = 1
	while ch1 != 0:
		print("\n\tMENU TRANSFORMATION 3D:")
		print("1 . Translation ")
		print("2 . Scale ")
		print("3 . Rotation ")
		print("4 . Mirroring ")
		print("5 . Shear ")
		print("0 . Exit ")
		ch1 = int(input("\nEnter the option: "))
		if ch1 == 1:		# TRANSLATION #
			tX = int(input("Enter the X offset: "))
			tY = int(input("Enter the Y offset: "))
			tZ = int(input("Enter the Z offset: "))
			matrixList.append(translation_3D(tX, tY, tZ))
		elif ch1 == 2: 		# SCALE #
			ch2 = int(input("Scale in relation: (1) the origin; (2) arbitrary point: "))
			if ch2 == 1:
				dX = 0
				dY = 0
				dZ = 0
			elif ch2 == 2:
				dX = int(input("Enter the x coordinate of the arbitrary point: "))
				dY = int(input("Enter the y coordinate of the arbitrary point: "))
				dZ = int(input("Enter the z coordinate of the arbitrary point: "))
				matrixList.append(translation_3D(dX, dY, dZ))
			else:
				print("\nIncorrect option")
				continue
			sX = float(input("Enter the scale at x: "))
			sY = float(input("Enter the scale at y: "))
			sZ = float(input("Enter the scale at z: "))
			matrixList.append(scale_3D(sX, sY, sZ))
			if ch2 == 2:
				matrixList.append(translation_3D(-dX, -dY, -dZ))
		elif ch1 == 3:		# ROTATION #
			ch2 = int(input("Rotation in relation: (1) x-axis; (2) y-axis; (3) y-axis; (4) arbitrary axis: "))
			if ch2 == 1 or ch2 == 2 or ch2 == 3:
				degrees = float(input("Enter the degrees for rotation: "))
				matrixList.append(rotation_3D(ch2, degrees))
				continue
			elif ch2 == 4:
				reta = Polygon()
				for i in range(0, 2):
					reta.p[i] = Point()
					print("Point ", i, ":")
					reta.p[i].x = int(input("Enter the x coordinate: "))
					reta.p[i].y = int(input("Enter the y coordinate: "))
					reta.p[i].z = int(input("Enter the z coordinate: "))
				degrees = float(input("Enter the degrees for rotation: "))
				v = ([reta.p[1].x - reta.p[0].x],[reta.p[1].y - reta.p[0].y],[reta.p[1].z - reta.p[0].z])
				print("To Do")	
				### transladar lugar original ###
				
				### rotacao 2 objetos, angulo -theta ###
				
				### Rotacionar em torno do eixo y, coincidindo o eixo de rotação com o eixo Ox ###
				
				### rotacao 2 objetos, sendo eixo arbitrario pertence ao plano xz ###
				matrixList.append(rotation_3D(1, math.degrees(theta)))
				### transladar 2 objetos, sendo o ponto A da reta == 0 ###
				matrixList.append(translation_3D(-reta.p[0].x, -reta.p[0].y, -reta.p[0].z))
				polygonList.append(reta)	
				BresenhamLine(reta.p[0].x, reta.p[0].y, reta.p[1].x, reta.p[1].y, reta.color)
			else:
				print("\nIncorrect option")
				continue
			degrees = float(input("Enter the degrees for rotation: "))
			
			if ch2 == 2:
				matrixList.append(translation_3D(-dX, -dY, -dZ))
		elif ch1 == 4:		# MIRRORING #
			# FAZER TUDO #
			mirror = int(input("Enter the desired axis: 1) x; 2) y; 3) xy; 4) arbitrary line: "))
			if mirror == 1:
				matrixList.append(scale_3D(1, -1))
			elif mirror == 2:
				matrixList.append(scale_3D(-1, 1))
			elif mirror == 3:
				matrixList.append(scale_3D(-1, -1))
			elif mirror == 4:
				reta = Polygon()
				for i in range(0, 2):
					reta.p[i] = Point()
					# print("Point ", i, ":")
					# reta.p[i].x = int(input("Enter the x coordinate: "))
					# reta.p[i].y = int(input("Enter the y coordinate: "))
					reta.p[i].z = 1
				reta.vertices = 2	
				reta.p[0].x = 200
				reta.p[0].y = 50
				reta.p[1].x = 400
				reta.p[1].y = 250
				if (reta.p[1].x - reta.p[0].x) == 0:
					theta = 0
				else:
					mReta = (reta.p[1].y - reta.p[0].y)/(reta.p[1].x - reta.p[0].x)
					theta = math.atan(mReta)
				### transladar lugar original
				matrixList.append(translation_3D(reta.p[0].x, reta.p[0].y))
				### rotacao 2 objetos, angulo -theta
				matrixList.append(rotation_3D(math.degrees(-theta)))
				### espelhar o objeto desejado
				matrixList.append(scale_3D(-1, 1))
				### rotacao 2 objetos, sendo reta paralela (em cima) de algum eixo (angulo theta)
				matrixList.append(rotation_3D(math.degrees(theta)))
				### transladar 2 objetos, sendo o ponto A da reta == 0
				matrixList.append(translation_3D(-reta.p[0].x, -reta.p[0].y))
				polygonList.append(reta)	
				BresenhamLine(reta.p[0].x, reta.p[0].y, reta.p[1].x, reta.p[1].y, reta.color)			
			else:
				print("\nIncorrect option")
				continue
		elif ch1 == 0:
			break
		else:
			print("\nIncorrect option")
			continue
	# print("MatrixList: ", matrixList)		
	while matrixList != []:
		matrixResult = multiplyMatrix(matrixResult, matrixList[0])
		matrixList.pop(0)
	print("matrix result final: ")	
	for r in matrixResult:
		print(r)
	polygonList = applyTransformation3D(polygonList, matrixResult)