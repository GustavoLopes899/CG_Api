import sys
from BezierCurve import *
from Initializate import *
from PrimitivesClass import *
	
def main():
	print("Bezier Curve Algorithm:\n")
	#numberPoints = int(input("Enter the number of points: "))
	numberPoints = 4
	straight = Straight(numberPoints)
	straight.inputPoints()
	straight = cubicBezier(straight)
	Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption('Bezier Curve Algorithm')
	main()