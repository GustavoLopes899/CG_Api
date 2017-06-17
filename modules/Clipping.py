import copy
from modules.Constants import *
from modules.Initializate import *
from modules.PrimitivesClass import *

def ComputeInt(x, x0, y0):							# METHOD TO CHECK IF THE POINT IS INSIDE OF MARGIN (COHEN-SUTHERLAND AUXILIARY)
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

def CohenSutherlandLineClipAndDraw(x):				# COHEN-SUTHERLAND CLIPPING ALGORITHM
	windowSurface.fill(BLACK)
	window = Polygon()
	inputRectangleWindow(window)
	xmin = window.xmin
	xmax = window.xmax
	ymin = window.ymin
	ymax = window.ymax
	z = Polygon()
	for i in range (0, x.vertices):
		accept = False
		if i == x.vertices-1:
			x0 = x.p[i].x
			y0 = x.p[i].y
			x1 = x.p[0].x
			y1 = x.p[0].y
		else:
			x0 = x.p[i].x
			y0 = x.p[i].y
			x1 = x.p[i+1].x
			y1 = x.p[i+1].y
		outcode0 = ComputeInt(window, x0, y0)
		outcode1 = ComputeInt(window, x1, y1)
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
					xAux = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
					yAux = ymax
				elif outcodeOut & BOTTOM:
					xAux = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
					yAux = ymin
				elif outcodeOut & RIGHT:
					yAux = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
					xAux = xmax
				elif outcodeOut & LEFT:
					yAux = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
					xAux = xmin
				if outcodeOut == outcode0:
					x0 = xAux
					y0 = yAux
					outcode0 = ComputeInt(window, x0, y0)
				else:
					x1 = xAux
					y1 = yAux
					outcode1 = ComputeInt(window, x1, y1)	
		if accept:
			z.vertices = z.vertices + 1
			z.p[i+1] = Point()
			z.p[i].x = x0
			z.p[i].y = y0
			z.p[i+1].x = x1
			z.p[i+1].y = y1
			#print("Reta aceita: ", x0, y0, x1, y1)
			BresenhamLine(x0, y0, x1, y1, x.color)
	window.calcMinMax()
	window.drawPolygon()		
	return z		

def SutherlandHodgemanClip(x):						# SUTHERLAND-HODGEMAN CLIPPING ALGORITHM
	window = Polygon()
	inputRectangleWindow(window)
	xmin = window.xmin
	xmax = window.xmax
	ymin = window.ymin
	ymax = window.ymax
	##	Before clipping ##
	window.drawPolygon()
	yes = input()
	left_clip(x, xmin)
	right_clip(x, xmax)
	bottom_clip(x, ymin)
	top_clip(x, ymax)
	##	After clipping ##
	x.calcMinMax()	
	x.drawPolygon()
	window.calcMinMax()
	window.drawPolygon()
	print("End of Program")

def left_clip(x, xmin):								# LEFT CLIP
	temp = list(range(20))
	j = 0
	count = 0
	for i in range(x.vertices):
		if i == x.vertices-1:
			x0 = x.p[i].x
			x1 = x.p[0].x
			y0 = x.p[i].y
			y1 = x.p[0].y
		else:	
			x0 = x.p[i].x
			y0 = x.p[i].y
			x1 = x.p[i+1].x
			y1 = x.p[i+1].y
		print("\nStraight test (left margin): [", x0,",", y0,"] -> [", x1,",", y1,"]")
		if x0 <= xmin and x1 < xmin:					# BOTH POINTS OUT. DO NOT STORE ANY VERTICES
			print("Do not store (left margin)")
		elif x0 >= xmin and x1 >= xmin:					# BOTH POINTS INSIDE. STORING THE SECOND VERTEX
			temp[j] = x1
			temp[j+1] = y1
			j = j + 2
			count = count + 1
			print("From inside to inside (left margin), point saved: [", x1, ",", y1, "]")
		elif x0 <= xmin and x1 >= xmin:					# OUTSIDE TO INSIDE. STORE INTERSECTION AND SECOND VERTEX
			xAux = xmin
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				yAux = y0
			else:
				yAux = y0 + (xmin- x0) * float((y1-y0)/(x1-x0))
			temp[j] = xAux
			temp[j+1] = yAux
			temp[j+2] = x1
			temp[j+3] = y1
			j = j + 4
			count = count + 2
			print("From outside to inside (left margin), points saved (intersection and second vertex): [", xAux,",", yAux,"], [", x1, ",", y1,"]")
		else:											# INSIDE TO OUTSIDE. STORE INTERSECTION ONLY
			xAux = xmin
			yAux = y0 + (xmin - x0) * float((y1-y0)/(x1-x0))
			temp[j] = xAux
			temp[j+1] = yAux
			j = j + 2
			count = count + 1
			print("From inside to outside (left margin), point saved (intersection): [", xAux,",", yAux,"]")
	n = int(count)
	j = 0
	x.vertices = 0
	for i in range(0, 2*n, 2):
		x.p[j] = Point()
		x.p[j].x = temp[i]
		x.p[j].y = temp[i+1]
		j = j + 1
		x.vertices = x.vertices + 1
	x.p[j].x = x.p[0].x	
	x.p[j].y = x.p[0].y
	return x
		
