#!/usr/bin/env python3

from matrix import Matrix
from rref import RREF
''' from enum import Enum

class ERO(Enum): # Elementary Row Operations
	SWAP = 1 # Swapping two rows
	RSUM = 2 # Row summation
	SCAL = 3 # Multiply by scalar
	
def generateEROMatrix(op, m, scalar=0):
	ret = generateIdentity(m)

	match op:
		case ERO.SWAP:
			pass
		case ERO.RSUM:
			pass
		case ERO.SCAL:
			for i in range(m):
				ret[i][j] *= scalar
			return ret
'''

def generate2DArray(m, n):
	ret = [[]]
	for i in range(m):
		ret.append([])
	
	for i in range(m):
		for j in range(n):
			ret[i].append(0.0)

	return ret
	
def generateIdentity(n):
	ident = [[]]
	for i in range(n):
		ident.append([])

	for i in range(n):
		for j in range(n):
			if i == j:
				ident[i].append(1.0) 
			else:
				ident[i].append(0.0)
	return Matrix(ident, n, n)


'''
	A: n x m
	B: m x p 
	C: n x p

	for i in 0..n
	  for k in 0..p
		temp = A[i][k]
		for j in 0..m
		  C[i][j] = C[i][j] + temp * B[k][j];
'''
def matrixMult(A, B):
	C = generate2DArray(A.m, B.n)

	for i in range(A.m): #n
		for k in range(B.m): # p
			temp = A.matrix[i][k]
			for j in range(A.m): # m
				C[i][j] = C[i][j] + temp * B.matrix[k][j];
	return Matrix(C, A.m, B.n)
		

if __name__ == "__main__":
	x = Matrix([[1,2,3],[4,5,6]], 2, 3)
	y = Matrix([[1,2],[3,4],[5,6]], 3, 2)
	product = matrixMult(x, y)
	product.printMatrix()

	a = Matrix([[1,2],[4,5]], 2, 2)
	b = Matrix([[1,2],[3,4]], 2, 2)
	product = matrixMult(a,b)
	product.printMatrix()
