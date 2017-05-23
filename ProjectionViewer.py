from Initializate import *

class ProjectionViewer:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((width, height))
		self.background = (10,10,50)
		self.wireframes = {}
		self.displayNodes = True
		self.displayEdges = True
		self.nodeColour = (255,255,255)
		self.edgeColour = (200,200,200)
		self.nodeRadius = 4
		
	def addWireframe(self, name, wireframe):
		self.wireframes[name] = wireframe
		
	def display(self):
		self.screen.fill(self.background)
		for wireframe in self.wireframes.values():
			if self.displayEdges:
				for edge in wireframe.edges:
					pygame.draw.aaline(self.screen, self.edgeColour, (edge.start.x, edge.start.y), (edge.stop.x, edge.stop.y), 1)
			if self.displayNodes:
				for node in wireframe.points:
					pygame.draw.circle(self.screen, self.nodeColour, (int(node.x), int(node.y)), self.nodeRadius, 0)	
	
	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			self.screen.fill(self.background)
			self.display()
			pygame.display.flip()	