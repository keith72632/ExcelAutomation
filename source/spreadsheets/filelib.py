from datetime import date, datetime
import os
import sys
from lib.colors import Prompts
import traceback
from pathlib import Path
from gui.visuals import inc_status_bar, root, log_error, INC_COUNT


class Directories:
	_working_dir = ' '
	_west_dir = ' '
	_east_dir = ' '
	_chem_treat_dir = ' '
	_chlorine_tables = ' '
	_mango_meter = ' '
	def __init__(self):
		pass

	EXCEPTIONS = 0

	def set_working_dir(self, _working_dir):
		global INC_COUNT
		p = Prompts()
		if _working_dir:
			INC_COUNT += inc_status_bar("Working directory validated", 10)
			self._working_dir = _working_dir
			pth = Path(self._working_dir)
			self._west_dir = str(pth) + "\\West_Plant_Operations_Reports\\"
			self._east_dir = str(pth) + "\\East_Plant_Operations_Reports\\"
			self._chem_treat_dir = str(pth) + "\\Chemical_Treatment_Records\\"
			self._chlorine_tables = str(pth) + "\\Chemical_Treatment_Records\\Chlorine_Tables\\"
			self._mango_meter = str(pth) + "\\MangoLogs\\"
		else:
			print(f'{p.err()}No working directory selected')
			INC_COUNT += inc_status_bar("No working directory selected", 10)
	def get_working_dir(self):
		return self._working_dir

	def get_year(self) -> str:
		#get month number to use as prefix
		# date_list = str(datetime.today()).split('-')
		year = str(datetime.now().year)
		return year

	def get_month_str(self) -> str:
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

	def get_prev_month_str(self) -> str:
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
		m = (datetime.now().month) - 1
		if m < 10:
			month = '0' + str(m)
		elif m == 0:
			month = '12'
		else:
			month = str(m)
		print(f'get prev month {months["12"]}')
		return months["12"]

	def convert_month_to_dec(self, monthstr):
		months = {
		"January": "01",
		"February": "02",
		"March": "03",
		"April": "04",
		"May": "05",
		"June": "06",
		"July": "07",
		"August": "08",
		"September": "09",
		"October": "10",
		"November": "11",
		"December": "12"
		}
		print(f'convert month to dec {months[monthstr]}')
		return months[monthstr]

	def  get_month_dec(self):
		month = datetime.now().month
		if month < 10:
			return '0' + str(month)
		else:
			return str(month)

	def get_prev_month_dec(self):
		prev_month = datetime.now().month - 1
		if prev_month < 10:
			return '0' + str(prev_month)
		else:
			return str(prev_month)


	def get_file_from_date(self, monthmenu):
		p = Prompts()
		global INC_COUNT
		#get month number to use as prefix
		# monthnum = str(datetime.today()).split('-')
		# month = monthnum[1]
		
		# use this below for previous month
		month = self.convert_month_to_dec(monthmenu)
	
		INC_COUNT += inc_status_bar("Month Selected", 10)



		#list of files in 2021 directory
		west_list = os.listdir(self._west_dir)
		east_list = os.listdir(self._east_dir)
		chem_list = os.listdir(self._chem_treat_dir)
		midnight_list = os.listdir(self._mango_meter)
		chlorine_tables_list = os.listdir(self._chlorine_tables)

		#sort through directory for file corresponding with the current month
		try:
			west_file =  [file for file in west_list if file.startswith(month)]
			print(f'{p.ok()}West file: {west_file[0]}')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.warn()}West Operations Report Not Found\n')
			traceback.print_exc()
		try:
			east_file =  [file for file in east_list if file.startswith(month)]
			print(f'{p.ok()}East file: {east_file[0]}')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.warn()}East Operations Report Not Found\n')
			traceback.print_exc()
		try:
			chem_file =  [file for file in chem_list if file.startswith(month)]
			print(f'{p.ok()}Chem file: {chem_file[0]}')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.warn()}Chemical Reatment Record Not Found\n')
			traceback.print_exc()
		try:
			midnight_file = [file for file in midnight_list if file.startswith(month)]
			print(f'{p.ok()}Midnight file: {midnight_file[0]}')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.warn()}Meter Reading File Not Found\n')
			traceback.print_exc()
		try:
			tables_file = [file for file in chlorine_tables_list if file.startswith(month)]
			print(f'{p.ok()}Tables file {tables_file[0]}')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.warn()}Chlorine Table not found\n')
			traceback.print_exc()

		try:
			west_path = self._west_dir + west_file[0]
			east_path = self._east_dir + east_file[0]
			chem_path = self._chem_treat_dir + chem_file[0]
			table_path = self._chlorine_tables + tables_file[0]
			midnight_path = self._mango_meter + midnight_file[0]
		except IndexError:
			print('Are you sure all spreadsheets have been created for last month?')
			traceback.print_exc()
			inc_status_bar("No spreadsheets found. Are you sure spreadsheets for last month have been created?", 10)
		
		INC_COUNT += inc_status_bar("All files matched with coreresponding month", 10)

		return west_path, east_path, chem_path, table_path, midnight_path

	def create_files(self, _west_dir, _east_dir):
		year = str(datetime.today()).split('-')
		print(year[0])
		for file in range(13):
			if file < 10:
				f = open(f'{_west_dir}0{str(file)}-{str(year[0])}_CBWD_West_FR.xlsx', 'w')
				x = open(f'{_east_dir}0{str(file)}-{str(year[0])}_CBWD_East_FR.xlsx', 'w')
			else:
				f = open(f'{_west_dir}{str(file)}-{str(year[0])}_CBWD_West_FR.xlsx', 'w')
				x = open(f'{_east_dir}{str(file)}-{str(year[0])}_CBWD_East_FR.xlsx', 'w')
				
			print(f'File created: {_west_dir}0{str(file)}-{str(year[0])}_CBWD_West_FR.xlsx')
			print(f'File created: {_east_dir}0{str(file)}-{str(year[0])}_CBWD_East_FR.xlsx')
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