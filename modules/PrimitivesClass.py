import math
from modules.BresenhamCircle import *
from modules.BresenhamLine import *

class Object3D:				# CLASS OF OBJECTS 3D #
	def __init__(self):
		size = 0
		self.edge = []
		self.vertices = [Point]*20
		self.surface = []

	def	inputObject3D(self):
		#self.size = int(input("Enter the number of vertices: "))
		self.size = 4
		for i in range(0, self.size):
			print("\nEnter the coordinate ", i, ":")
			self.vertices[i] = Point()
			#self.vertices[i].x = int(input("x = "))
			#self.vertices[i].y = int(input("y = "))
			#self.vertices[i].z = int(input("z = "))
			self.vertices[0].x = 100
			self.vertices[0].y = 100
			self.vertices[0].z = 0
			self.vertices[1].x = 200
			self.vertices[1].y = 100
			self.vertices[1].z = 0
			self.vertices[2].x = 150
			self.vertices[2].y = 300
			self.vertices[2].z = 0
			self.vertices[3].x = 150
			self.vertices[3].y = 175
			self.vertices[3].z = 10
			print("Point [", i, "] = (", self.vertices[i].x, ",", self.vertices[i].y, ",", self.vertices[i].z, ")")
		for j in range(0, self.size*2):
			print("\nEnter two points on the edge ", j, ": ")
			#point1 = int(input("What's the point 1: "))
			#while point1 < 0 or point1 >= self.size:
				#print("Point doesn't exist")
				#point1 = int(input("What's the point 1: "))
			#point2 = int(input("What's the point 2: "))
			#while point2 < 0 or point2 >= self.size:
				#print("Point doesn't exist")
				#point1 = int(input("What's the point 2: "))
			#self.edge.append((point1, point2))
			self.edge.append((0,1))
			self.edge.append((2,0))
			self.edge.append((0,3))
			self.edge.append((1,2))
			self.edge.append((3,1))
			self.edge.append((3,2))
			#choice = int(input("Another edge (1 to yes; 0 to no): "))
			choice = 0	# remover
			if choice == 0:
				break
		self.edge = list(set(self.edge))		# ordenar edges		
		for i in range(0, len(self.edge)):
			print("Edge[", i, "] = ", self.edge[i])		
		print("\n Enter the edges of the polygon surface:")
		#for i in range(1000):
			#print("\nEnter with the edges of the surface ", i, ": ")
			#edgesAux = []
			#while True:
				#edgesSurface = int(input("What's the edge: "))
				#edgesAux.append(edgesSurface)
				#print("EdgeAux = ", edgesAux)
				#choice = int(input("There's another edge? 1 to Yes and 0 to No: "))
				#while choice != 1 and choice != 0:
				#	choice = int(input("There's another edge? 1 to Yes and 2 to No: "))
				#if choice == 1:
				#	continue
				#else:
				#	edgesAux = tuple(edgesAux)
				#	self.surface.append(edgesAux)
				#	print("Surfaces = ", self.surface)
				#	break
			#choice = int(input("There's another surface? 1 to Yes and 0 to No: "))
			#while choice != 1 and choice != 0:
			#	choice = int(input("There's another surface? 1 to Yes and 0 to No: "))
			#if choice == 0:
			#	break
		self.surface.append(((0, 1), (1, 2), (2, 0)))	
		self.surface.append(((0, 3), (3, 2), (2, 0)))	
		self.surface.append(((0, 3), (3, 1), (1, 0)))	
		self.surface.append(((1, 3), (3, 2), (2, 2)))
		for i in range(len(self.surface)):
			print("Surface [", i, "= ", self.surface[i])
		if self.ConsistencyTest():
			for k in range(0, len(self.edge)):
				BresenhamLine(self.vertices[self.edge[k][0]].x, self.vertices[self.edge[k][0]].y,
							  self.vertices[self.edge[k][1]].x, self.vertices[self.edge[k][1]].y, 8)
		return self

	def ConsistencyTest(self):
		aux = []
		found = False
		count = 0
		# Cada vértice deve aparecer em ao menos duas linhas na tabela de arestas
		for i in range(0, self.size):
			count = 0
			for j in range(0, len(self.edge)):
				aux = self.edge[j]
				#print("Aux = ", aux)
				for k in range(0, len(self.edge[j])):
					if i == aux[k]:
						count = count + 1		
			if count < 2:
				print("Inconsistent polygon, invalid number of vertices.")
				return False
		# Toda aresta faz parte de ao menos um polígono (face)
		for i in range(len(self.edge)):						# laço de todas as arestas
			#print("I = ", i)
			found = False
			aux = self.edge[i]
			#print("Aux1 = ", aux)
			for j in range(0, len(self.surface)):			# laço de todos os poligonos
				for k in range(0, len(self.surface[j])):	# laço de cada componente do poligono
					for l in range(0, len(self.surface[j])):
						#print("self.surface[k][l] = ", self.surface[k][l])
						if self.surface[k][l] == aux:
							#print("Achou")
							found = True
							break
					if found:
						break
				if found:
					break
		if not(found):
			print("Inconsistent polygon, edges missing on polygons.")
			return False
		# Todo polígono é fechado
		for i in range(len(self.surface)):		# 4 * (x,y,z)
			for j in range(len(self.surface[i])):	# 3 vezes
				count = 1
				aux = self.surface[i][j][0]
				#print("Aux = ", aux)
				for k in range(len(self.surface[i])):
					#print("Cmp = ", self.surface[i][k][1])
					if aux == self.surface[i][k][1]:
						#print("Achou")
						count = count + 1
						break
				#print("Count = ", count)		
			if count != 2:
				print("Inconsistent polygon, polygon not closed")
				return False
		print("\n Consistency Test: STATUS OK")
		return True

