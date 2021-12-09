import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
import unittest

class PdfTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.pth = b'C:\Users\Carroll Boone Water\Documents\Working_Directory'

    def test_working_dir_path(self):
        res = os.path.isdir(self.pth)
        self.assertTrue(res)

    def test_pdf_dir_structure(self):
        stuff = os.path.isdir(self.pth + b'\DocumentsPDF')
        self.assertTrue(stuff)

    def test_files(self):
        directory = os.listdir(self.pth + b'\DocumentsPDF')
        for file in directory:
            if 'pdf' in str(file):
                self.assertTrue(1)

if __name__ == "__main__":
    unittest.main()