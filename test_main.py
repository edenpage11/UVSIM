import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestMain(unittest.TestCase):
    # Each test case should have a test case number,
    # short description, test date, inputs, expected outputs, 
    # pass/fail.
    # Each student needs to design 4-5 unit tests and put your 
    # name in the comments in the unit test case code.

    # 01: Eden Barlow - Testing read stores positive number in correct location in memory date: 11/30
    # input: '1234' string // expected output: 1234 int // p/f: p
    @patch('builtins.input', side_effect=['1234'])
    def test_read_pos(self, mock_input):
        test_read = main.IOops("1020")
        main.accumulator = '1234'
        test_read.run()
        self.assertEqual(main.memory[20], 1234)

    # 02: Eden Barlow - Testing read stores negative number in correct location in memory date: 11/30
    # input: '-1234' string // expected output: -1234 int // p/f: p
    @patch('builtins.input', side_effect=['-1234'])
    def test_read_neg(self, mock_input):
        test_read = main.IOops("1020")
        main.accumulator = '-1234'
        test_read.run()
        self.assertEqual(main.memory[20], -1234)

    # 03: Eden Barlow - testing if the function correctly prints out the positive value at specified memory location date: 11/30
    # input: 1234 int // expected output: 1234 int // p/f: p 
    def test_write_pos(self):
        # input: 1234 int
        main.memory[15] = 1234
        test_write = main.IOops('1115')
        test_write.run()
        # expected output: 1234 int
        self.assertEqual(main.memory[15], 1234)


    # 04: Eden Barlow - testing if the function correctly prints out the negative value at specified memory location date: 11/30
    # input: -1234 int // expected output: -1234 int // p/f: p
    def test_write_neg(self):
        # input: -1234 int
        main.memory[15] = -1234
        test_write = main.IOops('1115')
        test_write.run()
        # expected output: -1234 int
        self.assertEqual(main.memory[15], -1234)

    
    # 05: Eden Barlow - Testing write raises an error when attempting to access an invalid memory location. date: 9/25
    # input: none // expected output: AssertionError // p/f: p
    def test_write_error(self):
        # input: none
        test_write = main.IOops('11-1')
        with self.assertRaises(AssertionError):
            test_write.run()

    # 06: JiaSian/Blake - Testing if the add can add negative numbers together. date: 12/2
    # input: none // expected output: -4444 int // p/f: p
    def test_add_neg(self):
        # input: none
        main.memory[0] = 1234
        main.accumulator = -5678
        main.arithmetic("3000").run()
        # expected output: -4444 int
        self.assertEqual(main.accumulator, -4444)

    # 07: JiaSian/Blake - Test add can properly add the positive numbers date: 12/2
    # input: none // expected output: 2468 int // p/f: p
    def test_add_pos(self):
        # input: none
        main.memory[0] = 1234
        main.accumulator = 1234
        test_add = main.arithmetic('3000')
        test_add.run()  # Call the run method
        # expected output: 2468 int
        self.assertEqual(main.accumulator, 2468)

    # 08: JiaSian/Blake - Testing add can correctly subtract the negative numbers. date: 12/2
    # input: none // expected output: -4444 int // p/f: p
    def test_subtract_neg(self):
        # input: none
        main.accumulator = -5678
        main.memory[1] = -1234
        main.arithmetic("3101").run()  # Using run method
        # expected output: -4444 int
        self.assertEqual(main.accumulator, -4444)

    # 19: JiaSian/Blake - Testing if add can subtract the positive numbers. date: 12/2
    # input: none // expected output: 2222 int // p/f: p
    def test_subtract_pos(self):
        # input: none
        main.memory[0] = 1234
        main.accumulator = 3456
        main.arithmetic("3100").run()
        # expected output: 2222 int
        self.assertEqual(main.accumulator, 2222)

    # 10: Bryceton Sudweeks/Blake - Testing if divide function can accurately divide two positive numbers. date: 12/2
    # input: none // expected output: 2 int // p/f: p
    def test_divide_pos(self):
        # input: none
        main.accumulator = 4444
        main.memory[1] = 2222
        main.arithmetic("3201").run()
        # expected output: 2 int
        self.assertEqual(main.accumulator, 2)

    # 11: Bryceton Sudweeks /Blake - Testing if the divide function can accurately divide two negative numbers. date: 12/2
    # input: mem location 1 - 2222 accumulator - 4444 // expected output: 2
    def test_divide_neg(self):
        main.accumulator = -4444
        main.memory[1] = -2222
        main.arithmetic("3201").run()
        self.assertEqual(main.accumulator, 2)

    # 12: Bryceton Sudweeks /Blake - Testing if the multiply function can accurately multiply two positive numbers. date: 12/2
    # input: mem location 1 - 0002 accumulator - 800 // expected output: 1600
    def test_multiply_pos(self):
        main.accumulator = 4444
        main.memory[1] = 2
        main.arithmetic("3301").run()
        self.assertEqual(main.accumulator, 8888)

    # 13: Bryceton Sudweeks /Blake - Testing if the multiply function can accurately multiply two negative numbers. date: 12/2
    # input: mem location - -0003 accumulator - -3333 // expected output: 9999
    def test_multiply_neg(self):
        main.accumulator = -3333
        main.memory[1] = -3
        main.arithmetic("3301").run()
        self.assertEqual(main.accumulator, 9999)

    # 14: Eden Barlow - Testing if the load function loads the correct value from memory to the accumulator date: 12/3
    # input: 10 int // expected output: -5678 int // p/f: p
    def test_load_val(self):
        main.accumulator = None
        main.memory[10] = -5678
        main.LSops("2000").run()
        self.assertEqual(main.memory[10], -5678)

    # 15: Eden Barlow - Testing load function that word is None if memory is empty date: 12/3
    # input: 10 int // expected output: None NoneType // p/f: p
    def test_load_no_val(self):
        main.accumulator = 1234
        main.LSops("2000").run()
        self.assertEqual(main.memory[10], None)

    # 16: Eden Barlow - Testing store function that location in memory contains word from accumulator date: 12/3
    # input: 10 int // expected output: 1234 int // p/f: p
    def test_store_val(self):
        main.accumulator = 1234  # Set accumulator to the value
        main.LSops("2100").run()
        self.assertEqual(main.accumulator, 1234)

    # 17: Eden Barlow - Testing that location in memory == None if accumulator is empty date: 12/3
    # input: 10 int // expected output: None NoneType // p/f: p
    def test_store_no_val(self):
        main.accumulator = None
        main.LSops("2100").run()
        self.assertEqual(main.accumulator, None)

    # 18: Blake - testing branch to negative. date: 12/2
    # input: none // expected output: 0 int // p/f: p
    def test_branch_negative(self):
        # input: none
        main.BRops("4000").run()
        # expected output: 0 int
        self.assertEqual(main.program_counter, 0)

    # 19: Blake - testing branch to positive. date: 12/2
    # input: none // expected output: 1 int // p/f: p
    def test_branch_positive(self):
        # input: none
        main.BRops("4001").run()
        # expected output: 1 int
        self.assertEqual(main.program_counter, 1)

    # 20: Blake - testing when accumulator is negative. date: 12/2
    # input: none // expected output: 1 int // p/f: p
    def test_branchneg_neg(self):
        # input: none
        main.program_counter = 0
        main.accumulator = -5
        main.BRops("4101").run()
        # expected output: 1 int
        self.assertEqual(main.program_counter, 1)

    # 21: Blake - testing when accumulator is zero. date: 12/2
    # input: none // expected output: 0 int // p/f: p
    def test_branchzero_zero(self):
        # input: none
        main.program_counter = 0
        main.accumulator = 0
        main.BRops("4105").run()
        # expected output: 0 int
        self.assertEqual(main.program_counter, 0) 

    # 22: Blake - testing when accumulator is 0. date: 12/2
    # input: none // expected output: 1 int // p/f: p
    def test_branchzero_zero_nonz(self):
        # input: none
        main.program_counter = 0
        main.accumulator = 0
        main.BRops("4201").run()
        # expected output: 1 int
        self.assertEqual(main.program_counter, 1)

    # 23: Bryce/Blake - testing the value of program_running pre halt. date: 12/2
    # input: none // expected output: True // p/f: p
    def test_pre_halt(self):
        # input: none
        main.program_running = True
        # expected output: True
        self.assertEqual(main.program_running, True)

    # 24: Bryce/Blake - testing the value of program_running post halt. date:12/3
    # input: none // expected output: False // p/f: p
    def test_post_halt(self):
        # input: none
        test_instance = main.BRops(word='0000')
        test_instance.halt()
        # expected output: False
        self.assertEqual(main.program_running, False)

if __name__ == '__main__':
    unittest.main() 