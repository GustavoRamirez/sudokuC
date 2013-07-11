#Module 2/5:
import time


class PrintSolveGame:
    def __init__(self):
        self.sudoku_resolved_string = ""
        self.time = 0.0
        
    
    def print_solve(self, sudoku, asignadas):
        """
        it generates the sudoku resolved string
        the commented variables in this method is in case we would like to print it from here
        sudoku is a sudoku matrix to be resolved
        """
        COLUMNAS = len(sudoku[0])
        barra = ""

        for i in range(0,COLUMNAS):
            barra += "?---"
        barra += "."
        
        #print barra
        cadena_temp= ""
        
        for row in range(0,len(sudoku)):
            cadena = ""
            for columna in range(0,len(sudoku)):
                if sudoku[row][columna] == 0:
                    encontrado = False
                    for a in asignadas:
                        if a[0] == row and a[1] == columna:
                            cadena += "| "+ str(a[2]) + " "
                            
                            encontrado = True
                    if not encontrado:
                        cadena += "|"+"   "
                else:
                    cadena += "| "+str(sudoku[row][columna])+" "
            cadena += "|"
            cadena_temp= cadena_temp+ cadena
            #print barra
        
        temp_list = ""
        
        for cad in cadena_temp:
            #print cad
            if cad == "|" or cad == " " or cad == "| " or cad == "   ":
                temp_list = temp_list + cad 
            else:
                self.sudoku_resolved_string = self.sudoku_resolved_string + cad
        self.time = time.clock()
        
    def get_sudoku_resolved(self):
        """it returns the sudoku resolved as a single string"""
        return self.sudoku_resolved_string
    
    def get_time(self):
        return self.time