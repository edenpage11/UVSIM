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
    
    def test_startup(self):
        title = self.app.winfo_toplevel().title()
        expected = 'The Application'
        self.assertEqual(title, expected)

if __name__ == '__main__':
    unittest.main() 