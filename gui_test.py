import unittest
from unittest.mock import patch
import gui2

class TestGui(unittest.TestCase):
    
    # this will run on a separate thread.
    async def _start_app(self):
        self.app.mainloop()
    
    def setUp(self):
        self.app = gui2.Editor()
        self._start_app()
    
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