import os
import sys

from datetime import datetime
topdir = os.path.join(os.path.dirname(__file__), "..\source")
sys.path.append(topdir)
import unittest
from spreadsheets.filelib import Directories

class PdfTestCase(unittest.TestCase):
	def setUp(self) -> None:
		self.d = Directories()
		self.months = [ "zero", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]

	def test_get_year(self):
		year = str(datetime.now().year)
		self.assertEqual(year, self.d.get_year())

	def test_get_month_str(self):
		month_index = datetime.now().month
		self.assertEqual(self.months[month_index], self.d.get_month_str())

	def test_get_prev_month_str(self):
		month_index = datetime.now().month
		prev_month_index = 12 if month_index == 1 else month_index - 1
		self.assertEqual(self.months[prev_month_index], self.d.get_prev_month_str())

	def test_convert_month_to_dec(self):
		self.assertEqual(12, int(self.d.convert_month_to_dec("December")))

	def test_get_month_dec(self):
		self.assertEqual(str(datetime.now().month), self.d.get_month_dec())

	def test_get_prev_month_dec(self):
		self.assertEqual(str(datetime.now().month -1), self.d.get_prev_month_dec())

if __name__ == "__main__":
	unittest.main()