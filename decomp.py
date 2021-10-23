#!/usr/bin/env python3

from matrix import Matrix
from rref import RREF
from enum import Enum

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


def matrixMult(A, B):
	pass
	

if __name__ == "__main__":
	x = generateIdentity(6) 
	x.printMatrix()
	print(ERO.SWAP.value)
