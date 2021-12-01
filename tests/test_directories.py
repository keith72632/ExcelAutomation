import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "../source")
sys.path.append(topdir)
from spreadsheets.filelib import Directories
import unittest
from datetime import date, datetime

class DirectoriesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.workdir = 'C:\\Users\\Carroll Boone Water\\Documents\\Working_Directory'

    def test_directories_class(self):
        d = Directories()
        res = d.set_working_dir(self.workdir)
        self.assertEqual(d.get_working_dir(), self.workdir)
    def test_month_covert_class1(self):
        d = Directories()
        res = d.convert_month_to_dec("November")
        self.assertEqual(res, "11")

    def test_month_convert_class2(self):
        d = Directories()
        res = d.convert_month_to_dec("January")
        self.assertEqual(res, "01")

    def test_get_prev_month_str(self):
        months = [
            None,
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
        month = datetime.now().month
        d = Directories()
        res = d.get_prev_month_str()
        self.assertEqual(res, months[month-1])

    def test_convert_month_to_dec(self):
        month = datetime.now().month
        d = Directories()
        res = d.convert_month_to_dec("January")
        self.assertEqual(res, "01")

if __name__ == "__main__":
    unittest.main()

    