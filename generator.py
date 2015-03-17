from agent import Agent
from sudoku import Sudoku
from random import randint
import numpy as np

class Generator:
	def __init__(self, in_path):
		self.in_path = in_path

	def generate(self, n):
		sudoku = Sudoku(self.in_path)
		count = 0
		while(count != n):
			i = randint(0,8)
			j = randint(0,8)
			if(sudoku.arr[i][j] == 0):
				continue
			else:
				sudoku.arr[i][j] = 0
				count += 1
		return sudoku

	def benchmark(self):
		r_file = open("benchmark_a_star.dat","w")
		for i in range(60,61):
			#print("i:  ",i)
			result = []
			for k in range(1):
				sudoku = self.generate(i)
				#sudoku = Sudoku("in2")
				agent = Agent(sudoku)
				sudoku.dump()
				c = agent.solve('A*')
				print("expanded states:  ",c)
				result.append(c)
			r_file.write(str(i)+","+str(np.mean(result))+'\n')
		r_file.close()


