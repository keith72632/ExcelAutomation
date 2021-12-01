import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "../source")
sys.path.append(topdir)
import unittest
from bs4 import BeautifulSoup
from web.soups import BmrScraper
import requests

class WebScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.ark.org/health/eng/autoupdates/bacti/bactic.htm'
        self.res = requests.get(self.url)

    def test_request(self):
        self.assertEqual(self.res.status_code, 200)

    def test_title(self):
        self.assertTrue('Arkansas Department of Health' in self.res.text)

    def test_data(self):
        self.assertTrue('CARROLL-BOONE WATER DISTRICT' in self.res.text)

    def test_check_data(self):
        b = BmrScraper("CARROLL-BOONE WATER DISTRICT")
        locations = b.scan_health_dep()
        b.display_list_of_dicks(locations)
        if self.assertTrue(len(locations) > 0):
            pws = [data for data in locations if data['PWS'] == '675']
            self.assertTrue(pws)
    


if __name__ == "__main__":
    unittest.main()

    