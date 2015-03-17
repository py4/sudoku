class Sudoku:
    def __init__(self, in_path):
        self.arr = [[0 for x in range(9)] for x in range(9)]
        with open(in_path) as f:
            for i,line in enumerate(f):
                for j,el in enumerate(line.split(' ')):
                    self.arr[i][j] = int(el)

    def get_square(self, i, j):
        res = []
        i = i - (i % 3)
        j = j - (j % 3)
        for x in range(3):
            for y in range(3):
                res.append(self.arr[i+x][j+y])
                #res = self.arr[i+x][j+y]
        return res


    def get_options(self, i, j):
        if(self.arr[i][j] != 0):
            return []

        column = [self.arr[k][j] for k in range(9)]
        row = [self.arr[i][k] for k in range(9)]
        square = self.get_square(i,j)
        return [x for x in range(1,10) if (x not in column and x not in row and x not in square)]

    def get_empties(self):
        res = []
        for x in range(9):
            for y in range(9):
                if(self.arr[x][y] == 0):
                    res.append([x,y])
        return res

    def done(self):
        for i in range(9):
            for j in range(9):
                if(self.arr[i][j] == 0):
                    return False
        return True
