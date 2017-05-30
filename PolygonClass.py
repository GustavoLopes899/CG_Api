import math
from BresenhamCircle import *
from BresenhamLine import *

class Point:
	def __init__(self):
		x = None
		y = None
		z = None	

class Polygon:
	x = None
	y = None
	xmin = None
	ymin = None
	xmax = None
	ymax = None
	c = None
	color = 8
	window = False
	
	def __init__(self):	
		self.ch = 0					# 1 -> polygon e 2 -> circle #
		self.fill = 0				# 0 -> not filled e 1 -> filled #
		self.inter = [None] * 20
		self.p = [Point] * 20
		self.radius = 0
		self.vertices = 0

	def PolygonNotFilled(self):
		if self.ch == 1:		# POLYGON #
			for i in range(0, self.vertices):
				BresenhamLine(int(self.p[i].x), int(self.p[i].y), int(self.p[i+1].x), int(self.p[i+1].y), self.color)
		elif self.ch == 2:		# CIRCLE #
			BresenhamCircle(self.p[0].x, self.p[0].y, self.radius, self.color)
		pygame.event.get()	

	def PolygonFilled(self):
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
		
	def drawPolygon(self):
		if self.window == False:
			windowSurface.fill(BLACK)
		if self.fill == 0:
			self.PolygonNotFilled()
		# SCAN-LINE FILL #		
		elif self.fill == 1:
			self.PolygonFilled()

	def ints(self, s):
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
				
	def sort(self, s):
		for i in range(0, self.vertices):
			BresenhamLine(int(self.p[i].x), int(self.p[i].y), int(self.p[i+1].x), int(self.p[i+1].y), self.color)
		for i in range(0, self.c-1, 2):
			BresenhamLine(int(self.inter[i]), int(s),int(self.inter[i+1]),int(s), self.color)
	
	def calcMinMax(self):
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