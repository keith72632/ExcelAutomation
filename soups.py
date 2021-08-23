from bs4 import BeautifulSoup
import requests

def scan_health_dep():
	URL = 'https://www.ark.org/health/eng/autoupdates/bacti/bactic.htm'
	p = requests.get(URL)
	soup = BeautifulSoup(p.content, "html.parser")
	data = soup.find_all('tr')
	fir = data[1]
	# print(f'Data = {fir}')
	# print(f'attrs = {fir.attrs}')
	# print(f'td = {fir.td.text}')

	berryville = []
	for line in data[1:]:
		if line.td.text == "CARROLL-BOONE WATER DISTRICT":
			print(line.text)
			items = line.text.split('\n')
			for i in items:
				berryville.append(i)

	for x in berryville:
		print(f'list item: {x}')

	# cleaned = [x for x in data if x[0].text == "CARROLL-BOONE WATER DISTRICT"]
