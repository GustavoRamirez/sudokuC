import time
class PrintSolveGame:
    def __init__(self):
        self.sudoku_resolved_string = ""
        self.time = 0.0
    
    def print_solve(self, sudoku, asignadas):
        """
        it generates the sudoku resolved string
        The commented variables in this method are in case we would like to print the resolved 
        sudoku directly to the console
        sudoku is a sudoku matrix to be resolved
        """
        max_col = len(sudoku[0])
        bar = ""

        for i in range(0,max_col):
            bar += "?---"
        bar += "."
        string_temp = ""
        
        for row in range(0, len(sudoku)):
            string_to_print = ""
            for columna in range(0, len(sudoku)):
                if sudoku[row][columna] == 0:
                    encontrado = False
                    for a in asignadas:
                        if a[0] == row and a[1] == columna:
                            string_to_print += "| "+ str(a[2]) + " "
                            
                            encontrado = True
                    if not encontrado:
                        string_to_print += "|"+"   "
                else:
                    string_to_print += "| "+str(sudoku[row][columna])+" "
            string_to_print += "|"
            string_temp = string_temp+ string_to_print
        temp_list = ""
        
        for cad in string_temp:
            if cad == "|" or cad == " " or cad == "| " or cad == "   ":
                temp_list = temp_list + cad 
            else:
                self.sudoku_resolved_string = self.sudoku_resolved_string + cad
        self.time = time.clock()
        
    def get_sudoku_resolved(self):
        """
        it returns the sudoku resolved as a single string
        """
        return self.sudoku_resolved_string
    
    def get_time(self):
        """
        it returns the time
        """
        return(self.time)