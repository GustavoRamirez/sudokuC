import unittest
import stringsk

class TestString(unittest.TestCase):

    def setUp(self):
        self.string1 = "34_6_______7_______2__8_57______5____7__1__2____4______36_2__1_______9_______7_82_\n"
        self.string2 = ".2....5938..5..46.94..6...8..2.3.....6..8.73.7..2.........4.38..7....6..........5"
        self.string3 = "040050067000100040000200000100800300000000200060000000000040050300000800200000000"

    def test_get_length(self):
        size=len(self.string2)
        str2= stringsk.Stringsk(self.string2)
        self.assertEqual(size,str2.get_length())

    def test_verify_only_num_True(self):
        str2 = stringsk.Stringsk(self.string3)
        numbers = str2.verify_only_num()
        self.assertTrue(numbers)

    def test_verify_only_num_False(self):
        str2 = stringsk.Stringsk(self.string1)
        numbers = str2.verify_only_num()
        self.assertFalse(numbers)

    def test_get_81_characters(self):
        size=len(self.string1)
        print (size)
        str2= stringsk.Stringsk(self.string1)
        str2.get_81_characters()
        size_after = str2.get_81_characters()
        self.assertNotEqual(size,size_after)

    def test_get_zero_number(self):
        char = '0'
        str2 = stringsk.Stringsk(self.string3)
        numbers = str2.verify_only_num()
        zeros = self.string3.count(char)
        self.assertEqual(zeros , str2.get_zero_number(char))

    def test_verify_string_to_sudoku(self):
        str_final = "340600000007000000020080570000005000070010020000400000036020010000000900000007082"
        str2 = stringsk.Stringsk(self.string1)
        str2.verify_string_to_sudoku()
        final_str = str2.get_str()
        self.assertEqual(str_final,final_str)

if __name__ == '__main__':
    unittest.main()
