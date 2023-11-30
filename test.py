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
    @patch('builtins.input', side_effect=['hello', '1234'])
    def test_read_bad(self, mock_input):
        test_read = main.IOops("1020")
        with patch('sys.stdout', new_callable= StringIO) as mock_stdout:
            test_read.run()
        self.assertEqual(mock_stdout.getvalue().strip(), '-----Error:Only input numbers, Try again.-----')

    # 04: Eden Barlow - testing if the function correctly prints out the positive value at specified memory location date: 11/30
    # input: 1234 int // expected output: 1234 str // p/f: p 
    def test_write_pos(self):
        main.memory[15] = 1234
        test_write = main.IOops('1115')
        with patch('sys.stdout', new_callable= StringIO) as mock_stdout:
            test_write.run()
        self.assertEqual(mock_stdout.getvalue().strip(), '1234')

    # 05: Eden Barlow - testing if the function correctly prints out the positive value at specified memory location date: 11/30
    # input: -1234 int // expected output: -1234 str // p/f: p
    def test_write_pos(self):
        main.memory[15] = -1234
        test_write = main.IOops('1115')
        with patch('sys.stdout', new_callable= StringIO) as mock_stdout:
            test_write.run()
        self.assertEqual(mock_stdout.getvalue().strip(), '-1234')
    
    # 06: Eden Barlow - Testing write raises an error when attempting to access an invalid memory location. date: 9/25
    # input: expected output: p/f:
    def test_write_error(self):
        test_write = main.IOops('11-1')
        with self.assertRaises(AssertionError):
            test_write.run()
        

if __name__ == '__main__':
    unittest.main() 