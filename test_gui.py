import unittest
from unittest.mock import patch, MagicMock
import gui
import main

class TestGui(unittest.TestCase):
    
    # sets up the app
    @patch("gui.Editor.mainloop", return_value=None)
    def setUp(self, mock_mainloop):
        self.app = gui.Editor()

    # destroys the app
    def tearDown(self):
        self.app.destroy()
    
    # 26: Blake Adamson - Testing that number buttons get put in textbox. Date: 12/9
    # input: Clicking button "5" // expected output: Textbox insert called with "end" and "5" // p/f: p
    def test_num_button(self):
        with patch.object(self.app.textbox, "insert", MagicMock()) as mock_insert:
            self.app.num_button_click(5)
        mock_insert.assert_called_once_with("end", "5")

    # 27: Blake Adamson - Test that edit_button_clear method will clear inputs and textbox. Date: 12/9
    # input: Clicking "Clear"// expected output: Inputs list and textbox cleared // p/f: p
    def test_clear_button(self):
        self.app.num_button_click(3) # press 3
        self.app.edit_button_click("Clear") # press clear
        self.assertEqual(self.app.inputs, [])
        self.assertEqual(self.app.textbox.get("1.0", "end"), "\n")

    # 28: Blake Adamson - Test that edit_button_delete removes inputs. Date: 12/9
    # input: Clicking "Delete" // expected output: 12 // p/f: p
    def test_delete_button(self):
        self.app.inputs = [1, 2, 3]
        self.app.textbox.insert("end", "123")
        self.app.edit_button_click("Delete")
        self.assertEqual(self.app.inputs, [1, 2])
        self.assertEqual(self.app.textbox.get("1.0", "end"), "12\n")

    # 29: Blake Adamson - Test that "run" button calls "button_run" method once. Date: 12/9
    # input: Clicking "Run" // expected output: none // p/f: p
    def test_run_button(self):
        with patch.object(self.app, "button_run", MagicMock()) as mock_button_run:
            self.app.edit_button_click("Run")
        mock_button_run.assert_called_once()
    
    # 30: Blake Adamson - Test that "help" calls iconify method and opens helper window. Date: 12/9
    # input: Clicking "Help" // expected output: window opened // p/f: p
    def test_help_button(self):
        with patch.object(self.app, "iconify", MagicMock()) as mock_iconify:
            with patch.object(gui, "Helper", MagicMock()) as mock_helper:
                self.app.edit_button_click("Help")
        mock_iconify.assert_called_once()
        mock_helper.assert_called_once_with("helpEdit.txt", self.app)

    # 31: Blake Adamson - Test. Date: 12/9
    # input: Clicking "Newline" // expected output: Newline character in textbox // p/f: p
    def test_newline_button(self):
        self.app.textbox.insert("end", "1234")
        self.app.edit_button_click("Newline")
        self.assertEqual(self.app.textbox.get("1.0", "end"), "1234\n\n")

    # 32: Blake Adamson - Test that file_warning triggers iconify and opens window. Date: 12/9
    # input: Clicking "File Warning" // expected output: window opened // p/f: p
    def test_file_warning(self):
        with patch.object(self.app, "iconify", MagicMock()) as mock_iconify:
            with patch.object(gui, "File", MagicMock()) as mock_file:
                self.app.file_warning()
        mock_iconify.assert_called_once()
        mock_file.assert_called_once_with(self.app)

    # 33: Blake Adamson - Test that runIO method in Runner performes given operation. Date: 12/9
    # input: RunIO op // expected output: "Write" // p/f: p
    def test_runIO(self):
        # Create a Runner instance
        with patch.object(gui, "Runner") as mock_runner:
            runner_instance = mock_runner.return_value
            # run io op
            self.app.curr_command = MagicMock()
            self.app.curr_command.operation = ["IO", "0"]
            runner_instance.runIO()

    # 34: Blake Adamson - Testing that GUI correctly displays title. Date:12/9
    # input: expected string // expected output: UVSIM code editor // p/f: p
    def test_title(self):
        title = self.app.winfo_toplevel().title()
        expected = 'UVSIM code editor'
        self.assertEqual(title, expected)

if __name__ == '__main__':
    unittest.main() 