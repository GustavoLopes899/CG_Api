from Constants import *
from PolygonClass import *

def ComputeInt(x, x0, y0):
	code = INSIDE
	if x0 < x.xmin:
		code |= LEFT
	elif x0 > x.xmax:
		code |= RIGHT
	if y0 < x.ymin:
		code |= BOTTOM
	elif y0 > x.ymax:
		code |= TOP
	return code

def CohenSutherlandLineClipAndDraw(x, y):
	accept = False
	z = Polygon()
	for i in range (0, x.vertices):
		if i == x.vertices-1:
			x0 = x.p[i].x
			x1 = x.p[0].x
			y0 = x.p[i].y
			y1 = x.p[0].y
		elif i != x.vertices:
			x0 = x.p[i].x
			x1 = x.p[i+1].x
			y0 = x.p[i].y
			y1 = x.p[i+1].y
		outcode0 = ComputeInt(y, x0, y0)
		outcode1 = ComputeInt(y, x1, y1)	
		while True:
			if not(outcode0 | outcode1):
				accept = True
				break
			elif outcode0 & outcode1:
				break
			else:
				if outcode0:
					outcodeOut = outcode0
				else:
					outcodeOut = outcode1
				if outcodeOut & TOP:
					xAux = x0 + (x1 - x0) * (y.ymax - y0) / (y1 - y0)
					yAux = y.ymax
				elif outcodeOut & BOTTOM:
					xAux = x0 + (x1 - x0) * (y.ymin - y0) / (y1 - y0)
					yAux = y.ymin
				elif outcodeOut & RIGHT:
					yAux = y0 + (y1 - y0) * (y.xmax - x0) / (x1 - x0)
					xAux = y.xmax
				elif outcodeOut & LEFT:
					yAux = y0 + (y1 - y0) * (y.xmin - x0) / (x1 - x0)
					xAux = y.xmin
				if outcodeOut == outcode0:
					x0 = xAux
					y0 = yAux
					outcode0 = ComputeInt(y, x0, y0)
				else:
					x1 = xAux
					y1 = yAux
					outcode1 = ComputeInt(y, x1, y1)	
		if accept:
			z.vertices = z.vertices + 1
			z.p[i+1] = Point()
			z.p[i].x = x0
			z.p[i+1].x = x1
			z.p[i].y = y0
			z.p[i+1].y = y1
			BresenhamLine(x0, y0, x1, y1, x.color)
			print("aceitou")
	print(z.p[0].x, z.p[0].y)	
	print(z.p[1].x, z.p[1].y)	
		
def drawRectangleWindow(window):
	window.ch = 1	# polygon
	window.color = 8
	window.vertices = 4
	print("Program to draw rectangle window:")
	for i in range(0, window.vertices):
		window.p[i] = Point()
		#print("\nEnter the coordinate ", i+1, ": ")
		# window.p[i].x = int(input("x = "))
		# window.p[i].y = int(input("y = "))
		window.p[0].x = 50
		window.p[0].y = 125
		window.p[1].x = 175
		window.p[1].y = 125
		window.p[2].x = 175
		window.p[2].y = 175
		window.p[3].x = 50
		window.p[3].y = 175
		if i == 0:
			window.xmin = window.xmax = window.p[i].x
			window.ymin = window.ymax = window.p[i].y
		else:
			if window.xmin > window.p[i].x:
				window.xmin = window.p[i].x
			else:	
				if window.xmax < window.p[i].x:
					window.xmax = window.p[i].x
			if window.ymin > window.p[i].y:
				window.ymin = window.p[i].y
			else:	
				if window.ymax < window.p[i].y:
					window.ymax = window.p[i].y	
	window.p[i+1].x = window.p[0].x
	window.p[i+1].y = window.p[0].y
	window.PolygonNotFilled()