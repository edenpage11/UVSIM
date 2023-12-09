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
    
    # 0: Blake Adamson - Testing that GUI correctly displays title. Date:12/9
    # input: expected string // expected output: UVSIM code editor // p/f: p
    def test_title(self):
        title = self.app.winfo_toplevel().title()
        expected = 'UVSIM code editor'
        self.assertEqual(title, expected)
    
    # 0: Blake Adamson - Testing that number buttons get put in textbox. Date: 12/9
    # input: Clicking button "5" // expected output: Textbox insert called with "end" and "5" // p/f: p
    def test_num_button(self):
        with patch.object(self.app.textbox, "insert", MagicMock()) as mock_insert:
            self.app.num_button_click(5)
        mock_insert.assert_called_once_with("end", "5")

    # 0: Blake Adamson - Test that edit_button_clear method will clear inputs and textbox. Date: 12/9
    # input: Clicking "Clear"// expected output: Inputs list and textbox cleared // p/f: p
    def test_clear_button(self):
        self.app.num_button_click(3) # press 3
        self.app.edit_button_click("Clear") # press clear
        self.assertEqual(self.app.inputs, [])
        self.assertEqual(self.app.textbox.get("1.0", "end"), "\n")

    # 0: Blake Adamson - Test that edit_button_delete removes inputs. Date: 12/9
    # input: Clicking "Delete" // expected output: 12 // p/f: p
    def test_delete_button(self):
        self.app.inputs = [1, 2, 3]
        self.app.textbox.insert("end", "123")
        self.app.edit_button_click("Delete")
        self.assertEqual(self.app.inputs, [1, 2])
        self.assertEqual(self.app.textbox.get("1.0", "end"), "12\n")

    # 0: Blake Adamson - Test that "run" button calls "button_run" method once. Date: 12/9
    # input: Clicking "Run" // expected output: none // p/f: p
    def test_run_button(self):
        with patch.object(self.app, "button_run", MagicMock()) as mock_button_run:
            self.app.edit_button_click("Run")
        mock_button_run.assert_called_once()
    
    # 0: Blake Adamson - Testing that "help" calls iconify method and opens helper window. Date: 12/9
    # input: Clicking "Help" // expected output: window opened // p/f: p
    def test_help_button(self):
        with patch.object(self.app, "iconify", MagicMock()) as mock_iconify:
            with patch.object(gui2, "Helper", MagicMock()) as mock_helper:
                self.app.edit_button_click("Help")
        mock_iconify.assert_called_once()
        mock_helper.assert_called_once_with("helpEdit.txt", self.app)






if __name__ == '__main__':
    unittest.main() 