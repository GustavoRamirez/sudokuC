import time
class PeterAlgorithm:
    def get_dictionary_keys(self, row_values, column_values):
        """ Function that elaborates a square by 9 x 9 using the
        row_values and column_values. Together they form the keys
        of the dictionary.E.g. A1, A2, A3

        Keyword arguments:
            row_values  -- receives string like: 'ABCDEFGHI'
            column_values -- receives string like: '123456789'
        """
        return [one_row + one_digit for one_row in row_values \
                for one_digit in column_values]

    def __init__(self):
        """ Constructor that defines parameters to develop the game.
        """
        self.time_solve = 0.0
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits
        self.squares  = self.get_dictionary_keys(self.rows, self.cols)
        self.unitlist = ([self.get_dictionary_keys(self.rows, column) for column in self.cols] +
                         [self.get_dictionary_keys(row, self.cols) for row in self.rows] +
                         [self.get_dictionary_keys(rs, cs) for rs in ('ABC','DEF','GHI') for cs in \
                         ('123','456','789')])
        self.units    = dict((square_value, [unit for unit in self.unitlist \
                        if square_value in unit]) for square_value in self.squares)
        self.peers    = dict((square_value, set(sum(self.units[square_value],[])) - set([square_value])) \
                        for square_value in self.squares)

    def get_parse_grid_in_dictionary(self, grid):
        """ Convert grid to a dict of possible values, {square: digits}, or
            return False if a contradiction is detected.

        Keyword arguments:
            grid --  receive the game unresolved as a string
        """
        values = dict((square_value, self.digits) for square_value in self.squares)
        for square_value, digit in self.get_grid_values(grid).items():
            if digit in self.digits and not self.get_values_solution(values, square_value, digit):
                return(False)
        return(values)

    def get_grid_values(self, grid):
        """ Convert grid into a dict of {square: char} with '0' or '.'
        for empties.

        Keyword arguments:
            grid -- receive the game as a string unresolved.
        """
        chars = [column for column in grid if column in self.digits or column in '0.']
        if len(chars) == 81:
            return(dict(zip(self.squares, chars)))

    def get_values_solution(self, values, square_value, digit):
        """ Eliminate all the other values (except digit) from values
        [square_value] and propagate. Return values, except return
        False if a contradiction is detected.

        Keyword arguments:
            values -- receive the dictionary with game unresolved. E.g. {'A1': '0', 'A2': '3'}
            square_value -- receive the key of the dictionary E.g. [A1, A2, A3....B1, B2]
            digit -- receive the digit which will be replaced in a key of
            the dictionary. E.g. 4
        """
        other_values = values[square_value].replace(digit, '')
        if all(self.get_eliminate_values(values, square_value, auxiliary_digit) \
               for auxiliary_digit in other_values):
            return(values)
        else:
            return(False)

    def get_digit_by_reviewing_squares (self, values, square_value, digit):
        """ Function that receives the dictionary with all digits, then moves through the
            dictionary checking if the value that has in digit can be set as a solution for
            the square.
            When set the value of digit, returns a True values to the get eliminate values function

            Keyword arguments:
            values -- receive the dictionary with game unresolved E.g. {'A1': '0', 'A2': '3'}
            square_value -- receive the key of the dictionary E.g. [A1, A2, A3....B1, B2]
            digit -- receive the digit which will be deleted in a key of the dictionary.
            E.g. 4
            """
        for unit in self.units[square_value]:
            row_complete_in_dictionary = [square_value for square_value in unit if digit\
                                         in values[square_value]]
            if len(row_complete_in_dictionary) == 0:
                return(False)
            elif len(row_complete_in_dictionary) == 1:
                if not self.get_values_solution(values, row_complete_in_dictionary[0], digit):
                    return(False)
        return True

    def get_eliminate_values(self, values, square_value, digit):
        """	Eliminate digit from values[square_value]; propagate when values
        or places <= 2. Return values, except return False if a contradiction
        is detected.

        Keyword arguments:
            values -- receive the dictionary with game unresolved E.g. {'A1': '0', 'A2': '3'}
            square_value -- receive the key of the dictionary E.g. [A1, A2, A3....B1, B2]
            digit -- receive the digit which will be deleted in a key of the dictionary. E.g. 4
            auxiliary_digit --  When the values has the last two digits, the auxiliary digit takes
                                the first value and call the get eliminate values function to see
                                what value is the solution and  prevent the square is saved with
                                empty value.
        """
        if digit not in values[square_value]:
            return(values)
        values[square_value] = values[square_value].replace(digit, '')
        if len(values[square_value]) == 1:
            auxiliary_digit = values[square_value]
            if not all(self.get_eliminate_values(values, square_value, auxiliary_digit) \
              for square_value in self.peers[square_value]):
                return(False)
            if not self.get_digit_by_reviewing_squares(values, square_value, digit):
                return False
        return values

    def get_solve (self, grid):
        """	Receive the get_game_solution function a grid, el grid the grid is
        transformed to dictionaries using the get_parse_grid_in_dictionary function
        and start searching the solution using depth - first search and
        propagation, try all possible values.
        When the solution is found the search function returns the variable
        values.This has the solution

        Keyword arguments:
             grid --  receive the game unresolved as a string
        """
        return self.search(self.get_parse_grid_in_dictionary(grid))

    def search(self, values):
        """	Using depth - first search and propagation, try all possible values.

        Keyword arguments:
            values -- receive the dictionary with game unresolved.
            E.g. {'A1': '0', 'A2': '3'}
        """
        if values is False:
            return(False)
        if all(len(values[square_value]) == 1 for square_value in self.squares):
            return(values)
        n,square_value = min((len(values[square_value]), square_value) \
        for square_value in self.squares if len(values[square_value]) > 1)
        return self.get_sequence_values(self.search(self.get_values_solution(values.copy(), \
                    square_value, digit))
                    for digit in values[square_value])

    def get_sequence_values (self, seq):
        """	Return some element of seq when is true.

        Keyword arguments:
            seq -- receives values from assing and search functions
        """
        for e in seq:
            if e: return(e)
        return False

    def get_game_solution (self, grid):
        """	Receive an game without resolve (variable grid), the grid is
        transformed to dictionaries and start a search  using depth - first
        search and propagation, try all possible values.
        Return the game solved in the puzzle_solved variable.

         Keyword arguments:
             grid --  receive the game unresolved as a string
        """
        puzzle_solved = ""
        start = time.clock()
        values = self.get_solve(grid)
        time_of_resolution = time.clock() - start
        self.time_solve = time_of_resolution
        puzzle_sort = sorted(dict.items(values))
        for individual_square_position in range (0, 81):
            value_individual_per_square = puzzle_sort[individual_square_position][1]
            puzzle_solved += str(value_individual_per_square)
        return(str(puzzle_solved))

    def get_time(self):
        """	Function that returns the time that a game has been solved by
        the algorithm.
        """
        return(self.time_solve)

