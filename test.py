import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestMain(unittest.TestCase):
    #Each test case should have a test case number,
    # short description, test date, inputs, expected outputs, 
    # pass/ fail.
    #Each student needs to design 4-5 unit tests and put your 
    # name in the comments in the unit test case code.


    # 01: Eden Barlow - Testing read stores positive number in correct location in memory date: 11/30
    # input: '1234' string // expected output: 1234 int // p/f: p
    @patch('builtins.input', side_effect=['1234'])
    def test_read_pos(self, mock_input):
        test_read = main.IOops("1020")
        test_read.run()
        self.assertEqual(main.memory[20], 1234)

    # 02: Eden Barlow - Testing read stores negative number in correct location in memory date: 11/30
    # input: '-1234' string // expected output: -1234 int // p/f: p
    @patch('builtins.input', side_effect=['-1234'])
    def test_read_neg(self, mock_input):
        test_read = main.IOops("1020")
        test_read.run()
        self.assertEqual(main.memory[20], -1234)

    # 03: Eden Barlow - Testing read throws error when NaN input  11/30
    # input: 'hello' string // expected output: '-----Error:Only input numbers, Try again.-----' // p/f: p
    @patch('builtins.input', side_effect=['hello'])
    def test_read_bad(self, mock_input):
        test_read = main.IOops("1020")
        print(test_read)
        with patch('sys.stdout', new_callable= StringIO) as mock_stdout:
            test_read.run()
        self.assertEqual(mock_stdout.getvalue().strip(), '-----Error:Only input numbers, Try again.-----')
        

if __name__ == '__main__':
    unittest.main() 