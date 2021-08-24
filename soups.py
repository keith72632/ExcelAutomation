from bs4 import BeautifulSoup
import requests

def display_list_of_dicks(dick_list):
	for i, dick in enumerate(dick_list):
		print(f'{i} entry:\n')
		for key, value in dick.items():
			print(f'\t{key}: {value}')
		print('\n\n')

def scan_health_dep():
	URL = 'https://www.ark.org/health/eng/autoupdates/bacti/bactic.htm'
	p = requests.get(URL)
	soup = BeautifulSoup(p.content, "html.parser")
	data = soup.find_all('tr')
	fir = data[1]
	# print(f'Data = {fir}')
	# print(f'attrs = {fir.attrs}')
	# print(f'td = {fir.td.text}')

	locations = []
	for line in data[1:]:
		if line.td.text == "CARROLL-BOONE WATER DISTRICT":
			# print(line.text)
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

	# display_list_of_dicks(locations)

	return locations
	# cleaned = [x for x in data if x[0].text == "CARROLL-BOONE WATER DISTRICT"]
