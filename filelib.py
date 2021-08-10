from datetime import datetime
import os

def get_file_from_date():

	#get month number to use as prefix
	monthnum = str(datetime.today()).split('-')
	month = monthnum[1]
	print(f'Month: {month}')


	west_dir = "C:\\Users\\Carroll Boone Water\\Desktop\\2021_ADH_Reports\\West_Plant_Operations_Reports\\"
	east_dir = "C:\\Users\\Carroll Boone Water\\Desktop\\2021_ADH_Reports\\East_Plant_Operations_Reports\\"

	#list of files in 2021 directory
	west_list = os.listdir(west_dir)
	east_list = os.listdir(east_dir)

	#sort through directory for file corresponding with the current month
	west_file = [file for file in west_list if file.startswith(month)]
	east_file = [file for file in east_list if file.startswith(month)]
	print(f'West file: {west_file[0]}')
	print(f'East file: {east_file[0]}')


	west_path = west_dir + west_file[0]
	east_path = east_dir + east_file[0]

	return west_path, east_path
