import unittest
import sudokustr

class TestString(unittest.TestCase):

    def setUp(self):
        self.str_with_underscore = "34_6_______7_______2__8_57______5____7__1__2____4______36_2__1_______9_______7_82_\n"
        self.str_with_dots = ".2....5938..5..46.94..6...8..2.3.....6..8.73.7..2.........4.38..7....6..........5"
        self.str_with_zeros = "040050067000100040000200000100800300000000200060000000000040050300000800200000000"

    def test_get_length(self):
        size=len(self.str_with_dots)
        str_to_verify= sudokustr.SudokuStr(self.str_with_dots)
        self.assertEqual(size,str_to_verify.get_length())

    def test_verify_only_num_True(self):
        str_to_verify = sudokustr.SudokuStr(self.str_with_zeros)
        numbers = str_to_verify.verify_only_num()
        self.assertTrue(numbers)

    def test_verify_only_num_False(self):
        str_to_verify = sudokustr.SudokuStr(self.str_with_underscore)
        numbers = str_to_verify.verify_only_num()
        self.assertFalse(numbers)

    def test_get_81_characters(self):
        size=len(self.str_with_underscore)
        print(size)
        str_to_verify= sudokustr.SudokuStr(self.str_with_underscore)
        str_to_verify.get_81_characters()
        size_after = str_to_verify.get_81_characters()
        self.assertNotEqual(size,size_after)

    def test_get_zero_number(self):
        char = '0'
        str_to_verify = sudokustr.SudokuStr(self.str_with_zeros)
        numbers = str_to_verify.verify_only_num()
        zeros = self.str_with_zeros.count(char)
        self.assertEqual(zeros , str_to_verify.get_zero_number(char))

    def test_verify_string_to_sudoku(self):
        str_final = "340600000007000000020080570000005000070010020000400000036020010000000900000007082"
        str_to_verify = sudokustr.SudokuStr(self.str_with_underscore)
        str_to_verify.verify_string_to_sudoku()
        final_str = str_to_verify.get_str()
        self.assertEqual(str_final,final_str)

    def test_put_a_sring(self):
        str_final = "3406000000070000000200805700000050000700100200004000000360200100000009000000070"
        str_to_verify = sudokustr.SudokuStr()
        str_to_verify.put_a_sring(str_final)
        self.assertEqual(str_final, str_to_verify.get_str())


if __name__ == '__main__':
    unittest.main()
