import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
import unittest
from bs4 import BeautifulSoup
import requests

class WebScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.ark.org/health/eng/autoupdates/bacti/bactic.htm'
        self.res = requests.get(self.url)

    def test_request(self):
        self.assertEqual(self.res.status_code, 200)



if __name__ == "__main__":
    unittest.main()

    