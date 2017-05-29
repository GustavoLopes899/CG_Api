from Constants import *
from Initializate import *
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
			y0 = x.p[i].y
			x1 = x.p[0].x
			y1 = x.p[0].y
		else:
			x0 = x.p[i].x
			y0 = x.p[i].y
			x1 = x.p[i+1].x
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
			z.p[i].y = y0
			z.p[i+1].x = x1
			z.p[i+1].y = y1
			print("Reta aceita: ", x0, y0, x1, y1)
			BresenhamLine(x0, y0, x1, y1, x.color)
	return z		

def SutherlandHodgemanClip(x, window):
	left_clip(x, window)
	right_clip(x, window)
	bottom_clip(x, window)
	top_clip(x, window)
	x.calcMinMax()	
	x.drawPolygon()
	drawRectangleWindow(window)
	print("End of Program")

def left_clip(x, y):			# LEFT CLIP
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
		print("\nReta teste (margem esquerda): ", x0, y0, x1, y1)	
		if x0 <= y.xmin and x1 < y.xmin:				# Ambos os pontos fora. Não armazenar qualquer vértices
			print("Não armazenar (margem esquerda")
		elif x0 >= y.xmin and x1 >= y.xmin:				# Ambos os pontos dentro. Armazenar o segundo vértice
			temp[j] = x1
			temp[j+1] = y1
			j = j + 2
			count = count + 1
			print("Dentro pra dentro (margem esquerda), ponto salvo: ", x1, y1)
		elif x0 <= y.xmin and x1 >= y.xmin:				# Fora para dentro. Armazenar interseção e segundo vértice
			xAux = y.xmin
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				yAux = y0
			else:
				yAux = y0 + (y.xmin- x0) * float((y1-y0)/(x1-x0))
			temp[j] = xAux
			temp[j+1] = yAux
			temp[j+2] = x1
			temp[j+3] = y1
			j = j + 4
			count = count + 2
			print("Fora pra dentro (margem esquerda), ponto salvo = ", xAux, yAux, x1, y1)
		else:											# Dentro para fora. Armazenar interseção somente
			xAux = y.xmin
			yAux = y0 + (y.xmin - x0) * float((y1-y0)/(x1-x0))
			temp[j] = xAux
			temp[j+1] = yAux
			j = j + 2
			count = count + 1
			print("Dentro pra fora (margem esquerda), ponto salvo = ", xAux, yAux)
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
	for i in range(0, x.vertices):
	 	BresenhamLine(x.p[i].x, x.p[i].y, x.p[i+1].x, x.p[i+1].y, x.color)
	drawRectangleWindow(y)	
	yes = input()
	windowSurface.fill(BLACK)
	return x
		
def right_clip(x, y):			# RIGHT CLIP
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
		print("\nReta teste (margem direita): ", x0, y0, x1, y1)	
		if x0 >= y.xmax and x1 > y.xmax:				# Ambos os pontos fora. Não armazenar qualquer vértices
			print("Não armazenar (margem direita)")
		elif x0 <= y.xmax and x1 <= y.xmax:				# Ambos os pontos dentro. Armazenar o segundo vértice
			temp[j] = x1
			temp[j+1] = y1
			j = j + 2
			count = count + 2
			print("Dentro pra dentro (margem direita), ponto salvo: ", x1, y1)
		elif x0 >= y.xmax and x1 <= y.xmax:				# Fora para dentro. Armazenar interseção e segundo vértice
			xAux = y.xmax
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				yAux = y0
			else:
				yAux = y0 + (y.xmax-x0)*float((y1-y0)/(x1-x0))
			temp[j] = xAux
			temp[j+1] = yAux
			temp[j+2] = x1
			temp[j+3] = y1
			j = j + 4
			count = count + 2
			print("Fora pra dentro (margem direita), reta = ", xAux, yAux, x1, y1)
		else:											# Dentro para fora. Armazenar interseção somente
			xAux = y.xmax
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				yAux = y0
			else:
				yAux = y0 + (y.xmax-x0)*float((y1-y0)/(x1-x0))
			temp[j] = xAux
			temp[j+1] = yAux
			j = j + 2
			count = count + 1
			print("Dentro pra fora (margem direita), ponto salvo = ", xAux, yAux)
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
	for i in range(0, x.vertices):
		BresenhamLine(x.p[i].x, x.p[i].y, x.p[i+1].x, x.p[i+1].y, x.color)
	drawRectangleWindow(y)
	yes = input()
	windowSurface.fill(BLACK)
	return x

