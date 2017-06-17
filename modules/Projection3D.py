import math
from modules.BasicFunctions import *
from modules.PrimitivesClass import *
from modules.PolygonManager import *

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

def inputCameraPosition():
	x0 = int(input("Enter the x0 coordinate from the camera: "))
	y0 = int(input("Enter the y0 coordinate from the camera: "))
	z0 = int(input("Enter the z0 coordinate from the camera: "))
	return (x0, y0, z0)

def inputCenterPosition():
	xC = int(input("\nEnter the xC coordinate: "))
	yC = int(input("Enter the yC coordinate: "))
	zC = int(input("Enter the zC coordinate: "))
	return (xC, yC, zC, 1)

def viewTransformation():			# DISPLAY TRANSFORMATION MATRIX #
	#################### 			x0, y0, z0 -> posição do observador 				####################
	#################### vV -> "lado de cima" do sist. de referencia, exemplo (0,1,0)	####################
	#################### 				vA -> VETOR ALVO(VA)							####################	
	u = Vector()
	v = Vector()
	n = Vector()
	print("View Transformation:\n")
	for i in range(1):			# remover depois
		camera = inputCameraPosition()
		#vA = inputVector()
		#### Test #####
		vA = Vector()
		vA.x0 = 0
		vA.y0 = 0
		vA.z0 = 0
		vA.x1 = 1
		vA.y1 = 2
		vA.z1 = 3
		vA.vector = [vA.x1-vA.x0, vA.y1-vA.y0, vA.z1-vA.z0]
		################
		#vV = inputVector()
		##### test #####
		vV = Vector()
		vV.x0 = 0
		vV.y0 = 0
		vV.z0 = 0
		vV.x1 = 3
		vV.y1 = 4
		vV.z1 = 0
		vV.vector = [vV.x1-vV.x0, vV.y1-vV.y0, vV.z1-vV.z0]
		################
	moduleN = math.sqrt((vA.x1 - vA.x0)**2 + (vA.y1 - vA.y0)**2 + (vA.z1 - vA.z0)**2)
	#print("Modulo N: ", moduleN)
	n.vector = [vA.vector[0]/moduleN, vA.vector[1]/moduleN, vA.vector[2]/moduleN]
	#print("vA = ", vA.vector)
	moduleV = math.sqrt((vV.x1 - vV.x0)**2 + (vV.y1 - vV.y0)**2 + (vV.z1 - vV.z0)**2)
	#print("Modulo V: ", moduleV)
	u = crossProduct(vV, vA)
	u.vector = [u.vector[0]/moduleV, u.vector[1]/moduleV, u.vector[2]/moduleV]
	v = crossProduct(n, u)
	#print("u: ", u.vector)
	#print("v = ", v.vector)
	#print("n = ", n.vector)
	t = [[1, 0, 0, -camera[0]],
		 [0, 1, 0, -camera[1]],
		 [0, 0, 1, -camera[2]],
		 [0, 0, 0, 	   1  	]]
	#	 
	r = [[u.vector[0], u.vector[1], u.vector[2], 0],
		 [v.vector[0], v.vector[1], v.vector[2], 0],
		 [n.vector[0], n.vector[1], n.vector[2], 0],
		 [	  0		 , 	   0	  , 	0	   , 1]]
	m = multiplyMatrix(r, t, 4)
	print("Matrix = ", m)
	uP0 = m[0][3]
	vP0 = m[1][3]
	nP0 = m[2][3]

def orthogonalProjection_3D(axis):	# ORTOGONAL PROJECTION #
	print("Orthogonal Projection:")
	if axis == 1:							# AXIS-X
		ortogonalMatrix = [[0, 0, 0, 0],
						   [0, 1, 0, 0],
						   [0, 0, 1, 0],
						   [0, 0, 0, 1]]
	elif axis == 2:							# AXIS-Y
		ortogonalMatrix = [[1, 0, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 1, 0],
						   [0, 0, 0, 1]]
	elif axis == 3:							# AXIS-Z
		ortogonalMatrix = [[1, 0, 0, 0],
						   [0, 1, 0, 0],
						   [0, 0, 0, 0],
						   [0, 0, 0, 1]]
	return ortogonalMatrix

def perspectiveProjection_3D():	# PERSPECTIVE PROJECTION #
	print("Perspective Projection:")
	centerProjection = inputCenterPosition()
	xC, yC, zC = (centerProjection[i] for i in range(3))
	d = float(math.sqrt((xC-0)**2 + (yC-0)**2 + (zC-0)**2))
	perspectiveMatrix = [[1, 0,  0 , 0],
						 [0, 1,  0 , 0],
						 [0, 0,  1 , 0],
						 [0, 0, 1/d, 0]]
	return perspectiveMatrix