from datetime import datetime
import os
from colors import Prompts

WEST_DIR = "C:\\Users\\Carroll Boone Water\\Desktop\\2021_ADH_Reports\\West_Plant_Operations_Reports\\"
EAST_DIR = "C:\\Users\\Carroll Boone Water\\Desktop\\2021_ADH_Reports\\East_Plant_Operations_Reports\\"
CHEM_TREAT_DIR = "C:\\Users\\Carroll Boone Water\\Desktop\\2021_ADH_Reports\\Chemical_Treatment_Records\\"
MANGO_METERS = "C:\\Users\\Carroll Boone Water\\Documents\\keith's\\MangoLogs\\"


def get_year():
	#get month number to use as prefix
	date_list = str(datetime.today()).split('-')
	year = date_list[0]
	return year

def get_month_str():
	months = {
		"01": "January",
		"02": "February",
		"03": "March",
		"04": "April",
		"05": "May",
		"06": "June",
		"07": "July",
		"08": "August",
		"09": "September",
		"10": "October",
		"11": "November",
		"12": "December"
	}
	#get month number to use as prefix
	monthnum = str(datetime.today()).split('-')
	month = monthnum[1]
	return months[month]

def get_prev_month_str():
	months = {
		"01": "January",
		"02": "February",
		"03": "March",
		"04": "April",
		"05": "May",
		"06": "June",
		"07": "July",
		"08": "August",
		"09": "September",
		"10": "October",
		"11": "November",
		"12": "December"
	}

	month = '0' + str((datetime.now().month) - 1)
	return months[month]

def  get_month_dec():
	return '0' + str((datetime.now().month))

def get_prev_month_dec():
	return '0' + str((datetime.now().month) - 1)


def get_file_from_date():
	p = Prompts()

	#get month number to use as prefix
	# monthnum = str(datetime.today()).split('-')
	# month = monthnum[1]
	
	# use this below for previous month
	month = get_prev_month_dec()
	print(f'Month: {get_prev_month_str()}')



	#list of files in 2021 directory
	west_list = os.listdir(WEST_DIR)
	east_list = os.listdir(EAST_DIR)
	chem_list = os.listdir(CHEM_TREAT_DIR)
	meter_list = os.listdir(MANGO_METERS)

	#sort through directory for file corresponding with the current month
	try:
		west_file =  [file for file in west_list if file.startswith(month)]
		print(f'{p.ok()}West file: {west_file[0]}')
	except:
		print(f'{p.warn()}West Operations Report Not Found\n')

	try:
		east_file =  [file for file in east_list if file.startswith(month)]
		print(f'{p.ok()}East file: {east_file[0]}')
	except:
		print(f'{p.warn()}East Operations Report Not Found\n')

	try:
		chem_file =  [file for file in chem_list if file.startswith(month)]
		print(f'{p.ok()}Chem file: {chem_file[0]}')
	except:
		print(f'{p.warn()}Chemical Reatment Record Not Found\n')

	try:
		meter_file = [file for file in meter_list if file.startswith(month)]
		print(f'{p.ok()}Meter file {meter_file[0]}')
	except:
		print(f'{p.warn()}Meter Reading File Not Found\n')




	west_path = WEST_DIR + west_file[0]
	east_path = EAST_DIR + east_file[0]
	chem_path = CHEM_TREAT_DIR + chem_file[0]

	return west_path, east_path, chem_path

def create_files(west_dir, east_dir):
	year = str(datetime.today()).split('-')
	print(year[0])
	for file in range(13):
		if file < 10:
			f = open(f'{west_dir}0{str(file)}-{str(year[0])}_CBWD_West_FR.xlsx', 'w')
			x = open(f'{east_dir}0{str(file)}-{str(year[0])}_CBWD_East_FR.xlsx', 'w')
		else:
			f = open(f'{west_dir}{str(file)}-{str(year[0])}_CBWD_West_FR.xlsx', 'w')
			x = open(f'{east_dir}{str(file)}-{str(year[0])}_CBWD_East_FR.xlsx', 'w')
			
		print(f'File created: {west_dir}0{str(file)}-{str(year[0])}_CBWD_West_FR.xlsx')
		print(f'File created: {east_dir}0{str(file)}-{str(year[0])}_CBWD_East_FR.xlsx')
		f.close()
		x.close()

def delete_files(dir_name, file_ext):
	x = input(f'Are you sure you want to delete {file_ext} files in {dir_name}?')

	if x == 'yes':
		os.system(f'rm *.{file_ext}')

	else:
		print('Deleting failed')