import math
from modules.BasicFunctions import *
from modules.Constants import *
from modules.Initializate import *
from modules.PrimitivesClass import *
	
def translation_3D(tX, tY, tZ):				# TRANSLATION 3D #
	translationMatrix = [[1, 0, 0, tX],
						 [0, 1, 0, tY],
						 [0, 0, 1, tZ],
						 [0, 0, 0,  1]]
	return translationMatrix
		
def scale_3D(sX, sY, sZ):					# SCALE 3D #
	scaleMatrix = [[sX , 0 , 0 , 0],
				   [ 0 , sY, 0 , 0],
				   [ 0 , 0 , sZ, 0],
				   [ 0 , 0 , 0 , 1]]
	return scaleMatrix			   
		
def rotation_3D(axis, degrees):				# ROTATION 3D #	
	if axis == 1:		# AXIS-X
		rotationMatrix = [[1, 			0					 , 				0				   , 0],
						  [0, math.cos(math.radians(degrees)), -math.sin(math.radians(degrees)), 0],
						  [0, math.sin(math.radians(degrees)),  math.cos(math.radians(degrees)), 0],
						  [0,			0				     ,				0				   , 1]]
	elif axis == 2:		# AXIS-Y
		rotationMatrix = [[ math.cos(math.radians(degrees)), 0, math.sin(math.radians(degrees)), 0],
						  [				0				   , 1, 			0				   , 0],
						  [-math.sin(math.radians(degrees)), 0, math.cos(math.radians(degrees)), 0],
						  [				0			       , 0, 			0				   , 1]]
	elif axis == 3:		# AXIS-Z
		rotationMatrix = [[math.cos(math.radians(degrees)), -math.sin(math.radians(degrees)), 0, 0],
						  [math.sin(math.radians(degrees)),  math.cos(math.radians(degrees)), 0, 0],
						  [				0				  ,					0				, 1, 0],
						  [				0				  ,					0				, 0, 1]]
		
	return rotationMatrix				  
	
def applyTransformation3D(polygonList, matrixResult):	# METHOD TO APPLY TRANSFORMATION IN THE POLYGON #
	for i in range (0, len(polygonList)):
		for j in range (0, polygonList[i].vertices):
			matrixPoint = [[polygonList[i].p[j].x], [polygonList[i].p[j].y], [polygonList[i].p[j].z], [1]]
			points = multiplyMatrix(matrixResult, matrixPoint, 4)
			polygonList[i].p[j].x = points[0][0]
			polygonList[i].p[j].y = points[1][0]
			polygonList[i].p[j].z = points[2][0]
		polygonList[i].calcMinMax()
		polygonList[i].drawPolygon()
	return polygonList

