#Module 4/5: 
 
from test_sudoku import TestSudoku
from print_solve_game import PrintSolveGame
from position import Position
import time


class Resolve:
    def __init__(self,str_sudoku):
        self.new_print_solve_game = PrintSolveGame()
        self.new_test_sudoku = TestSudoku()
        self.str_sudoku = str_sudoku
        self.time = 0.0
        pass

    def resolve(self,sudoku):
        self.time = time.clock()
        MAXLINEAS = len(sudoku)
        MAXCOLS = MAXLINEAS
    
        """ we are going to start on [0,0]"""
        pos = Position(MAXLINEAS,MAXCOLS)
    
        currentCell = []
        possibleCell = []
            
        while not pos.fin():
            posibles = self.new_test_sudoku.prueba(sudoku,currentCell,pos.getRow(),pos.getCol())
    
            while posibles == []:
                if pos.fin():
                    """we arrived to end"""
                    self.new_print_solve_game.print_solve(sudoku, currentCell)
                    return True
                pos.sig()
                posibles = self.new_test_sudoku.prueba(sudoku,currentCell,pos.getRow(),pos.getCol())
    
            if posibles == [-1]:
                """ Backtracking """
                estado = currentCell.pop()
                while estado[0] != possibleCell[-1][0] or estado[1] != possibleCell[-1][1]:
                    estado = currentCell.pop()
                """now the last states for both have the same position"""
                currentCell.append(possibleCell.pop())
                
                """ we put the correct position """
                pos.setRow(currentCell[-1][0])
                pos.setCol(currentCell[-1][1])
            else:
                """
                here we have some possibles assertions
                we catch the first one and we have to input to the currentCell, and the rest in to possibleCell 
                """
                for posible in posibles[1:]:
                    possibleCell.append([pos.getRow(),pos.getCol(),posible])
    
                currentCell.append([pos.getRow(),pos.getCol(),posibles[0]])
    
            pos.sig()
   
    def generate_matrix(self,row,col):
        matrix = []
        for f in range(row):
            matrix.append([0] * col)
        return matrix

    def convert_str_to_matrix(self,str_to_convert,row,col):
        matrix = self.generate_matrix(row, col)
        lista_file = []
                
        for element in str_to_convert:
            lista_file.append(int(element))
        
        cont_col = 0
        cont_row = 0
        pos_list_file = 0
        
        for i in lista_file:
            if cont_col == 9:
                cont_row +=1
                cont_col = 0
                
            matrix[cont_row][cont_col] = lista_file[pos_list_file]
            
            cont_col += 1
            pos_list_file += 1

        return matrix
    
    def get_solve_game(self):
        return self.new_print_solve_game.get_sudoku_resolved()
    
    def get_time(self):
        return self.new_print_solve_game.get_time() - self.time

