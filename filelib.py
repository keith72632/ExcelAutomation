from datetime import datetime
import os
import sys
from colors import Prompts
from pathlib import Path


class Directories:
	working_dir = ' '
	west_dir = ' '
	east_dir = ' '
	chem_treat_dir = ' '
	chlorine_tables = ' '
	mango_meter = ' '
	def __init__(self):
		pass

	EXCEPTIONS = 0

	STAGING = f'\\Production\\' if len(sys.argv) > 1 and sys.argv[2] == "PROD" else "\\Development\\"

	# WORKING_DIR = "C:\\Users\\Carroll Boone Water\\Desktop\\2021_ADH_Reports\\Working_Directory\\"


	# WEST_DIR = WORKING_DIR + STAGING + "West_Plant_Operations_Reports\\"
	# EAST_DIR = WORKING_DIR + STAGING + "East_Plant_Operations_Reports\\"
	# CHEM_TREAT_DIR = WORKING_DIR + STAGING + "Chemical_Treatment_Records\\"
	# CHLORINE_TABLES = WORKING_DIR + STAGING + "Chemical_Treatment_Records\\Chlorine_Tables\\"
	# MANGO_METERS = WORKING_DIR + STAGING + "MangoLogs\\"

	def set_working_dir(self, working_dir):
		self.working_dir = working_dir
		pth = Path(self.working_dir)
		self.west_dir = str(pth) + self.STAGING + "West_Plant_Operations_Reports\\"
		self.east_dir = str(pth) + self.STAGING + "East_Plant_Operations_Reports\\"
		self.chem_treat_dir = str(pth) + self.STAGING + "Chemical_Treatment_Records\\"
		self.chlorine_tables = str(pth) + self.STAGING + "Chemical_Treatment_Records\\Chlorine_Tables\\"
		self.mango_meter = str(pth) + self.STAGING + "MangoLogs\\"
		print(f'Chlorine {self.chlorine_tables}')

	def get_working_dir(self):
		return self.working_dir

	def get_year(self):
		#get month number to use as prefix
		date_list = str(datetime.today()).split('-')
		year = date_list[0]
		return year

	def get_month_str(self):
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

	def get_prev_month_str(self):
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

	def  get_month_dec(self):
		return '0' + str((datetime.now().month))

	def get_prev_month_dec(self):
		return '0' + str((datetime.now().month) - 1)


	def get_file_from_date(self):
		p = Prompts()

		#get month number to use as prefix
		# monthnum = str(datetime.today()).split('-')
		# month = monthnum[1]
		
		# use this below for previous month
		month = self.get_prev_month_dec()
		print(f'Month: {self.get_prev_month_str()}')



		#list of files in 2021 directory
		west_list = os.listdir(self.west_dir)
		east_list = os.listdir(self.east_dir)
		chem_list = os.listdir(self.chem_treat_dir)
		midnight_list = os.listdir(self.mango_meter)
		chlorine_tables_list = os.listdir(self.chlorine_tables)

		#sort through directory for file corresponding with the current month
		try:
			west_file =  [file for file in west_list if file.startswith(month)]
			print(f'{p.ok()}West file: {west_file[0]}')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.warn()}West Operations Report Not Found\n')

		try:
			east_file =  [file for file in east_list if file.startswith(month)]
			print(f'{p.ok()}East file: {east_file[0]}')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.warn()}East Operations Report Not Found\n')

		try:
			chem_file =  [file for file in chem_list if file.startswith(month)]
			print(f'{p.ok()}Chem file: {chem_file[0]}')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.warn()}Chemical Reatment Record Not Found\n')

		try:
			midnight_file = [file for file in midnight_list if file.startswith(month)]
			print(f'{p.ok()}Midnight file: {midnight_file[0]}')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.warn()}Meter Reading File Not Found\n')

		try:
			tables_file = [file for file in chlorine_tables_list if file.startswith(month)]
			print(f'{p.ok()}Tables file {tables_file[0]}')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.warn()}Chlorine Table not found\n')


		west_path = self.west_dir + west_file[0]
		east_path = self.east_dir + east_file[0]
		chem_path = self.chem_treat_dir + chem_file[0]
		table_path = self.chlorine_tables + tables_file[0]
		midnight_path = self.mango_meter + midnight_file[0]
		return west_path, east_path, chem_path, table_path, midnight_path

	def create_files(self, west_dir, east_dir):
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

	def delete_files(self, dir_name, file_ext):
		x = input(f'Are you sure you want to delete {file_ext} files in {dir_name}?')

		if x == 'yes':
			os.system(f'rm *.{file_ext}')

		else:
			print('Deleting failed')

	def get_exceptions(self):
		return self.EXCEPTIONS