def InputTransformation3D(polygonList):					# INPUT FOR ALL TRANSFORMATIONS IN 3D #
	matrixList = []
	matrixResult = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
	ch1 = 1
	while ch1 != 0:
		print("\tMENU TRANSFORMATION 3D:")
		print(" 1 . Translation ")
		print(" 2 . Scale ")
		print(" 3 . Rotation ")
		print(" 4 . Mirroring ")
		print(" 5 . Shear ")
		print(" 0 . Exit ")
		ch1 = int(input("\nEnter the option: "))
		if ch1 == 1:		# TRANSLATION #
			tX = int(input("  Enter the X offset: "))
			tY = int(input("  Enter the Y offset: "))
			tZ = int(input("  Enter the Z offset: "))
			matrixList.append(translation_3D(tX, tY, tZ))
		elif ch1 == 2: 		# SCALE #
			ch2 = int(input("  Scale in relation: (1) the origin; (2) arbitrary point: "))
			if ch2 == 1:
				dX = 0
				dY = 0
				dZ = 0
			elif ch2 == 2:
				dX = int(input("  Enter the x coordinate of the arbitrary point: "))
				dY = int(input("  Enter the y coordinate of the arbitrary point: "))
				dZ = int(input("  Enter the z coordinate of the arbitrary point: "))
				matrixList.append(translation_3D(dX, dY, dZ))
			else:
				print("\n Incorrect option")
				continue
			sX = float(input("  Enter the scale at x: "))
			sY = float(input("  Enter the scale at y: "))
			sZ = float(input("  Enter the scale at z: "))
			matrixList.append(scale_3D(sX, sY, sZ))
			if ch2 == 2:
				matrixList.append(translation_3D(-dX, -dY, -dZ))
		elif ch1 == 3:		# ROTATION #
			ch2 = int(input("  Rotation in relation: (1) x-axis; (2) y-axis; (3) z-axis; (4) arbitrary axis: "))
			if ch2 == 1 or ch2 == 2 or ch2 == 3:
				degrees = float(input("  Enter the degrees for rotation: "))
				matrixList.append(rotation_3D(ch2, degrees))
				continue
			elif ch2 == 4:
				reta = Polygon()
				reta.vertices = 2
				for i in range(0, reta.vertices):
					reta.p[i] = Point()
					print(" Point ", i, ":")
					reta.p[i].x = int(input("  Enter the x coordinate: "))
					reta.p[i].y = int(input("  Enter the y coordinate: "))
					reta.p[i].z = int(input("  Enter the z coordinate: "))
				theta = float(input("  Enter the degrees for rotation: "))
				V = Vector()
				V.x0 = reta.p[0].x
				V.y0 = reta.p[0].y
				V.z0 = reta.p[0].z
				V.x1 = reta.p[1].x
				V.y1 = reta.p[1].y
				V.z1 = reta.p[1].z
				V.vector = [V.x1 - V.x0, V.y1 - V.y0, V.z1 - V.z0]
				moduleV = math.sqrt((V.x1 - V.x0)**2 + (V.y1 - V.y0)**2 + (V.z1 - V.z0)**2)
				u = Vector()
									#a					#b					#c
				u.vector = [V.vector[0]/moduleV, V.vector[1]/moduleV, V.vector[2]/moduleV]
				uLinha = Vector()
										#b			 #c
				uLinha.vector = [0, u.vector[1], u.vector[2]]
				moduleULinha = math.sqrt(uLinha.vector[0]**2 + uLinha.vector[1]**2 + uLinha.vector[2]**2)	# d
				alpha = math.asin(u.vector[1]/moduleULinha)
				beta = math.asin(u.vector[0])
				### transladar lugar original ###
				matrixList.append(translation_3D(reta.p[0].x, reta.p[0].y, reta.p[0].z))
				### 6) Rotacionar em torno do eixo x, com o ângulo oposto do realizado no passo (2) ###
				matrixList.append(rotation_3D(1, math.degrees(-alpha)))
				### 5) Rotacionar em torno do eixo y, com o ângulo oposto do realizado no passo (3) ###
				matrixList.append(rotation_3D(2, math.degrees(-beta)))
				### 4) rotacionar em torno do eixo z, com o ângulo desejado ###
				matrixList.append(rotation_3D(3, math.degrees(theta)))
				### 3) rotacionar em torno do eixo y, coincidindo o eixo de rotação com o eixo Ox ###
				matrixList.append(rotation_3D(2, math.degrees(beta)))
				### 2) rotacionar em torno do eixo x (eixo de rotação vai para o plano xz) ###
				matrixList.append(rotation_3D(1, math.degrees(alpha)))
				### 1) transladar 2 objetos, sendo o ponto A da reta == 0 ###
				matrixList.append(translation_3D(-reta.p[0].x, -reta.p[0].y, -reta.p[0].z))			
				polygonList.append(reta)	
				BresenhamLine(reta.p[0].x, reta.p[0].y, reta.p[1].x, reta.p[1].y, reta.color)
			else:
				print("\nIncorrect option")
				continue			
		elif ch1 == 4:		# MIRRORING #
			ch2 = int(input(" Mirroring in relation: (1) x-axis; (2) y-axis; (3) z-axis; (4) arbitrary axis: "))
			if ch2 == 1 or ch2 == 2 or ch2 == 3 or ch2 == 4:
				reta = Polygon()
				reta.vertices = 2
				reta.p[0] = Point()
				reta.p[1] = Point()
				if ch2 == 1:
					reta.p[0].x = 0
					reta.p[0].y = 0
					reta.p[0].z = 0
					reta.p[1].x = 200
					reta.p[1].y = 1
					reta.p[1].z = 1
				elif ch2 == 2:
					reta.p[0].x = 0
					reta.p[0].y = 0
					reta.p[0].z = 0
					reta.p[1].x = 1
					reta.p[1].y = 200
					reta.p[1].z = 1
				elif ch2 == 3:
					reta.p[0].x = 0
					reta.p[0].y = 0
					reta.p[0].z = 0
					reta.p[1].x = 1
					reta.p[1].y = 1
					reta.p[1].z = 200
				theta = 180
				V = Vector()
				V.x0 = reta.p[0].x
				V.y0 = reta.p[0].y
				V.z0 = reta.p[0].z
				V.x1 = reta.p[1].x
				V.y1 = reta.p[1].y
				V.z1 = reta.p[1].z
				V.vector[0] = V.x1 - V.x0
				V.vector[1] = V.y1 - V.y0
				V.vector[2] = V.z1 - V.z0
				moduleV = math.sqrt((V.x1 - V.x0)**2 + (V.y1 - V.y0)**2 + (V.z1 - V.z0)**2)
				u = Vector()
				u.vector[0] = V.vector[0]/moduleV		# a
				u.vector[1] = V.vector[1]/moduleV		# b
				u.vector[2] = V.vector[2]/moduleV		# c
				uLinha = Vector()
				uLinha.vector[0] = 0
				uLinha.vector[1] = u.vector[1]			# b	
				uLinha.vector[2] = u.vector[2]			# c
				moduleULinha = math.sqrt(uLinha.vector[0]**2 + uLinha.vector[1]**2 + uLinha.vector[2]**2)	# d
				alpha = math.asin(u.vector[1]/moduleULinha)
				beta = math.asin(u.vector[0])
				### transladar lugar original ###
				matrixList.append(translation_3D(reta.p[0].x, reta.p[0].y, reta.p[0].z))
				### 6) Rotacionar em torno do eixo x, com o ângulo oposto do realizado no passo (2) ###
				matrixList.append(rotation_3D(1, math.degrees(-alpha)))
				### 5) Rotacionar em torno do eixo y, com o ângulo oposto do realizado no passo (3) ###
				matrixList.append(rotation_3D(2, math.degrees(-beta)))
				### 4) rotacionar em torno do eixo z, com o ângulo desejado ###
				matrixList.append(rotation_3D(3, math.degrees(theta)))
				### 3) rotacionar em torno do eixo y, coincidindo o eixo de rotação com o eixo Ox ###
				matrixList.append(rotation_3D(2, math.degrees(beta)))
				### 2) rotacionar em torno do eixo x (eixo de rotação vai para o plano xz) ###
				matrixList.append(rotation_3D(1, math.degrees(alpha)))
				### 1) transladar 2 objetos, sendo o ponto A da reta == 0 ###
				matrixList.append(translation_3D(-reta.p[0].x, -reta.p[0].y, -reta.p[0].z))			
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
		print()		
	while matrixList != []:
		matrixResult = multiplyMatrix(matrixResult, matrixList[0], 4)
		matrixList.pop(0)
	polygonList = applyTransformation3D(polygonList, matrixResult)