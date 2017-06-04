import math
from basicFunctions import *
from PrimitivesClass import *
from PolygonManager import *

def crossProduct(a, b):
	c = Vector()
	c.vector = [a.vector[1]*b.vector[2] - a.vector[2]*b.vector[1],
				a.vector[2]*b.vector[0] - a.vector[0]*b.vector[2],
				a.vector[0]*b.vector[1] - a.vector[1]*b.vector[0]]
	return c

def inputVector():
	v = Vector()
	print("Input Vector:")
	v.x0 = int(input("Enter the x0 coordinate: "))
	v.y0 = int(input("Enter the y0 coordinate: "))
	v.z0 = int(input("Enter the z0 coordinate: "))
	v.x1 = int(input("Enter the x1 coordinate: "))
	v.y1 = int(input("Enter the y1 coordinate: "))
	v.z1 = int(input("Enter the z1 coordinate: "))
	v.vector = [v.x1-v.x0, v.y1-v.y0, v.z1-v.z0]
	return v

def viewTransformation():
	#################### 			x0, y0, z0 -> posição do observador 				####################
	#################### vV -> "lado de cima" do sist. de referencia, exemplo (0,1,0)	####################
	#################### 				vA -> VETOR ALVO(VA)							####################	
	u = Vector()
	v = Vector()
	n = Vector()
	print("View Transformation")
	for i in range(1):
		#vA = inputVector()
		vA = Vector()
		vA.x0 = 0
		vA.y0 = 0
		vA.z0 = 0
		vA.x1 = 1
		vA.y1 = 2
		vA.z1 = 3
		vA.vector = [vA.x1-vA.x0, vA.y1-vA.y0, vA.z1-vA.z0]
		#vV = inputVector()
		vV = Vector()
		vV.x0 = 0
		vV.y0 = 0
		vV.z0 = 0
		vV.x1 = 3
		vV.y1 = 4
		vV.z1 = 0
		vV.vector = [vV.x1-vV.x0, vV.y1-vV.y0, vV.z1-vV.z0]
	moduleN = math.sqrt((vA.x1 - vA.x0)**2 + (vA.y1 - vA.y0)**2 + (vA.z1 - vA.z0)**2)
	print("Modulo N: ", moduleN)
	# n = [vA.vector[0]/moduleN, vA.vector[1]/moduleN, vA.vector[2]/moduleN]
	n.vector[0] = vA.vector[0]/moduleN
	n.vector[1] = vA.vector[1]/moduleN
	n.vector[2] = vA.vector[2]/moduleN
	print("vA = ", vA.vector)
	moduleV = math.sqrt((vV.x1 - vV.x0)**2 + (vV.y1 - vV.y0)**2 + (vV.z1 - vV.z0)**2)
	print("Modulo V: ", moduleV)
	u = crossProduct(vV, vA)
	# print("u prod. vetorial = ", u.vector)
	u.vector[0] = u.vector[0]/moduleV
	u.vector[1] = u.vector[1]/moduleV
	u.vector[2] = u.vector[2]/moduleV
	v = crossProduct(n, u)
	print("u: ", u.vector)
	print("v = ", v.vector)
	print("n = ", n.vector)
	t = [[1, 0, 0, -vA.x0],			## arrumar x0 = posicao da camera
		 [0, 1, 0, -vA.y0],
		 [0, 0, 1, -vA.z0],
		 [0, 0, 0, 	  1  ]]
	#	 
	r = [[u.vector[0], u.vector[1], u.vector[2], 0],
		 [v.vector[0], v.vector[1], v.vector[2], 0],
		 [n.vector[0], n.vector[1], n.vector[2], 0],
		 [	  0		 , 	   0	  , 	0	   , 1]]
	m = [[]]
	m = multiplyMatrix(r, t, 4)
	print("Matrix = ", m)

def orthogonalProjection_3D(axis):
	print("Orthogonal Projection")
	if axix == 1:							# x-axis
		ortogonalMatrix = [[0, 0, 0, 0],
						   [0, 1, 0, 0],
						   [0, 0, 1, 0],
						   [0, 0, 0, 1]]
	elif axis == 2:							# y-axis
		ortogonalMatrix = [[1, 0, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 1, 0],
						   [0, 0, 0, 1]]
	elif axis == 3:							# z-axis
		ortogonalMatrix = [[1, 0, 0, 0],
						   [0, 1, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 0, 1]]
	return ortogonalMatrix
	
def perspectiveProjection_3D(x):
	print("Perspective Projection")
	### centro projecao (xc, yc, zc)
	d = float(math.sqrt((xc-0)**2 + (yc-0)**2 + (zc-xp)**2))
	perspectiveMatrix = [[]]
	perspectiveMatrix = [[0, 0, 0, 0],
						 [0, 1, 0, 0],
						 [0, 0, 1, 0],
						 [0, 0, 0, 1]]