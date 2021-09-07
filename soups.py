from bs4 import BeautifulSoup
import sys
import requests
from colors import Prompts

def display_list_of_dicks(dick_list):
	p = Prompts()
	print(str(p.OK) + '\n' + '*' * 50 + str(p.RESET))
	print('Entries for BMR from Health Departement Website')
	for i, dick in enumerate(dick_list):
		print(f'entry #{i + 1} \n')
		for key, value in dick.items():
			print(f'\t{key}: {value}')
		print('\n')
	print(str(p.OK) + '\n' + '*' * 50 + str(p.RESET))


def scan_health_dep():
	p = Prompts()
	URL = 'https://www.ark.org/health/eng/autoupdates/bacti/bactic.htm'
	p = requests.get(URL)
	soup = BeautifulSoup(p.content, "html.parser")
	data = soup.find_all('tr')
	fir = data[1]

	locations = []
	i = 0
	for line in data[1:]:
		if line.td.text == sys.argv[1]:
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

	print(f'{i} Entries for {sys.argv[1]} found\n')

	return locations
