#!/usr/bin/env python3

import  sys
sys.path.insert(0, '../RREF-calculator')
from matrix import Matrix
from rref import RREF

class Decomp:
	def __init__(self, A: Matrix):
		if A.n != A.m:
			print("Not a square matrix, LU Decomp unavailable")

if __name__ == "__main__":
	x = Matrix([[1,1],[1,1]],2,2)
	x.printMatrix()
	y = RREF(x)

	'''
	if getattr(y, 'flag') == True:
		print("I had to interchange")
	else:
		print("I did not have to interchange")
	'''
