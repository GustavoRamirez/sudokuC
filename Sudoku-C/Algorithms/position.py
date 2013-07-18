class Position:
    """
    It manage a position, and it controls the increase
    """
    def __init__(self, max_row, max_col):
        self.max_row = max_row
        self.max_col = max_col
        self.row = 0
        self.col = 0

    def set_row(self, row):
        """
        it set a row
        row is a variable in order to set the new row
        """
        if row < 0:
            self.row = 0
        elif row >= self.max_row:
            self.row = -1
        else:
            self.row = row

    def set_col(self, col):
        """
        it set a column
        col is a variable in order to set the new column
        """
        if col < 0:
            self.col = 0
        elif col >= self.max_col:
            self.col = -1
        else:
            self.col = col

    def get_row(self):
        """
        it returns the current row
        """
        return self.row

    def get_col(self):
        """
        it returns the current column
        """
        return self.col

    def end_matrix(self):
        """
        it verifies the end of the matrix, it means it could not pass the 
        max row and max column
        """
        return self.row == -1 and self.col == -1

    def reset(self):
        """
        it reset the row to zero and column to zero
        """
        self.row = 0
        self.col = 0

    def next_position(self):
        """
        it increase the position in order to go next position
        but it should not be more than end max_row and end max_col
        """
        if not self.end_matrix():
            self.col += 1
            if self.col == self.max_col:
                self.col = 0
                self.row += 1
                if self.row == self.max_row:
                    self.row = -1
                    self.col = -1

    def get_position(self):
        """
        it returns the current position
        """
        return([self.row, self.col])