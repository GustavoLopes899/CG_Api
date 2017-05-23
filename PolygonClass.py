from BresenhamCircle import *
from BresenhamLine import *
from Transformations_2D import *
import math

class Point:
	def __init__(self):
		x = None
		y = None

class Polygon:
	x = None
	y = None
	xmin = None
	ymin = None
	xmax = None
	ymax = None
	c = None
	color = None
	
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
		print("\n\tMENU: ")
		print("1 . Not filled ")
		print("2 . Scan Line Fill ")
		print("3 . Exit ")
		ch1 = int(input("\nEnter the option: "))
		# NOT FILLED #
		if ch1 == 1:
			self.fill = 0
			self.PolygonNotFilled()
		# SCAN-LINE FILL #		
		elif ch1 == 2:
			self.fill = 1	
			self.PolygonFilled()
		# END OF PROGRAM #				
		elif ch1 == 3:		
			print("End Of Program")		

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
			
	def InputTransformation(self):
		lisTransformations = []
		num_transformations = 0
		ch1 = 1
		while ch1 != 0:
			print("\n\tMENU:")
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
				#self = translation(self, tX, tY)
				lisTransformations.append("translation_2D(self, " + str(tX) + ", " + str(tY) + ")")
			elif ch1 == 2: 		# SCALE #
				ch2 = int(input("Scale in relation: (1) the origin; (2) arbitrary point: "))
				if ch2 == 1:
					dX = 0
					dY = 0
				elif ch2 == 2:
					dX = int(input("Enter the x coordinate of the arbitrary point: "))
					dY = int(input("Enter the x coordinate of the arbitrary point: "))
				else:
					print("\nIncorrect option")
					continue
				if self.ch == 1:
					sC = 0
					sX = int(input("Enter the scale at x: "))
					sY = int(input("Enter the scale at y: "))
					#self = scale_2D(self, sX, sY, sC, dX, dY)
					lisTransformations.append("scale_2D(self, " + str(sX) + ", " + str(sY) + ", " + str(sC) + ", " + str(dX) + ", " + str(dY) + ")")
				elif self.ch == 2:
					sX = 0
					sY = 0
					sC = float(input("Choose the scale: "))
					#self = scale_2D(self, sX, sY, sC, dX, dY)
					lisTransformations.append("scale_2D(self, " + str(sX) + ", " + str(sY) + ", " + str(sC) + ", " + str(dX) + ", " + str(dY) + ")")
			elif ch1 == 3:		# ROTATION #
				ch2 = int(input("Rotation in relation: (1) the origin; (2) arbitrary point: "))
				if ch2 == 1:
					dX = 0
					dY = 0
				elif ch2 == 2:
					dX = int(input("Enter the x coordinate of the arbitrary point: "))
					dY = int(input("Enter the x coordinate of the arbitrary point: "))
				else:
					print("\nIncorrect option")
					continue
				degrees = int(input("Enter the degrees for rotation: "))
				#self = rotation_2D(self, degrees, dX, dY)
				lisTransformations.append("rotation_2D(self, " + str(degrees) + ", " + str(dX) + ", " + str(dY) + ")")
			elif ch1 == 4:		# MIRRORING #
				# ARRUMAR MIRRORING PARA CIRCULOS #
				mirror = int(input("Enter the desired axis: 1) x; 2) y; 3) xy: "))
				if mirror == 1:
					#self = scale_2D(self, -1, 1, 0, 0, 0)
					lisTransformations.append("scale_2D(self, " + str(-1) + ", " + str(1) + ", " + str(0) + ", " + str(0) + ", " + str(0) + ")")
				elif mirror == 2:
					#self = scale_2D(self, 1, -1, 0, 0, 0)
					lisTransformations.append("scale_2D(self, " + str(1) + ", " + str(-1) + ", " + str(0) + ", " + str(0) + ", " + str(0) + ")")
				elif mirror == 3:
					#self = scale_2D(self, -1, -1, 0, 0, 0)
					lisTransformations.append("scale_2D(self, " + str(-1) + ", " + str(-1) + ", " + str(0) + ", " + str(0) + ", " + str(0) + ")")
				else:
					print("\nIncorrect option")
					continue
			elif ch1 == 5:		# SHEAR #
				axis = int(input("Enter the desired axis to shear: 1)x; 2)y: "))
				if axis == 1:
					shearX = int(input("Enter the value of the x-axis shear: "))
					self = shear(self, axis, shearX)
				elif axis == 2:
					shearY = int(input("Enter the value of the y-axis shear: "))
					self = shear(self, axis, shearY)
			elif ch1 == 0:
				break
			else:
				print("\nIncorrect option")
				continue
			num_transformations = num_transformations + 1
		for i in range (num_transformations-1, -1, -1):
			self = eval(lisTransformations[i])