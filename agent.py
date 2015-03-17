from sudoku import Sudoku
import copy
from heapq import *
class Agent:
	def __init__(self, sudoku):
		self.sudoku = sudoku
		self.visited_states = set()
		self.expanded_states = 0
		self.queue = []


	def solve(self, method):
		if(method == 'DFS'):
			self.solve_by_DFS(self.sudoku)
		elif(method == 'A*'):
			self.solve_by_A_Star(self.sudoku)
		return self.expanded_states


	def solve_by_DFS(self, sudoku):
#		self.visited_states.append(self.get_state(sudoku))
		empties = sudoku.get_empties()
		if(sudoku.done()):
			return True
		if(empties == []):
			return False

		for pos in [empties[0]]: #[empties[0]]:
			for option in sudoku.get_options(pos[0], pos[1]):
				sudoku.arr[pos[0]][pos[1]] = option
				if(sudoku.get_state() in self.visited_states):
					print("len:  ", len(self.visited_states))
					print("shit")
					sudoku.arr[pos[0]][pos[1]] = 0
					continue
				self.expanded_states += 1
				if(self.solve_by_DFS(sudoku)):
					return True
				else:
					sudoku.arr[pos[0]][pos[1]] = 0
		return False

	def solve_by_A_Star(self, sudoku):
		self.visited_states.add(sudoku.get_state())
		heappush(self.queue, (0, sudoku))

		while len(self.queue) > 0:
			self.expanded_states += 1
			print("expanded states:  ", self.expanded_states)
			w, s = heappop(self.queue)
			if(s.done()):
				s.dump()
				print("done!")
				break

			empties = s.get_empties()
			pushed = 0
			for pos in empties:
				for option in s.get_options(pos[0], pos[1]):
					new_state = copy.deepcopy(s)
					new_state.arr[pos[0]][pos[1]] = option
					if(new_state.get_state() in self.visited_states):
						continue
					if not new_state.solvable():
						continue
					t_options = new_state.total_options()
					pushed += 1
					self.visited_states.add(new_state.get_state())
					heappush(self.queue, (t_options, new_state))
