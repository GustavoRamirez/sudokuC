import unittest
from position import Position
from resolve import Resolve


class UnitTestBacktrak(unittest.TestCase):

    def setUp(self):
        self.max_col = 9
        self.max_row = 9
        self.col = 0
        self.row = 0
        self.new_position = Position(self.max_row,self.max_col)

        self.sudoku_str = "273481960000075030048090100059300000367510809124968700001829576685734000092156384"
        self.sudoku_resolved_to_compare = "273481965916275438548693127859347612367512849124968753431829576685734291792156384"
        list_for_matrix = [0] * self.max_col
        self.zero_matrix = [list_for_matrix] * self.max_row
        self.sudoku_matrix = [[2, 7, 3, 4, 8, 1, 9, 6, 0], [0, 0, 0, 0, 7, 5, 0, 3, 0], [0, 4, 8, 0, 9, 0, 1, 0, 0],
                              [0, 5, 9, 3, 0, 0, 0, 0, 0], [3, 6, 7, 5, 1, 0, 8, 0, 9], [1, 2, 4, 9, 6, 8, 7, 0, 0],
                              [0, 0, 1, 8, 2, 9, 5, 7, 6], [6, 8, 5, 7, 3, 4, 0, 0, 0], [0, 9, 2, 1, 5, 6, 3, 8, 4]]
        self.new_resolve = Resolve(self.sudoku_str)

    def test_verify_it_can_set_row(self):
        self.new_position.setRow(4)
        self.assertEqual(4,self.new_position.getRow())


    def test_verify_it_can_set_row_equal_to_0_if_it_is_minor_to_0(self):
        self.new_position.setRow(-1)
        self.assertEqual(0,self.new_position.getRow())

    def test_verify_it_cat_set_row_equal_to_minus_1_if_it_is_mayor_to_max_row(self):
        self.new_position.setRow(11)
        self.assertEqual(-1,self.new_position.getRow())

    def test_verify_it_can_set_col(self):
        self.new_position.setCol(5)
        self.assertEqual(5,self.new_position.getCol())

    def test_verify_it_can_set_col_equal_to_0_if_it_is_minor_to_0(self):
        self.new_position.setCol(-2)
        self.assertEqual(0,self.new_position.getCol())

    def test_verify_it_cat_set_col_equal_to_minus_1_if_it_is_mayor_to_max_col(self):
        self.new_position.setCol(20)
        self.assertEqual(-1,self.new_position.getCol())

    def test_verify_it_can_get_row(self):
        self.new_position.setRow(8)
        self.assertEqual(8,self.new_position.getRow())

    def test_verify_it_can_get_col(self):
        self.new_position.setCol(4)
        self.assertEqual(4,self.new_position.getCol())

    def test_verify_it_is_end_of_the_matrix_it_should_return_minus_1(self):
        self.new_position.setRow(self.max_col)
        self.new_position.setCol(self.max_row)
        self.assertTrue(self.new_position.end_matrix())

    def test_verify_it_can_reset_to_zero_the_row_and_col(self):
        self.new_position.reset()
        self.assertEqual(0,self.new_position.getCol())
        self.assertEqual(0,self.new_position.getRow())

    def test_verify_it_can_move_to_next_vale_of_a_matrix(self):
        """
        if initial position is row = 0, col = 1
        the next position should be row = 0, col = 2
        """
        self.new_position.setRow(0)
        self.new_position.setCol(1)
        self.new_position.sig()
        self.assertEqual(0,self.new_position.getRow())
        self.assertEqual(2,self.new_position.getCol())

    def test_verify_it_can_not_move__next_row_if_it_is_mayor_to_max_row(self):
        self.new_position.setRow(self.max_row + 1)
        self.new_position.sig()
        self.assertEqual(-1,self.new_position.getRow())

    def test_verify_it_can_move_to_next_col_if_it_is_mayor_to_max_col(self):
        self.new_position.setCol(self.max_col + 1)
        self.new_position.sig()
        self.assertEqual(0,self.new_position.getCol())

    def test_verify_it_can_not_move_to_next_value_if_it_is_end_of_the_matrix(self):
        self.new_position.setRow(self.max_row)
        self.new_position.setCol(self.max_col)
        self.new_position.sig()
        self.assertTrue(self.new_position.end_matrix())

    def test_verify_it_can_get_a_position_of_a_matrix(self):
        self.new_position.setRow(3)
        self.new_position.setCol(3)
        self.assertEqual([3,3],self.new_position.getPos())

    def test_verify_it_could_resolve_a_sudoku(self):
        self.new_resolve.resolve(self.sudoku_matrix)
        self.assertEqual(self.sudoku_resolved_to_compare,self.new_resolve.get_solve_game())

    def test_verify_it_could_generate_a_zero_matrix(self):
        self.assertEqual(self.zero_matrix, self.new_resolve.generate_matrix(self.max_row, self.max_col))

    def test_verify_it_could_convert_an_string_to_a_matrix(self):
        self.assertEqual(self.sudoku_matrix, self.new_resolve.convert_str_to_matrix(self.sudoku_str, self.max_row, self.max_col))


if __name__ == '__main__':
    unittest.main()