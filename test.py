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

    # 05: Eden Barlow - testing if the function correctly prints out the negative value at specified memory location date: 11/30
    # input: -1234 int // expected output: -1234 str // p/f: p
    def test_write_neg(self):
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

    # 07: JiaSian/Blake - Testing if the add can add negative numbers together. date: 12/2
    # input: expected output: p/f:
    def test_add_neg(self):
        main.memory[0] = 1234
        main.accumulator = -5678
        main.arithmetic("3000").run()
        self.assertEqual(main.accumulator, -4444)

    # 08: JiaSian/Blake - Test add can properly add the positive numbers date: 12/2
    # input: expected output: p/f:
    def test_add_pos(self):
        main.memory[0] = 1234
        main.accumulator = 1234
        test_add = main.arithmetic('3000')
        test_add.run()  # Call the run method
        self.assertEqual(main.accumulator, 2468)

    # 09: JiaSian/Blake - Testing add can correctly subtract the negative numbers. date: 12/2
    # input: expected output: p/f:
    def test_subtract_neg(self):
        main.accumulator = -5678
        main.memory[1] = -1234
        main.arithmetic("3101").run()  # Using run method
        self.assertEqual(main.accumulator, -4444)

    # 010: JiaSian/Blake - Testing if add can subtract the positive numbers. date: 12/2
    # input: expected output: p/f:
    def test_subtract_pos(self):
        main.memory[0] = 1234
        main.accumulator = 3456
        main.arithmetic("3100").run()
        self.assertEqual(main.accumulator, 2222)

    # 11: Bryceton Sudweeks/Blake - Testing if divide function can accurately divide two positive numbers. date: 12/2
    # input: mem location 1 - 2222 accumulator - 4444 // expected output: 2
    def test_divide_pos(self):
        main.accumulator = 4444
        main.memory[1] = 2222
        main.arithmetic("3201").run()
        self.assertEqual(main.accumulator, 2)

    # 12: Bryceton Sudweeks /Blake - Testing if the divide function can accurately divide two negative numbers. date: 12/2
    # input: mem location 1 - 2222 accumulator - 4444 // expected output: 2
    def test_divide_neg(self):
        main.accumulator = -4444
        main.memory[1] = -2222
        main.arithmetic("3201").run()
        self.assertEqual(main.accumulator, 2)

    # 13: Bryceton Sudweeks /Blake - Testing if the multiply function can accurately multiply two positive numbers. date: 12/2
    # input: mem location 1 - 0002 accumulator - 800 // expected output: 1600
    def test_multiply_pos(self):
        main.accumulator = 4444
        main.memory[1] = 2
        main.arithmetic("3301").run()
        self.assertEqual(main.accumulator, 8888)

    # 14: Bryceton Sudweeks /Blake - Testing if the multiply function can accurately multiply two negative numbers. date: 12/2
    # input: mem location - -0003 accumulator - -3333 // expected output: 9999
    def test_multiply_neg(self):
        main.accumulator = -3333
        main.memory[1] = -3
        main.arithmetic("3301").run()
        self.assertEqual(main.accumulator, 9999)

    ##############################################################################
    # 15: Eden Barlow - Testing if the load function loads the correct value from memory to the accumulator date: 12/2
    # input: 10 int // expected output: -5678 int // p/f: 
    def test_load_val(self):
        main.accumulator = None
        main.memory[10] = -5678

        main.LSops("2000").run()
        self.assertEqual(main.accumulator, -5678)

    # 16: Eden Barlow - Testing load function that word is None if memory is empty date: 12/2
    # input: 10 int // expected output: None NoneType // p/f: 
    def test_load_no_val(self):
        main.accumulator = 1234

        main.LSops("2000").run()
        self.assertEqual(main.accumulator, None)

    # 17: Eden Barlow - Testing store function that location in memory contains word from accumulator date: 12/2
    # input: 10 int // expected output: 1234 int // p/f: 
    def test_store_val(self):
        main.accumulator = 1234

        main.LSops("2100").run()
        self.assertEqual(main.memory[10], 1234)

    # 18: Eden Barlow /Blake - Testing that location in memory == None if accumulator is empty date: 12/2
    # input: 10 int // expected output: None NoneType // p/f: 
    def test_store_no_val(self):
        main.accumulator = None
        main.LSops("2100").run()
        self.assertEqual(main.memory[10], None)
    ##################################################################################

    # 19: Blake - testing branch to negative. date: 12/2
    # input: Memory address expected output: None p/f: Pass
    def test_branch_negative(self):
        main.BRops("4000").run()
        self.assertEqual(main.program_counter, 0)

    # 20: Blake - testing branch to positive. date: 12/2
    # input: Memory address expected output: None p/f: Pass
    def test_branch_positive(self):
        main.BRops("4001").run()
        self.assertEqual(main.program_counter, 1)

    # 21: Blake - testing when accumulator is negative. date: 12/2
    # input: Memory address expected output: None p/f: Pass
    def test_branchneg_neg(self):
        main.program_counter = 0
        main.accumulator = -5
        main.BRops("4101").run()
        self.assertEqual(main.program_counter, 1)

    ##############
    # 22: Blake - testing when accumulator is zero. date: 12/2
    # input: Memory address expected output: None p/f: Pass
    def test_branchneg_zero(self):
        main.program_counter = 0
        main.accumulator = 0
        main.BRops("4105").run()
        self.assertEqual(main.program_counter, 5)

    # 23: Blake - testing when accumulator is 0. date: 12/2
    # input: expected output: p/f:
    def test_branchzero_zero(self):
        main.program_counter = 0
        main.accumulator = 0
        main.BRops("4201").run()
        self.assertEqual(main.program_counter, 1)



    # 24: Bryce - testing the value of program_running pre halt. date: 12/2
    # input: none // expected output: True
    def test_pre_halt(self):
        self.assertEqual(main.program_running, True)

    # 25: Bryce - testing the value of program_running post halt. date: 12/2
    # input: none // expected output: False
    def test_post_halt(self):
        main.program_running = True  # Reset program_running to True before testing
        main.BRops().halt()
        self.assertEqual(main.program_running, False)


if __name__ == '__main__':
    unittest.main() 