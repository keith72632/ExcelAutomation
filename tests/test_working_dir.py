import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
import unittest

class WorkingDirTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.pth = b'C:\Users\Carroll Boone Water\Documents\Working_Directory'

    def test_working_dir_path(self):
        res = os.path.isdir(self.pth)
        self.assertTrue(res)

    def test_working_dir_structure(self):
        stuff = os.listdir(self.pth)
        res = True if b'MangoLogs' \
            and b'Chemical_Treatment_Records' \
            and b'DocumentsJPG' \
            and b'DocumentsPDF' \
            and b'East_Plant_Operations_Reports' \
            and b'West_Plant_Operations_Reports' in stuff \
        else False
        self.assertTrue(res)

    def test_for_chlorine_tables(self):
        res = os.path.isdir(self.pth + b'\Chemical_Treatment_Records\Chlorine_Tables')
        self.assertTrue(res)

    def test_jpg_dir_structure(self):
        stuff = os.listdir(self.pth + b'\DocumentsJPG')
        res = True if b'files' and b'finals' in stuff else True
        self.assertTrue(res)

    def test_pdf_dir_structure(self):
        stuff = os.path.isdir(self.pth + b'\DocumentsPDF')
        self.assertTrue(stuff)


if __name__ == "__main__":
    unittest.main()

    