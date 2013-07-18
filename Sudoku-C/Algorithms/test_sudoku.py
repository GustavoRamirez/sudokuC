class TestSudoku:
    def __init__(self):
        pass
    
    def try_sudoku(self, sudoku, assigned, row, col):
        """
        it test the sudoku matrix trying the possible 
        sudoku it is a sudoku matrix that it is going to be resolved
        assigned it is a variable that contain the possible numbers in order to resolve the sudoku
        row is a position row for the matrix
        col is a position column for the matrix
        """
        rows = len(sudoku)
        cols = len(sudoku[0])
    
        if sudoku[row][col] != 0:
            return([])
    
        else:
            result = []
    
            """ we tried all the possible numbers """
            for n in range(1, rows+1):
    
                existe = False
    
                """we cover all the lines"""
                for l in range(0, rows):
                    if sudoku[l][col] == n:
                        existe = True
                        break
                
                """we cover all the columns"""
                for c in range(0, cols):
                    if sudoku[row][c] == n:
                        existe = True
                        break
                """look for assigned positions"""
                for asig in assigned:
                    if asig[0] == row and asig[2] == n:
                        existe = True
                        break
                    if asig[1] == col and asig[2] == n:
                        existe = True
                        break
    
                if not existe:
                    result.append(n)
    
            if result == []:
                """end way"""
                result = [-1]
    
            return(result)


