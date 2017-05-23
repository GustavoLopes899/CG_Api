class Point:
	def __init__(self, coordinates):
		self.x = coordinates[0]
		self.y = coordinates[1]
		self.z = coordinates[2]
        
class Edge:
	def __init__(self, start, stop):
		self.start = start
		self.stop  = stop

class Wireframe:
	def __init__(self):
		self.points = []
		self.edges = []

	def addPoints(self, PointList):
		for points in PointList:
			self.points.append(Point(points))

	def addEdges(self, edgeList):
		for (start, stop) in edgeList:
			self.edges.append(Edge(self.points[start], self.points[stop]))
			
	def outputPoints(self):
		print("\n --- Nodes --- ")
		for i, point in enumerate(self.points):
			print(" %d: (%.2f, %.2f, %.2f)" % (i, point.x, point.y, point.z))

	def outputEdges(self):
		print("\n --- Edges --- ")
		for i, edge in enumerate(self.edges):
			print(" %d: (%.2f, %.2f, %.2f)" % (i, edge.start.x, edge.start.y, edge.start.z),)
			print("to (%.2f, %.2f, %.2f)" % (edge.stop.x,  edge.stop.y,  edge.stop.z))		