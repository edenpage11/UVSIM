import unittest
from unittest.mock import patch
from io import StringIO
from tkinter import Tk
import gui2  # Assuming gui2 is the name of your GUI module

class TestGUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create an instance of the GUI for testing
        cls.app = gui2.Editor()
        cls.app.withdraw()  # Hide the GUI during tests

    @classmethod
    def tearDownClass(cls):
        # Destroy the GUI instance after all tests are done
        cls.app.destroy()

    def setUp(self):
        # Reset the GUI state before each test
        self.app.textbox.delete("1.0", "end")
        self.app.inputs = []

    @patch('builtins.input', side_effect=['1234'])  # Mock user input for testing
    def test_number_buttons(self, mock_input):
        # Simulate clicking number buttons
        for i in range(10):
            self.app.num_button_click(i)
        # Check if inputs are appended correctly
        self.assertEqual(self.app.inputs, list(range(10)))
        self.assertEqual(self.app.textbox.get("1.0", "end-1c"), '0123456789')

    def test_edit_buttons(self):
        # Simulate clicking edit buttons
        self.app.edit_button_click("Run")
        # Add more tests for other edit buttons

    def test_run_button(self):
        # Simulate clicking the Run button
        with patch.object(self.app, 'button_run') as mock_button_run:
            self.app.edit_button_click("Run")
            mock_button_run.assert_called_once()

    # Add similar methods for other test cases (Step In, Halt, Reset, Help, File Button, File Window Close)

if __name__ == '__main__':
    unittest.main()
