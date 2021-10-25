from bs4 import BeautifulSoup
import sys
import requests
from lib.colors import Prompts

class BmrScraper:
	url = 'https://www.ark.org/health/eng/autoupdates/bacti/bactic.htm'
	name = None
	def __init__(self, name=None):
		self.name = name

	def __del__(self):
		print('BmrScraper Destroyed')
		
	EXCEPTIONS = 0

	def display_list_of_dicks(self, dick_list):
		p = Prompts()
		print(str(p.OK) + '\n' + '*' * 50 + str(p.RESET))
		print('Entries for BMR from Health Departement Website')
		for i, dick in enumerate(dick_list):
			print(f'entry #{i + 1} \n')
			for key, value in dick.items():
				print(f'\t{key}: {value}')
			print('\n')
		print(str(p.OK) + '\n' + '*' * 50 + str(p.RESET))


	def scan_health_dep(self):
		P = Prompts()
		print(f'BMR url {self.url}')
		p = requests.get(self.url)
		soup = BeautifulSoup(p.content, "html.parser")
		data = soup.find_all('tr')

		locations = []
		i = 0
		for line in data[1:]:
			if line.td.text == self.name:
				i += 1
				items = line.text.split('\n')
				locations.append(
					{
						'PWS': items[2],
						'lab_no': items[3],
						'date_collected': items[4],
						'date_recv': items[5],
						'location_id': items[6],
						'location': items[7],
						'signature': items[8],
						'sample_type': items[9],
						'result': items[10],
						'chlorine': items[12]
					}
				)

		print(f'{P.ok()}{i} BMR entries for {self.name} found\n')

		return locations

	def get_exceptions(self):
		return self.EXCEPTIONS