def right_clip(x, xmax):							# RIGHT CLIP
	temp = list(range(20))
	j = 0
	count = 0
	for i in range (x.vertices):
		if i == x.vertices-1:
			x0 = x.p[i].x
			y0 = x.p[i].y
			x1 = x.p[0].x
			y1 = x.p[0].y
		else:	
			x0 = x.p[i].x
			y0 = x.p[i].y
			x1 = x.p[i+1].x
			y1 = x.p[i+1].y
		print("\nStraight test (right margin): [", x0,",", y0,"] -> [", x1,",", y1,"]")	
		if x0 >= xmax and x1 > xmax:					# BOTH POINTS OUT. DO NOT STORE ANY VERTICES
			print("Do not store (right margin)")
		elif x0 <= xmax and x1 <= xmax:					# BOTH POINTS INSIDE. STORING THE SECOND VERTEX
			temp[j] = x1
			temp[j+1] = y1
			j = j + 2
			count = count + 2
			print("From inside to inside (right margin), point saved: [", x1, ",", y1, "]")
		elif x0 >= xmax and x1 <= xmax:					# OUTSIDE TO INSIDE. STORE INTERSECTION AND SECOND VERTEX
			xAux = xmax
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				yAux = y0
			else:
				yAux = y0 + (xmax-x0)*float((y1-y0)/(x1-x0))
			temp[j] = xAux
			temp[j+1] = yAux
			temp[j+2] = x1
			temp[j+3] = y1
			j = j + 4
			count = count + 2
			print("From outside to inside (right margin), points saved (intersection and second vertex): [", xAux,",", yAux,"], [", x1, ",", y1,"]")
		else:											# INSIDE TO OUTSIDE. STORE INTERSECTION ONLY
			xAux = xmax
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				yAux = y0
			else:
				yAux = y0 + (xmax-x0)*float((y1-y0)/(x1-x0))
			temp[j] = xAux
			temp[j+1] = yAux
			j = j + 2
			count = count + 1
			print("From inside to outside (right margin), point saved (intersection): [", xAux,",", yAux,"]")
	n = int(count)
	j = 0
	x.vertices = 0
	for i in range (0, 2*n, 2):
		x.p[j] = Point()
		x.p[j].x = temp[i]
		x.p[j].y = temp[i+1]
		j = j + 1
		x.vertices = x.vertices + 1
	x.p[j].x = x.p[0].x	
	x.p[j].y = x.p[0].y
	return x

