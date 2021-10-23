#!/usr/bin/env python3

from matrix import Matrix
from rref import RREF

class Decomp:
	def __init__(self, A: Matrix):
		if A.n != A.m:
			print("Not a square matrix, LU Decomp unavailable")

if __name__ == "__main__":
	x = Matrix([[1,1],[1,1]],2,2)
	y = RREF(x)
	if y.valid:
		print("It's a valid rref")

	if y.flag == True:
		print("I had to interchange")
	else:
		print("I did not have to interchange")
