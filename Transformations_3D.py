from Constants import *
from Initializate import *
from PolygonClass import *
import math

def translation_3D(x, tX, tY):
	print("To do")
'''	
	windowSurface.fill(BLACK)
	if x.ch == 1:
		for i in range(0, x.vertices+1):
			x.p[i].x = int(x.p[i].x) + tX
			x.p[i].y = int(x.p[i].y) + tY
		x.xmin = x.xmin + tX	
		x.xmax = x.xmax + tX	
		x.ymin = x.ymin + tY	
		x.ymax = x.ymax + tY
	elif x.ch == 2:			# CIRCLE #
		x.p[0].x = int(x.p[0].x) + tX
		x.p[0].y = int(x.p[0].y) + tY
	if x.fill == 0:
		x.PolygonNotFilled()
	elif x.fill == 1:
		x.PolygonFilled()
	return x
'''	
		
def scale_2D(x, sX, sY, sC, dX, dY):
	print("To do")
'''	
	windowSurface.fill(BLACK)
	if dX != 0 and dY != 0:
		translation_2D(x, -dX, -dY)
		yes = input()
	if x.ch == 1:			# POLYGON #
		for i in range(0, x.vertices+1):
			x.p[i].x = int(x.p[i].x) * sX
			x.p[i].y = int(x.p[i].y) * sY
		x.xmin = x.xmin * sX	
		x.xmax = x.xmax * sX	
		x.ymin = x.ymin * sY	
		x.ymax = x.ymax * sY	
	elif x.ch == 2:			# CIRCLE #
		x.radius = int(x.radius) * sC
	if dX != 0 and dY != 0:	
		translation_2D(x, dX, dY)	
	if x.fill == 0:
		x.PolygonNotFilled()
	elif x.fill == 1:
		x.PolygonFilled()
	return x	
'''
		
def rotation_3D(x, degrees, dX, dY):
	print("To do")
'''	
	############################## APAGAR POLIGONO ANTIGO ##############################
	print("\nRotation Around The Origin:")
	if dX != 0 and dY != 0:
		translation_2D(x, -dX, -dY)	
	if x.ch == 1:			# POLYGON #
		for i in range(0, x.vertices+1):
			xCos = x.p[i].x * math.cos(math.radians(degrees))
			xSin = x.p[i].x * math.sin(math.radians(degrees))
			yCos = x.p[i].y * math.cos(math.radians(degrees))
			ySin = x.p[i].y * math.sin(math.radians(degrees))
			x.p[i].x = int(xCos - ySin)								# x*cos? – y*sen?
			x.p[i].y = int(yCos + xSin)								# y*cos? + x*sen?
			if x.p[i].x < x.xmin:
				x.xmin = x.p[i].x
			if x.p[i].x > x.xmax:
				x.xmax = x.p[i].x	
			if x.p[i].y < x.ymin:
				x.ymin = x.p[i].y
			if x.p[i].y > x.ymax:
				x.ymax = x.p[i].y	
	elif x.ch == 2:			# CIRCLE #
		xCos = int(x.p[0].x) * math.cos(math.radians(degrees))
		xSin = int(x.p[0].x) * math.sin(math.radians(degrees))
		yCos = int(x.p[0].y) * math.cos(math.radians(degrees))
		ySin = int(x.p[0].y)* math.sin(math.radians(degrees))
		x.p[0].x = int(xCos - ySin)									# x*cos? – y*sen?
		x.p[0].y = int(yCos + xSin)									# y*cos? + x*sen?
	if dX != 0 and dY != 0:	
		translation_2D(x, dX, dY)	
	if x.fill == 0:
		x.PolygonNotFilled()
	elif x.fill == 1:
		x.PolygonFilled()
	return x
'''	