def bottom_clip(x, ymin):							# BOTTOM CLIP
	temp = list(range(20))
	j = 0
	count = 0
	for i in range (x.vertices):
		if i == x.vertices-1:
			x0 = x.p[i].x
			y0 = x.p[i].y
			x1 = x.p[0].x
			y1 = x.p[0].y
		else:	
			x0 = x.p[i].x
			y0 = x.p[i].y
			x1 = x.p[i+1].x
			y1 = x.p[i+1].y
		print("\nStraight test (bottom margin): [", x0,",", y0,"] -> [", x1,",", y1,"]")	
		if y0 <= ymin and y1 < ymin:					# Both points out. Do not store any vertices
			print("Do not store (bottom margin)")
		elif y0 >= ymin and y1 >= ymin:					# Both points inside. Storing the second vertex
			temp[j] = x1
			temp[j+1] = y1
			j = j + 2
			count = count + 1
			print("From inside to inside (bottom margin), point saved: [", x1, ",", y1, "]")
		elif y0 <= ymin and y1 >= ymin:					# Outside to inside. Store intersection and second vertex
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				xAux = x0
			else:	
				xAux = x0 + (ymin - y0)/(float((y1-y0)/(x1-x0)))
			yAux = ymin
			temp[j] = xAux
			temp[j+1] = yAux
			temp[j+2] = x1
			temp[j+3] = y1
			j = j + 4
			count = count + 2
			print("From outside to inside (bottom margin), points saved (intersection and second vertex): [", xAux,",", yAux,"], [", x1, ",", y1,"]")
		else:											# Inside to outside. Store intersection only
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				xAux = x0
			else:	
				xAux = x0 + (ymin-y0)/(float((y1-y0)/(x1-x0)))
			yAux = ymin
			temp[j] = xAux
			temp[j+1] = yAux
			j = j + 2
			count = count + 1
			print("From inside to outside (bottom margin), point saved (intersection): [", xAux,",", yAux,"]")
	n = int(count)
	j = 0
	x.vertices = 0
	for i in range (0, 2*n, 2):
		x.p[j] = Point()
		x.p[j].x = temp[i]
		x.p[j].y = temp[i+1]
		j = j + 1
		x.vertices = x.vertices + 1
	x.p[j].x = x.p[0].x	
	x.p[j].y = x.p[0].y
	return x

def top_clip(x, ymax):								# TOP CLIP
	temp = list(range(20))
	j = 0
	count = 0
	for i in range (x.vertices):
		if i == x.vertices-1:
			x0 = x.p[i].x
			y0 = x.p[i].y
			x1 = x.p[0].x
			y1 = x.p[0].y
		else:	
			x0 = x.p[i].x
			y0 = x.p[i].y
			x1 = x.p[i+1].x
			y1 = x.p[i+1].y
		print("\nStraight test (top margin): [", x0,",", y0,"] -> [", x1,",", y1,"]")
		if y0 >= ymax and y1 > ymax: 					# Both points out. Do not store any vertices
			print("Do not store (top margin)")
		elif y0 <= ymax and y1 <= ymax:					# Both points inside. Storing the second vertex
			temp[j] = x1
			temp[j+1] = y1
			j = j + 2
			count = count + 1
			print("From inside to inside (top margin), point saved: [", x1, ",", y1, "]")
		elif y0 >= ymax and y1 <= ymax:					# Outside to inside. Store intersection and second vertex
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				xAux = x0
			else:
				xAux = x0 + (ymax-y0)/(float((y1-y0)/(x1-x0)))
			yAux = ymax
			temp[j] = xAux
			temp[j+1] = yAux
			temp[j+2] = x1
			temp[j+3] = y1
			j = j + 4
			count = count + 2
			print("From outside to inside (top margin), points saved (intersection and second vertex): [", xAux,",", yAux,"], [", x1, ",", y1,"]")
		else:											# Inside to outside. Store intersection only
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				xAux = x0
			else:
				xAux = x0 + (ymax-y0)/(float((y1-y0)/(x1-x0)))
			yAux = ymax
			temp[j] = xAux
			temp[j+1] = yAux
			j = j + 2
			count = count + 1
			print("From inside to outside (top margin), point saved (intersection): [", xAux,",", yAux,"]")
	n = int(count)
	j = 0
	x.vertices = 0
	for i in range (0, 2*n, 2):
		x.p[j] = Point()
		x.p[j].x = temp[i]
		x.p[j].y = temp[i+1]
		j = j + 1
		x.vertices = x.vertices + 1
	x.p[j].x = x.p[0].x	
	x.p[j].y = x.p[0].y
	return x

def inputRectangleWindow(window):					# INPUT FOR THE RECTANGULAR WINDOW
	window.ch = 1	# polygon
	window.color = 8
	window.vertices = 4
	window.window = True
	print("\n Program to draw rectangle window:")
	for i in range(0, window.vertices):
		window.p[i] = Point()
		#print("\n Enter the coordinate ", i+1, ": ")
		# window.p[i].x = int(input(" x = "))
		# window.p[i].y = int(input(" y = "))
		window.p[0].x = 50
		window.p[0].y = 125
		window.p[1].x = 175
		window.p[1].y = 125
		window.p[2].x = 175
		window.p[2].y = 175
		window.p[3].x = 50
		window.p[3].y = 175
	window.calcMinMax()
	return window