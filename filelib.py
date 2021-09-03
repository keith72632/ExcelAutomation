from datetime import datetime
import os
from colors import Prompts

west_dir = "C:\\Users\\Carroll Boone Water\\Desktop\\2021_ADH_Reports\\West_Plant_Operations_Reports\\"
east_dir = "C:\\Users\\Carroll Boone Water\\Desktop\\2021_ADH_Reports\\East_Plant_Operations_Reports\\"
chem_treat_dir = "C:\\Users\\Carroll Boone Water\\Desktop\\2021_ADH_Reports\\Chemical_Treatment_Records\\"
mango_meters = "C:\\Users\\Carroll Boone Water\\Documents\\keith's\\MangoLogs\\"

def get_file_from_date():
	p = Prompts()
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
	# monthnum = str(datetime.today()).split('-')
	# month = monthnum[1]
	
	# use this below for previous month
	month = '0' + str((datetime.now().month) - 1)
	print(f'Month: {months[month]}')



	#list of files in 2021 directory
	west_list = os.listdir(west_dir)
	east_list = os.listdir(east_dir)
	chem_list = os.listdir(chem_treat_dir)
	meter_list = os.listdir(mango_meters)

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




	west_path = west_dir + west_file[0]
	east_path = east_dir + east_file[0]
	chem_path = chem_treat_dir + chem_file[0]

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