#Module 1/5:

class Position:
    """It manage a position, and it controls the increase"""
    def __init__(self,maxrow,maxcol):
        self.maxrow = maxrow
        self.maxcol = maxcol
        self.row = 0
        self.col = 0

    def setRow(self, row):
        if row < 0:
            self.row = 0
        elif row >= self.maxrow:
            self.row = -1
        else:
            self.row = row

    def setCol(self, col):
        if col < 0:
            self.col = 0
        elif col >= self.maxcol:
            self.col = -1
        else:
            self.col = col

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def fin(self):
        return self.row == -1 and self.col == -1

    def reset(self):
        self.row = 0
        self.col = 0

    def sig(self):
        # Incrementa la posici?n controlando que no se pasa
        # del final.
        if not self.fin():
            self.col += 1
            if self.col == self.maxcol:
                self.col = 0
                self.row +=1
                if self.row == self.maxrow:
                    self.row = -1
                    self.col = -1

    def getPos(self):
        return [self.row, self.col]