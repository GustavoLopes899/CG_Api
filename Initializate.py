import abc
import pygame

width = 640
height = 480

pygame.init()
windowSurface = pygame.display.set_mode((width,height),0,32)
pixArray = pygame.PixelArray(windowSurface)

class Initializate:
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def run():
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			#self.screen.fill(self.background)
			pygame.display.flip()	