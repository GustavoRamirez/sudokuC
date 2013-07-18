'''
Created on Jul 07, 2013
@author: Rafael Alfaro
'''
import time
class Recursive:
    def __init__(self, board, chr_empty = '0'):
        self.board = board
        self.chr_empty = chr_empty
        self.time = 0.0
        self.solution = ""

    def load_puzzle(self, puzzle):
        digits = list(puzzle)
        grid = self.group(digits, 9)
        return grid

    def get_time(self):
        """
        get "time" from the object

        """
        return self.time

    def get_original(self):
        """
        get the original board
        """
        return self.board

    def get_solution(self):
        """
        get the puzzle solved
        """
        return self.solution

    def find_empty_position(self, grid , value):
        """
        It is a private method get the empty values into the puzzle
        """
        for ri in range(9):
            for ci in range(9):
                if grid[ri][ci] == value:
                    return (ri, ci)

    def get_row(self, grid, pos):
        """
        It is a private method to get the row
        """
        ri, ci = pos
        return grid[ri]

    def get_col(self, grid, pos):
        """
        It is a private method to get the column
        """
        ri, ci = pos
        return [grid[ri][ci] for ri in range(9)]

    def get_block(self, grid, pos):
        """
        It is a private method to get a block form matrix
        """
        ri, ci = pos
        br0 = 3 * (ri/3)
        bc0 = 3 * (ci/3)
        return [grid[br0+r][bc0+c] for r in range(3) for c in range(3)]

    def find_possible_values(self, grid, pos):
        """
        It is a private method find a possible values
        """
        return set("123456789") \
            - set(self.get_row(grid, pos)) \
            - set(self.get_col(grid, pos)) \
            - set(self.get_block(grid, pos))

    def solve(self, grid, chr_empty):
        """
        It is a private method to solve the puzzle
        """
        pos = self.find_empty_position(grid ,self.chr_empty)
        if not pos:
            return grid

        ri, ci = pos
        for n in self.find_possible_values(grid, pos):
            grid[ri][ci] = n
            solution = self.solve(grid,chr_empty)
            if solution:
                return solution
        grid[ri][ci] = chr_empty

    def group(self, xs, n):
        """
        It is a internal method to group part of matrix
        """
        return [xs[i:i+n] for i in range(0, len(xs), n)]

    def display(values):
        """
        This method display the puzzle
        """
        print("\n".join("".join(row) for row in grid))


    def matrix_to_string(self, values):
        """
        This method convert to matrix to string.

        """
        try:
            solution = ""
            len_rows = len (values)
            for i in range(len_rows):
                len_colums = len (values[i])
                for j in range(len_colums):
                    solution = solution + values [i][j]
            return solution
        except:
            self.time = 0.0
            return "None"

    def solve_one_sudoku(self):
        """
        This method solve the puzzle into the object
        get the time used to solve the puzzle in "time"
        and the solution of puzzle is put in "solution"
        """
        #self.board = self.verify_line(self.board,self.chr_empty)
        grid = self.load_puzzle(self.board)
        start = time.clock()
        soln = self.solve(grid,self.chr_empty)
        self.time= time.clock()-start
        self.solution = self.matrix_to_string (soln)
        return self.solution







