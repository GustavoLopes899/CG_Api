from modules.Initializate import *
from modules.Constants import *

def antiAliasing(windowSurface):
	print("\n>> Applying Antialiasing, please wait ...")
	matrix = pygame.surfarray.array2d(windowSurface)
	for i in range(0, width-1):
		for j in range(0, height-1):		
			pixel_00 = ((matrix[i-1][j-1] % 256)*(1/9), (matrix[i-1][j-1] / 256 % 256)*(1/9), (matrix[i-1][j-1] / 256 / 256 % 256)*(1/9))
			pixel_01 = ((matrix[i-1][ j ] % 256)*(1/9), (matrix[i-1][ j ] / 256 % 256)*(1/9), (matrix[i-1][ j ] / 256 / 256 % 256)*(1/9))
			pixel_02 = ((matrix[i-1][j+1] % 256)*(1/9), (matrix[i-1][j+1] / 256 % 256)*(1/9), (matrix[i-1][j+1] / 256 / 256 % 256)*(1/9))
			pixel_10 = ((matrix[ i ][j-1] % 256)*(1/9), (matrix[ i ][j-1] / 256 % 256)*(1/9), (matrix[ i ][j-1] / 256 / 256 % 256)*(1/9))
			pixel_11 = ((matrix[ i ][ j ] % 256)*(1/9), (matrix[ i ][ j ] / 256 % 256)*(1/9), (matrix[ i ][ j ] / 256 / 256 % 256)*(1/9))
			pixel_12 = ((matrix[ i ][j+1] % 256)*(1/9), (matrix[ i ][j+1] / 256 % 256)*(1/9), (matrix[ i ][j+1] / 256 / 256 % 256)*(1/9))
			pixel_20 = ((matrix[i+1][j-1] % 256)*(1/9), (matrix[i+1][j-1] / 256 % 256)*(1/9), (matrix[i+1][j-1] / 256 / 256 % 256)*(1/9))
			pixel_21 = ((matrix[i+1][ j ] % 256)*(1/9), (matrix[i+1][ j ] / 256 % 256)*(1/9), (matrix[i+1][ j ] / 256 / 256 % 256)*(1/9))
			pixel_22 = ((matrix[i+1][j+1] % 256)*(1/9), (matrix[i+1][j+1] / 256 % 256)*(1/9), (matrix[i+1][j+1] / 256 / 256 % 256)*(1/9))
			RGBint = tuple(map(sum, zip(pixel_00, pixel_01, pixel_02, pixel_10, pixel_11, pixel_12, pixel_20, pixel_21, pixel_22)))
			pixArray[i][j] = RGBint
	print("\n>> Antialiasing is complete")		