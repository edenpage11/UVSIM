import unittest
from unittest.mock import patch, MagicMock
import gui2

class TestGui(unittest.TestCase):
    
    # sets up the app
    @patch("gui2.Editor.mainloop", return_value=None)
    def setUp(self, mock_mainloop):
        self.app = gui2.Editor()

    # destroys the app
    def tearDown(self):
        self.app.destroy()
    
    # 01: Blake Adamson - Testing that startup has correct title. Date:12/9
    # input: expected string // expected output: UVSIM code editor // p/f: p
    def test_title(self):
        title = self.app.winfo_toplevel().title()
        expected = 'UVSIM code editor'
        self.assertEqual(title, expected)
    
    # 01: Blake Adamson - Testing the num_button_click method. Date: 12/9
    # input: Clicking a number button (e.g., 5) // expected output: Textbox insert called with "end" and "5" // p/f: p
    def test_num_button_click(self):
        # Mock the textbox insert method to check if called with correct value
        with patch.object(self.app.textbox, "insert", MagicMock()) as mock_insert:
            self.app.num_button_click(5)
        # Assert that insert method called with expected args
        mock_insert.assert_called_once_with("end", "5")

if __name__ == '__main__':
    unittest.main() 