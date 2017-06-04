#################################################################################
############################ MATRIX OPERATIONS ##################################
#################################################################################

def multiplyMatrix(matrix1, matrix2, tam):		# MULTIPLY 2 MATRIX #
	matrixResult = [[0]*tam for i in range(tam)]	
	for l in range(len(matrix1)):
	   for j in range(len(matrix2[0])):
		   for k in range(len(matrix2)):
			   matrixResult[l][j] += float(matrix1[l][k]) * float(matrix2[k][j])
	return matrixResult
	
#################################################################################
############################ GENERIC OPERATIONS #################################
#################################################################################