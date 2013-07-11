#Module 3/5:

class TestSudoku:
    def __init__(self):
        pass
    
    def prueba(self, sudoku, asignadas, row, col):
        LINEAS = len(sudoku)
        COLUMNAS = len(sudoku[0])
    
        if sudoku[row][col] != 0:
            return []
    
        else:
            result = []
    
            """ we tried all the possible numbers """
            for n in range(1,LINEAS+1):
    
                existe = False
    
                """we cover all the lines"""
                for l in range(0,LINEAS):
                    if sudoku[l][col] == n:
                        existe = True
                        break
                
                """we cover all the columns"""
                for c in range(0,COLUMNAS):
                    if sudoku[row][c] == n:
                        existe = True
                        break
                """look for assigned positions"""
                for asig in asignadas:
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
    
            return result