class Straight:				# CLASS OF A SINGLE STRAIGHT #
	def __init__(self, tam):
		self.x = [None]*tam
		self.y = [None]*tam
		self.z = [None]*tam
		self.size = tam
		self.color = 8

	def inputPoints(self):
		for i in range(0, self.size):
			print("\nEnter the coordinate ", i+1, ":")
			#self.x[i] = int(input("x = "))
			#self.y[i] = int(input("y = "))
			#### TEST ####
			self.x[0] = 10
			self.y[0] = 10
			self.x[1] = 150
			self.y[1] = 200
			self.x[2] = 300
			self.y[2] = 450
			self.x[3] = 450
			self.y[3] = 130
			##############
			print("Point [", i+1, "] = (", self.x[i], ",", self.y[i], ")")

class Vector:				# CLASS OF A VECTOR #
	def __init__(self):
		x0 = None
		y0 = None
		x1 = None
		y1 = None
		self.vector = [None] * 3

class Point:				# CLASS OF A SINGLE POINT #
	def __init__(self):
		x = None
		y = None
		z = None	

class Polygon:				# CLASS OF A POLYGON #
	x = None
	y = None
	xmin = None
	ymin = None
	xmax = None
	ymax = None
	c = None
	color = 8

	def __init__(self):	
		self.ch = 0					# 1 -> polygon e 2 -> circle #
		self.fill = 0				# 0 -> not filled e 1 -> filled #
		self.inter = [None] * 20
		self.p = [Point] * 20
		self.radius = 0
		self.vertices = 0

	def PolygonNotFilled(self):		# FUNCTION TO DRAW POLYGONS NOT FILLED #
		if self.ch == 1:		# POLYGON #
			for i in range(0, self.vertices):
				BresenhamLine(int(self.p[i].x), int(self.p[i].y), int(self.p[i+1].x), int(self.p[i+1].y), self.color)
		elif self.ch == 2:		# CIRCLE #
			BresenhamCircle(self.p[0].x, self.p[0].y, self.radius, self.color)
		pygame.event.get()	

	def PolygonFilled(self):		# FUNCTION TO DRAW POLYGONS FILLED #
		if self.ch == 1:		# POLYGON #	
			s = int(self.ymin) + 0.01
			while s <= int(self.ymax):
				self.ints(s)
				self.sort(s)
				s = s + 1
		elif self.ch == 2:		# CIRCLE #
			counter = int(self.p[0].y) + int(self.radius)
			count = int(self.p[0].y) - int(self.radius)
			for i in range (count, counter):
				x1 = int(int(self.p[0].x) + float(math.sqrt((pow(int(self.radius),2)) - ((i - int(self.p[0].y))*(i - int(self.p[0].y))))) + 0.5)
				x2 = int(int(self.p[0].x) - float(math.sqrt((pow(int(self.radius),2)) - ((i - int(self.p[0].y))*(i - int(self.p[0].y))))) + 0.5)
				BresenhamLine(x1, i, x2, i, self.color)	
		pygame.event.get()	

	def drawPolygon(self):			# FUNCTION ANALYZING IF FILLED OR NOT FILLED #	
		#if self.window == False:
			#windowSurface.fill(BLACK)
			#print("Clear Screen")
		if self.fill == 0:
			self.PolygonNotFilled()
		# SCAN-LINE FILL #		
		elif self.fill == 1:
			self.PolygonFilled()

	def ints(self, s):				# SCANLINE AUXILIARY FUNCTION #			
		self.c = 0
		for i in range(0, self.vertices):
			x1 = self.p[i].x
			y1 = self.p[i].y
			x2 = self.p[i+1].x
			y2 = self.p[i+1].y
			if y2 < y1:
				temp = x1
				x1 = x2
				x2 = temp
				temp = y1
				y1 = y2
				y2 = temp
			if s <= int(y2) and s >= int(y1):
				if int(y1) - int(y2) == 0:
					self.x = int(x1)
				else:
					self.x = ((int(x2) - int(x1))*(s - int(y1)))/(int(y2) - int(y1))
					self.x = self.x + int(x1)
				if (self.x <= int(self.xmax)) and (self.x >= int(self.xmin)):
					self.inter[self.c] = self.x
					self.c = self.c + 1

	def sort(self, s):				# SCANLINE AUXILIARY FUNCTION #
		for i in range(0, self.vertices):
			BresenhamLine(int(self.p[i].x), int(self.p[i].y), int(self.p[i+1].x), int(self.p[i+1].y), self.color)
		for i in range(0, self.c-1, 2):
			BresenhamLine(int(self.inter[i]), int(s),int(self.inter[i+1]),int(s), self.color)

	def calcMinMax(self):			# CALCULATE THE NEW POLYGON LIMITS #
		if self.ch == 1:
			for i in range (0, self.vertices):
				if i == 0:
					self.xmin = self.xmax = self.p[i].x
					self.ymin = self.ymax = self.p[i].y
				else:
					if self.xmin > self.p[i].x:
						self.xmin = self.p[i].x
					else:	
						if self.xmax < self.p[i].x:
							self.xmax = self.p[i].x
					if self.ymin > self.p[i].y:
						self.ymin = self.p[i].y
					else:	
						if self.ymax < self.p[i].y:
							self.ymax = self.p[i].y	
			self.p[self.vertices].x = self.p[0].x
			self.p[self.vertices].y = self.p[0].y
		return self