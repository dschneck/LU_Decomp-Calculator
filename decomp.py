#!/usr/bin/env python3

import copy
import sys
from matrix import Matrix
from getInput import Input

def removeRow(a, size, x):
	b = copy.deepcopy(a)
	a = a[0:x]

	if x+1 < size:
		b = b[x+1:]
		a += b
	return a

def removeCol(a, x):
	for i in range(len(a)):
		a[i].pop(x)
	return a

def subMatrix(A, x, y):
	a = copy.deepcopy(A.matrix)
	a = removeRow(a,len(a), x)
	a = removeCol(a, y)
	return Matrix(a, A.m-1, A.n-1)

def verifyLeadingMinors(A):
	maxMinorSize = max(A.m, A.n) - abs((A.m-A.n))

	for i in range(1, maxMinorSize):
		tmpMatrix = copy.deepcopy(A.matrix)
		size = len(tmpMatrix)

		while size > i+1:
			removeRow(tmpMatrix, size, size-1)
			size -= 1

		size = len(tmpMatrix[0])

		while size > i+1:
			removeCol(tmpMatrix, size-1)
			size -= 1
		tmp = Matrix(tmpMatrix, i+1, i+1)
		if determinant(tmp) == 0:
			return False
		
	return True

def rowSum(n, base, target, scalar):
	ident = generateIdentity(n)
	ident.matrix[base][target] = scalar
	return ident

def rowScale(n, row, scalar):
	ident = generateIdentity(n)
	ident.matrix[row][row] = scalar
	return ident

def permutation(n, base, target):
	ident = generateIdentity(n)
	tmp = ident.matrix[base]
	ident.matrix[base]  = ident.matrix[target]
	ident.matrix[target] = tmp
	return ident

def determinant(A):
	if A.n == 1:
		return A.matrix[0][0]
	if A.n == 2:
		return A.matrix[0][0] * A.matrix[1][1] - A.matrix[0][1] * A.matrix[1][0]

	det = 0
	for i in range(A.n):
		tmp = subMatrix(A, 0, i)
		det += pow(-1, i+2) * A.matrix[0][i] * determinant(tmp) 

	return det
	
def generate2DArray(m, n):
	ret = [[]]
	for i in range(m):
		ret.append([])
	
	for i in range(m):
		for j in range(n):
			ret[i].append(0.0)

	return ret
	
def invertEM(A):
	for i in range(A.m):
		for j in range(A.n):
			if i != j:
				A.matrix[i][j] *= -1
	return A

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

def findNonZero(A: Matrix, offset: int):
	for i in range(offset, A.m):
		for j in range(A.n):
			if A.matrix[i][j] != 0:
				return i, j
	return -1, -1
		

if __name__ == "__main__":
	if len(sys.argv) == 1:
		x = Input.getInput()
		A = Matrix(x[0], x[1], x[2])
	else:
		x = Input.getInput(sys.argv[1])
		A = Matrix(x[0], x[1], x[2])
	print("A is:")
	A.printMatrix()
	#C = Matrix([[1,0],[-4,1]], 2, 2)
	#D = Matrix([[2,1],[8,7]], 2, 2)

	#matrixMult(C, D).printMatrix()

	E = []
	P = generateIdentity(A.m)
	pivot = 0
	k = 0
	if True:
		for i in range(A.m):
			if pivot > A.n-1 or pivot > A.m-1:
				break

			row, col = findNonZero(A, pivot)
			if (row, col) == (-1, -1): # case where there are no more nonzero values
				break

			# Interchanging
			if (pivot, pivot) != (row, col):
				if row == A.m-1:
					for j in range(A.m-1, 0, -1):
						if A.matrix[j][pivot] == 0:
							P = matrixMult(permutation(A.n, j, row), P)
							A =  matrixMult(P, A)
							row = j
							break
				
				else:
					for j in range(row+1, A.m):
						if A.matrix[j][pivot] != 0:
							P = matrixMult(permutation(A.n, j, row), P)
							A =  matrixMult(P, A)
							row = j
							break

			# Row summing
			for j in range(i+1, A.m):
				if A.matrix[j][i] != 0:
					E.append(rowSum(A.n,j, pivot, -1*A.matrix[j][pivot]/A.matrix[pivot][pivot]))
					print("new row sum")
					E[k].printMatrix()
					A = matrixMult(E[k], A)
					print("Now A is:")
					A.printMatrix()
					k += 1
					
			'''
			for j in range(A.m):
				if j != pivot and A.matrix[j][pivot] != 0 and A.matrix[pivot][pivot] != 0: 
					E.append(rowSum(A.n,j, pivot, -1*A.matrix[j][pivot]/A.matrix[pivot][pivot]))
					print("new row sum")
					E[k].printMatrix()
					A = matrixMult(E[k], A)
					print("Now A is:")
					A.printMatrix()
					k += 1
			pivot += 1
			'''
	else:
		print("LU Decomp does not exist. Program terminated.")

	print("P is: ")
	P.printMatrix()
	print("U is: ")
	U = copy.deepcopy(A)
	U.printMatrix()

	L = generateIdentity(U.m)
	size = len(E)
	for i in range(size-1, -1, -1):
		#print("Going to multiply A with:")
		E[i] = invertEM(E[i])
		#E[i].printMatrix()
		L = matrixMult(E[i], L)
	print("Finally L is:")
	L.printMatrix()
