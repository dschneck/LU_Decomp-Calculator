#!/usr/bin/env python3

from matrix import Matrix
from rref import RREF

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

if __name__ == "__main__":
	x = generateIdentity(6) 
	x.printMatrix()
