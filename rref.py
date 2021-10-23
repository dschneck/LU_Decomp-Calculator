#!/usr/bin/env python3

'''
	Inspiration for the solution came from the following link:
	https://www.math.purdue.edu/~shao92/documents/Algorithm%20REF.pdf

'''

import sys
from matrix import Matrix
from getInput import Input

class RREF:
	def __init__(self, A: Matrix):
		self.flag = False
		#print("Original matrix:")
		#A.printMatrix()
		pivot = 0

		for i in range(A.m):
			if pivot > A.n-1 or pivot > A.m-1:
				break

			row, col = self.__findNonZero(A, pivot)
			if (row, col) == (-1, -1): # case where there are no more nonzero values
				break

			# Interchanging
			if (pivot, pivot) != (row, col):
				if row == A.m-1:
					for j in range(A.m-1, 0, -1):
						if A.matrix[j][pivot] == 0:
							self.flag = False
							A.matrix[j], A.matrix[row] = self.__interchange(A, row, j)
							row = j
							break
				
				else:
					for j in range(row+1, A.m):
						if A.matrix[j][pivot] != 0:
							self.flag = False
							A.matrix[j], A.matrix[row] = self.__interchange(A, row, j)
							row = j
							break

			# Row summing
			for j in range(A.m):
				if j != pivot and A.matrix[j][pivot] != 0 and A.matrix[pivot][pivot] != 0: 
					A.matrix[j] = self.__rowSum(A, j, pivot, -1*A.matrix[j][pivot]/A.matrix[pivot][pivot]) 
			# Scaling
			if A.matrix[pivot][pivot] != 0:
				val = 1/A.matrix[pivot][pivot]
				A.matrix[pivot] = self.__scale(A, pivot, val)

			pivot = pivot + 1

		#print("\nRREF matrix: ")
		#A.printMatrix()
		self.valid = self.__validate(A)

	@staticmethod
	def __validate(A: Matrix):
		flag = 0 # changes if an error is detected

		if A.n != 1:
			for i in range(A.m-1):
				if A.matrix[i][i] != 1:
					flag = 1
					break

		if flag == 0:
			#print("This is a valid RREF")
			return True
		else:
			#print("This is NOT a valid RREF")
			return False


	@staticmethod
	def __findNonZero(A: Matrix, offset: int):
		for i in range(offset, A.m):
			for j in range(A.n):
				if A.matrix[i][j] != 0:
					return i, j
		return -1, -1

	@staticmethod
	def __interchange(A: Matrix, row1: int, row2: int):
		#print(f"\nInterchanging row {row1} and row {row2}")
		return A.matrix[row1], A.matrix[row2]

	@staticmethod
	def __scale(A: Matrix, row: int, scalar: float):
		#print(f"\nScaling row {row} by {scalar}")
		tempRow = A.matrix[row]

		for i in range(A.n):
			tempRow[i] = tempRow[i] * scalar
		return tempRow
		
	@staticmethod
	def __rowSum(A: Matrix, row1: int, row2: int, scalar: float):
		#print(f"\nSumming up row {row1} by {scalar} times row {row2}")
		tempRow = A.matrix[row1]
		tempRow2 = A.matrix[row2]

		for i in range(A.n):
			tempRow[i] = tempRow[i] + scalar * tempRow2[i]

		return tempRow

if __name__ == "__main__":
	if len(sys.argv) == 1: 				# input from command line
		x = Input.getInput()
		y = Matrix(x[0], x[1], x[2])
		z = RREF(y)
	else: 								# input from file
		x = Input.getInput(sys.argv[1])
		y = Matrix(x[0], x[1], x[2])
		z = RREF(y)
