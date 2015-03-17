from sudoku import Sudoku
class Agent:
	def __init__(self, sudoku):
		self.sudoku = sudoku
		self.visited_states = []
		self.expanded_states = 0

	def solve(self, method):
		if(method == 'DFS'):
			self.solve_by_DFS(self.sudoku)
		return self.expanded_states


	def solve_by_DFS(self, sudoku):
		empties = sudoku.get_empties()
		if(sudoku.done()):
			return True
		if(empties == []):
			return False

		for pos in [empties[0]]:
			for option in sudoku.get_options(pos[0], pos[1]):
				sudoku.arr[pos[0]][pos[1]] = option
				if(self.get_state(sudoku) in self.visited_states):
					sudoku.arr[pos[0]][pos[1]] = 0
					continue
				self.expanded_states += 1
				if(self.solve_by_DFS(sudoku)):
					return True
				else:
					sudoku.arr[pos[0]][pos[1]] = 0
		return False

	def get_state(self, sudoku):
		return [item for sublist in sudoku.arr for item in sublist]

	def dump(self, sudoku):
		for i in range(9):
			print ' '.join([str(x) for x in sudoku.arr[i]])

