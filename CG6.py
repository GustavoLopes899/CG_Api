'''
Tests with Bezier Curves
'''

import sys
from modules.BezierCurve import *
from modules.Initializate import *
from modules.PrimitivesClass import *
	
def main():
	print("Bezier Curve Algorithm:")
	numberPoints = 4
	straight = Straight(numberPoints)
	straight.inputPoints()
	straight = cubicBezier(straight)
	print("\nEnd of Program")	
	Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption('Bezier Curve Algorithm')
	main()