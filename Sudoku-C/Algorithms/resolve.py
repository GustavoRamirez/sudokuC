from test_sudoku import TestSudoku
from print_solve_game import PrintSolveGame
from position import Position
import time

class Resolve:
    def __init__(self, str_sudoku):
        self.new_print_solve_game = PrintSolveGame()
        self.new_test_sudoku = TestSudoku()
        self.str_sudoku = str_sudoku
        self.time = 0.0

    def resolve(self, sudoku):
        """
        this method resolves the sudoku game
        sudoku it is the sudoku matrix in order to be resolved
        """
        self.time = time.clock()
        max_rows = len(sudoku)
        max_col = max_rows
    
        """ we are going to start on [0, 0]"""
        pos = Position(max_rows, max_col)
    
        current_cell = []
        possibleCell = []
            
        while not pos.end_matrix():
            possibles = self.new_test_sudoku.try_sudoku(sudoku, current_cell, pos.get_row(), pos.get_col())
    
            while possibles == []:
                if pos.end_matrix():
                    """we arrived to end"""
                    self.new_print_solve_game.print_solve(sudoku, current_cell)
                    return True
                pos.next_position()
                possibles = self.new_test_sudoku.try_sudoku(sudoku, current_cell, pos.get_row(), pos.get_col())
    
            if possibles == [-1]:
                """ Backtracking """
                estado = current_cell.pop()
                while estado[0] != possibleCell[-1][0] or estado[1] != possibleCell[-1][1]:
                    estado = current_cell.pop()
                """now the last states for both have the same position"""
                current_cell.append(possibleCell.pop())
                
                """ we put the correct position """
                pos.set_row(current_cell[-1][0])
                pos.set_col(current_cell[-1][1])
            else:
                """
                here we have some possibles assertions
                we catch the first one and we have to input to the current_cell, and the rest in to possibleCell 
                """
                for possible in possibles[1:]:
                    possibleCell.append([pos.get_row(), pos.get_col(), possible])
    
                current_cell.append([pos.get_row(), pos.get_col(), possibles[0]])
    
            pos.next_position()
   
    def generate_matrix(self, row, col):
        """
        it generates a zero matrix
        row is the number of rows for the matrix
        col is the number of columns for the matrix
        """
        matrix = []
        for f in range(row):
            matrix.append([0] * col)
        return(matrix)

    def convert_str_to_matrix(self, str_to_convert, row, col):
        """
        it receives an string and it returns a matrix
        str_to_convert is an string in order to convert a matrix
        row it is the max row for the matrix
        col it is the max column for the matrix
        """
        matrix = self.generate_matrix(row, col)
        list_file = []
                
        for element in str_to_convert:
            list_file.append(int(element))
        
        cont_col = 0
        cont_row = 0
        pos_list_file = 0
        
        for i in list_file:
            if cont_col == 9:
                cont_row += 1
                cont_col = 0
                
            matrix[cont_row][cont_col] = list_file[pos_list_file]
            
            cont_col += 1
            pos_list_file += 1

        return(matrix)
    
    def get_solve_game(self):
        """
        it returns the sudoku solved game in a single string
        """
        return(self.new_print_solve_game.get_sudoku_resolved())
    
    def get_time(self):
        """
        it returns the time in order to get the sudoku resolution game.
        """
        return(self.new_print_solve_game.get_time() - self.time)