def bottom_clip(x, y):			# BOTTOM CLIP
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
		print("\nReta teste (margem baixa): ", x0, y0, x1, y1)	
		if y0 <= y.ymin and y1 < y.ymin:				# Ambos os pontos fora. Não armazenar qualquer vértices
			print("Não armazenar (margem baixa)")
		elif y0 >= y.ymin and y1 >= y.ymin:				# Ambos os pontos dentro. Armazenar o segundo vértice
			temp[j] = x1
			temp[j+1] = y1
			j = j + 2
			count = count + 1
			print("Dentro pra dentro (margem baixa), ponto salvo: ", x1, y1)
		elif y0 <= y.ymin and y1 >= y.ymin:				# Fora para dentro. Armazenar interseção e segundo vértice
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				xAux = x0
			else:	
				xAux = x0 + (y.ymin - y0)/(float((y1-y0)/(x1-x0)))
			yAux = y.ymin
			temp[j] = xAux
			temp[j+1] = yAux
			temp[j+2] = x1
			temp[j+3] = y1
			j = j + 4
			count = count + 2
			print("Fora pra dentro (margem baixa), ponto salvo = ", xAux, yAux, x1, y1)
		else:											# Dentro para fora. Armazenar interseção somente
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				xAux = x0
			else:	
				xAux = x0 + (y.ymin-y0)/(float((y1-y0)/(x1-x0)))
			yAux = y.ymin
			temp[j] = xAux
			temp[j+1] = yAux
			j = j + 2
			count = count + 1
			print("Dentro pra fora (margem baixa), ponto salvo = ", xAux, yAux)
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
	for i in range(0, x.vertices):
		BresenhamLine(x.p[i].x, x.p[i].y, x.p[i+1].x, x.p[i+1].y, x.color)
	drawRectangleWindow(y)
	yes = input()
	windowSurface.fill(BLACK)
	return x

def top_clip(x, y):				# TOP CLIP
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
		print("\nReta teste (margem topo): ", x0, y0, x1, y1)
		if y0 >= y.ymax and y1 > y.ymax: 				# Ambos os pontos fora. Não armazenar qualquer vértices
			print("Não armazenar (margem topo)")
		elif y0 <= y.ymax and y1 <= y.ymax:				# Ambos os pontos dentro. Armazenar o segundo vértice
			temp[j] = x1
			temp[j+1] = y1
			j = j + 2
			count = count + 1
			print("Dentro pra dentro (margem topo), ponto salvo: ", x1, y1)
		elif y0 >= y.ymax and y1 <= y.ymax:				# Fora para dentro. Armazenar interseção e segundo vértice
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				xAux = x0
			else:
				xAux = x0 + (y.ymax-y0)/(float((y1-y0)/(x1-x0)))
			yAux = y.ymax
			temp[j] = xAux
			temp[j+1] = yAux
			temp[j+2] = x1
			temp[j+3] = y1
			j = j + 4
			count = count + 2
			print("Fora pra dentro (margem topo), reta salvo = ", xAux, yAux, x1, y1)
		else:											# Dentro para fora. Armazenar interseção somente
			if (x1 - x0) == 0 or (y1 - y0) == 0:
				xAux = x0
			else:
				xAux = x0 + (y.ymax-y0)/(float((y1-y0)/(x1-x0)))
			yAux = y.ymax
			temp[j] = xAux
			temp[j+1] = yAux
			j = j + 2
			count = count + 1
			print("Dentro pra fora (margem topo), ponto salvo = ", xAux, yAux)
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
	for i in range(0, x.vertices):
		BresenhamLine(x.p[i].x, x.p[i].y, x.p[i+1].x, x.p[i+1].y, x.color)
	drawRectangleWindow(y)
	yes = input()
	windowSurface.fill(BLACK)
	return x

def drawRectangleWindow(window):
	if window.ch != 1:
		window.ch = 1	# polygon
		window.color = 8
		window.vertices = 4
		# print("Program to draw rectangle window:")
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
		print(i)				
		window.p[i+1].x = window.p[0].x
		window.p[i+1].y = window.p[0].y
		for i in range(0, window.vertices+1):
			print(window.p[i].x)
			print(window.p[i].y)
	window.PolygonNotFilled()
	return window