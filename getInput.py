import sys

class Input:
	@staticmethod
	def getInput(filename=None):
		A =[[]]
		r = None
		c = None

		if filename == None:
			print("How many rows?")
			r = int(input())

			print("How many columns?")
			c = int(input())

			for i in range(r):
				for j in range(c):
					A[i].append(float(input(f'Entry {i},{j}: ')))
				if i != r-1:
					A.append([])
		else:
			print("Getting input from:", filename, sep=" ")
			with open(filename, "r") as matrix:
				s = matrix.read()
				s = s.split()

				r = int(s[0])
				c = int(s[1])

				s = s[2:]
				k = 0

				for i in range(r):
					for j in range(c):
						A[i].append(float(s[k]))
						k += 1
					if i != r-1:
						A.append([])
		print()
		return (A, r, c)
