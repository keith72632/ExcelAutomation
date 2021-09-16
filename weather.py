import pyowm
from colors import Prompts

APIKEY = 'You Fucking Thought Bitch'
CITY = 'London'

def get_temp():
	p = Prompts()

	try:
		OpenWMap=pyowm.OWM(APIKEY)                   # Use API key to get data
		Weather=OpenWMap.weather_at_place('London')  # give where you need to see the weather
		Data=Weather.get_weather()                   # get out data in the mentioned location

	except AttributeError:
		print(f'{p.warn()}Could not fetch temperatures. Check API key\n')

	try:
		stuff = requests.get(f'api.openweathermap.org/data/2.5/weather?q={CITY}&appid={APIKEY}')
	except:
		print(f'{p.warn()}Could not fetch URL\n')








