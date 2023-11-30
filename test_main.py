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

    
    
    # 04: Jia-Sian - Testing write raises an error when attempting to access an invalid memory location. date: 9/25
    # input: expected output: p/f:
    def test_write_error(self):
        with self.assertRaises(AssertionError):
            main.IOops.write(-1)

    # 05: Jia Sian-testing if the add can correctly add the positive numbers date: 9/25
    # input: expected output: p/f:
    def test_add_pos(self):
        main.memory[0] = 1234
        main.accumulator = 1234
        main.arithmetic.add(0)
        self.assertEqual(main.accumulator, 2468)

    # 06: Jia Sian-testing if the add can correctly add negative numbers together. date: 9/25
    # input: expected output: p/f:
    def test_add_neg(self):
        main.memory[0] = 1234
        main.accumulator = -5678
        main.arithmetic.add(0)
        self.assertEqual(main.accumulator, -4444)
    
    # 07: Jia Sian-testing if the add can correctly substract the positive numbers together. date: 9/25
    # input: expected output: p/f:
    def test_substract_pos(self):
        main.memory[0] = 1234
        main.accumulator = 3456
        main.arithmetic.substract(0)
        self.assertEqual(main.accumulator, 2222)

    # 08: Jia Sian-testing if the add can correctly substract the negative numbers together. date: 9/25
    # input: expected output: p/f:
    def test_substract_neg(self):
        main.accumulator = -5678
        main.memory[1] = -1234
        main.arithmetic.substract(1)
        self.assertEqual(main.accumulator, -4444)

    # 09: Bryceton Sudweeks - Testing if the divide function can accurately divide two positive numbers. date: 9/25
    # input: mem location 1 - 2222 accumulator - 4444 // expected output: 2
    def test_divide_pos(self):
        main.accumulator = 4444
        main.memory[1] = 2222
        main.arithmetic.divide(1)
        self.assertEqual(main.accumulator, 2)

    # 10: Bryceton Sudweeks - Testing if the divide function can accurately divide two negative numbers. date: 9/25
    # input: mem location 1 - 2222 accumulator - 4444 // expected output: 2
    def test_divide_neg(self):
        main.accumulator = -4444
        main.memory[1] = -2222
        main.arithmetic.divide(1)
        self.assertEqual(main.accumulator, 2)

    # 11: Bryceton Sudweeks - Testing if the multiply function can accurately multiply two positive numbers. date: 9/25
    # input: mem location 1 - 0002 accumulator - 800 // expected output: 1600
    def test_multiply_pos(self):
        main.accumulator = 4444
        main.memory[1] = 2
        main.arithmetic.multiply(1)
        self.assertEqual(main.accumulator, 8888)

    # 12: Bryceton Sudweeks - Testing if the multiply function can accurately multiply two negative numbers. date: 9/25
    # input: mem location - -0003 accumulator - -3333 // expected output: 9999
    def test_multiply_neg(self):
        main.accumulator = -3333
        main.memory[1] = -3
        main.arithmetic.multiply(1)
        self.assertEqual(main.accumulator, 9999)

    # 13: Eden Barlow - Testing if the load function loads the correct value from memory to the accumulator date: 9/25
    # input: 10 int // expected output: -5678 int // p/f: p
    def test_load_val(self):
        main.accumulator = 1234
        main.memory[10] = -5678

        main.LSops.load(10)
        self.assertEqual(main.accumulator, -5678)

    # 14: Eden Barlow - Testing load function that word is None if memory is empty date: 9/25
    # input: 10 int // expected output: None NoneType // p/f: p
    def test_load_no_val(self):
        main.accumulator = 1234

        main.LSops.load(10)
        self.assertEqual(main.accumulator, None)

    # 15: Eden Barlow - Testing store function that location in memory contains word from accumulator date: 9/25
    # input: 10 int // expected output: 1234 int // p/f: p
    def test_store_val(self):
        main.accumulator = 1234

        main.LSops.store(10)
        self.assertEqual(main.memory[10], 1234)

    # 16: Eden Barlow - Testing that location in memory == None if accumulator is empty date: 9/25
    # input: 10 int // expected output: None NoneType // p/f: p
    def test_store_no_val(self):
        main.accumulator = None
        main.LSops.store(10)
        self.assertEqual(main.memory[10], None)

    # 17: Blake-testing branch to negative. date:9/23
    # input:Memory address expected output:None p/f:Pass
    def test_branch_negative(self):
        main.BRops.branch(-5)
        self.assertEqual(main.program_counter,0)

    # 18: Blake- testing branch to positive. date: 9/25
    # input:Memory address expected output:None p/f:Pass
    def test_branch_positive(self):
        main.BRops.branch(10)
        self.assertEqual(main.program_counter,10)


    # 19: Blake-testing when accumulator is negative. date:9/23
    # input:Memory address expected output:None p/f:Pass
    def test_branchneg_neg(self):
        main.program_counter = 0
        main.accumulator = -5
        main.BRops.branchneg(10)
        self.assertEqual(main.program_counter,10)

    # 20: Blake-testing when accumulator is zero. date:9/25
    # input:Memory address expected output:None p/f:Pass
    def test_branchneg_zero(self):
        main.program_counter = 0
        main.accumulator = 0
        main.BRops.branchneg(5)
        self.assertEqual(main.program_counter, 0)


    # 21: Blake-testing when accumulator is 0. date:9/23
    # input: expected output: p/f:
    def test_branchzero_zero(self):
        main.program_counter = 0
        main.accumulator = 0 
        main.BRops.branchzero(10)
        self.assertEqual(main.program_counter, 10)

    # 22: Blake-testing when accumulator is negative. date:9/25
    # input:Memory address expected output:None p/f:Pass
    def test_branchzero_neg(self):
        main.program_counter = 0
        main.accumulator = -5
        main.BRops.branchzero(10)
        self.assertEqual(main.program_counter,0)
    
    def test_halt(self):
        #23: Bryce - testing the value of program_running pre halt. date:9/25
    #input: none // expected output: True !!!Getting False!!!
        self.assertEqual(main.program_running, True)

        #24: Bryce - testing the value of program_running post halt. date:9/25
    #input: none // expected output: False
        main.BRops.halt()
        self.assertEqual(main.program_running, False)
        

if __name__ == '__main__':
    unittest.main() 