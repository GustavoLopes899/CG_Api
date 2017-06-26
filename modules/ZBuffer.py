'''
Z-Buffer:
InitScreen:
	for i := 0 to N do
		for j := 1 to N do
			Screen[i][j] := BACKGROUND_COLOR; Zbuffer[i][j] := infinito;
DrawZpixel (x, y, z, color):
	if (z <= Zbuffer[x][y]) then
		Screen[x][y] := color; Zbuffer[x][y] := z;
'''		

'''
Z-buffer: Scanline
I.
for each polygon do
	for each pixel (x,y) in the polygon’s projection do
		z := -(D+A*x+B*y)/C;
		DrawZpixel(x, y, z, polygon’s color);
II.
	for each scan-line y do
		for each “in range” polygon projection do
			for each pair (x1, x2) of X-intersections do
				for x := x1 to x2 do
					z := -(D+A*x+B*y)/C;
					DrawZpixel(x, y, z, polygon’s color);
					
If we know zx,y at (x,y) than: zx+1,y = zx,y - A/C	
'''

from modules.Constants import *

def zBufferInit():
	print("Z-Buffer Init Screen")
	ZBuffer = [width][height] * None
	for i in range(0, width-1):
		for j in range(0, height-1):
			pixArray[i][j] = BLACK
			ZBuffer[i][j] = MAX_Z
			
def zBufferDrawPixel(x):
	for i in range(0, width-1):
		for j in range(0, height-1):
			if z <= ZBuffer[i][j]:
				pixArray[i][j] = x.color
				ZBuffer[i][j] = MAX_Z