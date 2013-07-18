'''
Created on Jul 07, 2013
@author: Rafael Alfaro
'''
import unittest
import recursive

class Testrecursive(unittest.TestCase):

    def setUp(self):
        self.board_easy = "040000700000700001005021006000800900600002003030005008301640000000050000006008200"
        self.board_hard = "094000130000000000000076002080010000032000000000200060000050400000008007006304008"
        self.board_easy_sl ="143586792862794351975321846214837965658912473739465128321649587487253619596178234"
        self.matrix = [['0', '4', '0', '0', '0', '0', '7', '0', '0'],
                       ['0', '0', '0', '7', '0', '0', '0', '0', '1'],
                       ['0', '0', '5', '0', '2', '1', '0', '0', '6'],
                       ['0', '0', '0', '8', '0', '0', '9', '0', '0'],
                       ['6', '0', '0', '0', '0', '2', '0', '0', '3'],
                       ['0', '3', '0', '0', '0', '5', '0', '0', '8'],
                       ['3', '0', '1', '6', '4', '0', '0', '0', '0'],
                       ['0', '0', '0', '0', '5', '0', '0', '0', '0'],
                       ['0', '0', '6', '0', '0', '8', '2', '0', '0']]

        self.matrix_sl = [['1', '4', '3', '5', '8', '6', '7', '9', '2'],
                          ['8', '6', '2', '7', '9', '4', '3', '5', '1'],
                          ['9', '7', '5', '3', '2', '1', '8', '4', '6'],
                          ['2', '1', '4', '8', '3', '7', '9', '6', '5'],
                          ['6', '5', '8', '9', '1', '2', '4', '7', '3'],
                          ['7', '3', '9', '4', '6', '5', '1', '2', '8'],
                          ['3', '2', '1', '6', '4', '9', '5', '8', '7'],
                          ['4', '8', '7', '2', '5', '3', '6', '1', '9'],
                          ['5', '9', '6', '1', '7', '8', '2', '3', '4']]



    def test_load_puzzle(self):
        sudoku = recursive.Recursive(self.board_easy)
        matrix_out = sudoku.load_puzzle(self.board_easy)
        self.assertEqual(self.matrix,matrix_out)


    def test_get_time(self):
        sudoku = recursive.Recursive(self.board_easy)
        time_review = sudoku.get_time()
        sudoku.solve_one_sudoku()
        self.assertNotEqual(time_review,sudoku.get_time())

    def test_get_original(self):
        sudoku = recursive.Recursive(self.board_easy)
        self.assertEqual(self.board_easy,sudoku.get_original())

    def test_solve_one_sudoku(self):
        sudoku = recursive.Recursive(self.board_easy)
        self.assertEqual(self.board_easy_sl,sudoku.solve_one_sudoku())

    def test_find_empty_position(self):
        sudoku = recursive.Recursive(self.board_easy)
        tupla = sudoku.find_empty_position(self.board_easy,'0')
        self.assertEqual((0,0),tupla)

    def test_matrix_to_string(self):
       sudoku = recursive.Recursive(self.board_easy)
       str_out = sudoku.matrix_to_string(self.matrix)
       self.assertEqual(self.board_easy,str_out)

    def test_get_solution(self):
      sudoku = recursive.Recursive(self.board_easy)
      sudoku.solve_one_sudoku()
      self.assertEqual(self.board_easy_sl,sudoku.get_solution())

    def test_solve(self):
        sudoku = recursive.Recursive(self.board_easy)
        solution = sudoku.solve(self.matrix,'0')
        self.assertEqual(solution,self.matrix_sl)

if __name__ == '__main__':
    unittest.main()
