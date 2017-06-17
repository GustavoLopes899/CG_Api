'''
Testing with polygon clipping
'''

import sys
from modules.Clipping import *
from modules.Initializate import *
from modules.PrimitivesClass import *
from modules.PolygonManager import *
	
def main():
	print("Clipping Algorithms:")
	polygonList = inputPolygon()
	choice = int(input("\n Enter 1 to Cohen-Sutherland or 2 to Sutherland-Hodgman Algorithm: "))
	while choice != 1 and choice != 2:
		choice = int(input("\n Enter 1 to Cohen-Sutherland or 2 to Sutherland-Hodgman Algorithm: "))
	if choice == 1:
		polygonList[0] = CohenSutherlandLineClipAndDraw(polygonList[0])
	else:
		polygonList[0] = SutherlandHodgemanClip(polygonList[0])
	print("\nEnd of Program")	
	Initializate.run()
	
if __name__ == "__main__":
	pygame.display.set_caption('Clipping Algorithms')
	main()