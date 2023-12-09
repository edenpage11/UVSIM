import unittest
from unittest.mock import patch
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
    

if __name__ == '__main__':
    unittest.main() 