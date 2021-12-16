import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "../source")
sys.path.append(topdir)
import unittest
from spreadsheets.workbooks import Books

class WorkbookTestCase(unittest.TestCase):
    def test_books(self):
        pth = os.path.dirname(os.path.abspath(__file__))
        try:
            book = Books(pth + '\\test.xlsx')
        except AttributeError:
            print('Ignore AttributeError')

if __name__ == "__main__":
    unittest.main()

    