import time
class peter_norving_algoritmo:
    """Cross product of elements in A and elements in B."""
    def cross(self, A, B):
        return [a+b for a in A for b in B]

    def __init__(self):
        """Constructor that defines parameters to develop the game."""
        self.time_solve = 0.0
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits
        self.squares  = self.cross(self.rows,self.cols)
        self.unitlist = ([self.cross(self.rows, c) for c in self.cols] +
                          [self.cross(r, self.cols) for r in self.rows] +
                          [self.cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
        self.units = dict((s, [u for u in self.unitlist if s in u])
                        for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s],[]))-set([s]))
                        for s in self.squares)

    def parse_grid(self, grid):
        """Convert grid to a dict of possible values, {square: digits}, or
            return False if a contradiction is detected."""
        values = dict((s, self.digits) for s in self.squares)
        for s,d in self.grid_values(grid).items():
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values

    def grid_values(self, grid):
        """Convert grid into a dict of {square: char} with '0' or '.'
        for empties."""
        chars = [c for c in grid if c in self.digits or c in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    def assign(self, values, s, d):
        """Eliminate all the other values (except d) from values[s] and
        propagate. Return values, except return False if a contradiction
         is detected."""
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False

    def eliminate(self, values, s, d):
        """Eliminate d from values[s]; propagate when values or places <= 2.
         Return values, except return False if a contradiction is detected."""
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d,'')
        if len(values[s]) == 0:
            return False
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False
        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.assign(values, dplaces[0], d):
                    return False
        return values

    def display(self, values):
        """Displays a square of 9 x 9 and the values the sudoku.
        These values can be an unsolved game or a game resolved."""
        width = 1+max(len(values[s]) for s in self.squares)
        line = '+'.join(['-'*(width*3)]*3)
        for r in self.rows:
            print ''.join(values[r+c].center(width)+('|' if c in '36' else '')
                          for c in self.cols)
            if r in 'CF': print line

    def solve(self, grid):
        """Receive a grid and resolves the game"""
        return self.search(self.parse_grid(grid))

    def search(self, values):
        """Using depth-first search and propagation, try all possible values."""
        if values is False:
            return False
        if all(len(values[s]) == 1 for s in self.squares):
            return values
        n,s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return self.some(self.search(self.assign(values.copy(), s, d))
                    for d in values[s])

    def some(self, seq):
        for e in seq:
            if e: return e
        return False

    def from_grid(self, value_grid):
        """Parse a grid and adds the separator of nine characters."""
        size = len (value_grid)
        cont = 9
        str_final =""
        for i in range(size):
            if i == cont:
                str_final+= '\n'
                cont +=9
            str_final+=value_grid[i]
        str_final += '\n'
        return str_final

    def resolvedor(self,grid):
        """Solve the game, displays the time resolution and returns the
           resolution in a string."""
        puzzle_solved = ""
        start = time.clock()
        values = self.solve(grid)
        tiempo_resolucion = time.clock()-start
        self.time_solve = tiempo_resolucion
        puzzle_ordenado = sorted(dict.items(values))
        for x in range (0,81):
            solucion_x_casilla = puzzle_ordenado[x][1]
            puzzle_solved += str(solucion_x_casilla)
        return str(puzzle_solved)

    def get_time(self):
        return self.time_solve

