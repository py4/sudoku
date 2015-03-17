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
		r_file = open("benchmark.dat","w")
		for i in range(1,82):
			print("i:  ",i)
			result = []
			for k in range(4):
				sudoku = self.generate(i)
				agent = Agent(sudoku)
#				agent.dump(sudoku)
				result.append(agent.solve('DFS'))
			r_file.write(str(i)+","+str(np.mean(result))+'\n')
		r_file.close()


