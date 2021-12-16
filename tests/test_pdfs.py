import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..\source")
sys.path.append(topdir)
import unittest
from lib.dirtools import export_page

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
    
    def test_export_pdf(self):
        here = os.path.dirname(os.path.abspath(__file__))
        excel = here + '\\test.xlsx'
        pdf_path = here + '\\test.pdf'
        export_page(
            file_path=excel, 
            pdf_path=pdf_path, 
            page_index=1
        )
        files = os.listdir(here)
        pdf = [file for file in files if file == 'test.pdf']
        self.assertTrue(pdf)

if __name__ == "__main__":
    unittest.main()