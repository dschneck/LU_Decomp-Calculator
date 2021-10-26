class Matrix:
	def  __init__(self, matrix: [[float]], m: float, n: float):
		self.matrix = matrix
		self.m = m
		self.n = n

	def printMatrix(self):
		line = "+++++++++"

		for i in range(self.n):
			line += "++++++++"

		print(line)

		for i in range(self.m):
			print("|\t ", end="")
			for j in range(self.n):
				print(round(self.matrix[i][j],2), end="\t")
			print("|")

		print(line, "\n")
