'''
Created on Jul 07, 2013
@author: Rafael Alfaro
         Gustavo Ramirez
         Carla Munoz
'''
import recursive
import peter_algorithm
import sudokustr
from resolve import Resolve

class Solver:
    def __init__(self,puzzle):
        """
        This is the constructor of method
        """
        self.original = puzzle
        self.solution = ""
        self.execute = ""
        self.solve_time = 0.0
        self.file_of_output =""

    def human_string(self, puzzle):
        """
        This method returns a matrix in a format more understandable for human
        """
        line = " ------+-------+------ \n"
        cont = 0
        board = ""
        for i in range(len(puzzle)):
            if (cont == 3 or cont == 6):
                board = board + ' '
            cont += 1
            if cont == 1:
                board = board +' '
            board = board + puzzle[i] + ' '
            if cont == 9:
                board
                board = board +'\n'
                if (i == 26 or i == 53):
                    board = board + line
                cont = 0
            elif (str(cont) in '36'):board = board +'|'
        return board

#############################-Solver-##############################

    def solver(self,puzzle,algorithm):
        """
        This method uses the algorithm specified to solve the game
        """
        if(algorithm =="recursive"):
            board = sudokustr.SudokuStr(puzzle)
            if(board.verify_string_to_sudoku()):
                self.original = board.get_str()
                puzzle = board.get_str()
                recursivesk = recursive.Recursive(puzzle)
                self.solution=recursivesk.solve_one_sudoku()
                self.solve_time = recursivesk.get_time()
                print(self.human_string(self.solution))
                print self.solve_time

        elif (algorithm =="peter"):
            board = sudokustr.SudokuStr(puzzle)
            if(board.verify_string_to_sudoku()):
                self.original = board.get_str()
                puzzle = board.get_str()
                petersk = peter_algorithm.Peter_algorithm()
                self.solution = petersk.get_game_solution (puzzle)
                self.solve_time = petersk.get_time()
                print(self.human_string(self.solution))
                print self.solve_time


        elif (algorithm =="bactracking"):
            """
            This implements the backtrack algorithm in order to solve the game
            """
            board = sudokustr.SudokuStr(puzzle)
            if(board.verify_string_to_sudoku()):
                self.original = board.get_str()
                puzzle = board.get_str()

                bactrack = Resolve(puzzle)

                sudoku_matrix = bactrack.convert_str_to_matrix(puzzle, 9, 9)
                self.execute = bactrack.resolve(sudoku_matrix)
                self.solution = bactrack.get_solve_game()


                self.solve_time = bactrack.get_time()
                print(self.human_string(self.solution))
                print self.solve_time
        else:
            print ("Other algorithm")


print ""
print "----------------------"
print "RECURSIVE ALGORITHM"
print "----------------------"

board_easy = "040000700000700001005021006000800900600002003030005008301640000000050000006008200"

algorithm = "recursive"
sl = Solver(board_easy)
sl.solver(board_easy, algorithm)


print ""
print "----------------------"
print "PETER ALGORITHM"
print "----------------------"

algorithm = "peter"
s2 = Solver(board_easy)
s2.solver(board_easy, algorithm)


print ""
print "----------------------"
print "BACKTRAKING ALGORITHM"
print "----------------------"
board_easy_back = "273481960000075030048090100059300000367510809124968700001829576685734000092156384"
algorithm = "bactracking"

sl = Solver(board_easy_back)
sl.solver(board_easy_back, algorithm)
