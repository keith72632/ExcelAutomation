import sys
from openpyxl import Workbook, load_workbook
from lib.colors import Prompts

class Books:
	def __init__(self, west_file, east_file, chem_file, table_file, meter_file):
		self.west_file = west_file
		self.east_file = east_file
		self.chem_file = chem_file
		self.table_file = table_file
		self.meter_file = meter_file

	def __del__(self):
		print('Books Destroyed')

	EXCEPTIONS = 0

	def load_workbooks(self):
		p = Prompts()
		COLOR = p.DEV
		RESET = p.RESET
		FAIL = p.FAIL
		try:
			self.west_wb = load_workbook(self.west_file)
			print(f'{p.ok()}West Workbook loaded from:\n{COLOR}{self.west_file}{RESET}\n')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Workbook loading failed from:\n{FAIL}{self.west_file}{RESET}\n')

		try:
			self.east_wb = load_workbook(self.east_file)
			print(f'{p.ok()}East Workbook loaded from:\n{COLOR}{self.east_file}{RESET}\n')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Workbook loading failed from:\n{FAIL}{self.east_file}{RESET}\n')

		try:
			self.chem_wb = load_workbook(self.chem_file)
			print(f'{p.ok()}Chemical Treatment Workbook loaded from:\n{COLOR}{self.chem_file}{RESET}\n')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Chemical Treatment Workbook loading failed from:\n{FAIL}{self.chem_file}{RESET}\n')

		try:
			self.table_wb = load_workbook(self.table_file)
			print(f'{p.ok()}Chlorine Table Workbook loaded from:\n{COLOR}{self.table_file}{RESET}\n')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Chlorine Table Workbook loading failed from:\n{FAIL}{self.table_file}{RESET}\n')

		try:
			self.meter_wb = load_workbook(self.meter_file)
			print(f'{p.ok()}Meter Workbook loaded from:\n{COLOR}{self.meter_file}{RESET}\n')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Meter Workbook loading failed from:\n{FAIL}{self.meter_file}{RESET}\n')

		return self.west_wb, self.east_wb, self.chem_wb, self.table_wb, self.meter_wb

	def individual_pages_init(self):
		self.bmr_wb = self.west_wb['BMR']
		self.w_chem = self.chem_wb['West']
		self.e_chem = self.chem_wb['East']
		self.west_swor_front = self.west_wb['SWO&R Front Side']
		self.west_swor_back = self.west_wb['SWO&R Back Side']
		self.east_swor_front = self.east_wb['SWO&R Front Side']
		self.east_swor_back = self.east_wb['SWO&R Back Side']
		self.west_ifmr = self.west_wb['IFMR >10,000']
		self.east_ifmr = self.east_wb['IFMR >10,000']
		self.east_table = self.table_wb['East']
		self.west_table = self.table_wb['West']
		self.midnight_readings = self.meter_wb['Midnight']

	def activate_workbooks(self, west_wb, east_wb, chem_wb):
		return west_wb.active, east_wb.active, chem_wb.active


	def get_sub_workbooks(self, west_wb, chem_wb):
		return west_wb['BMR'], chem_wb['West'], chem_wb['East']


	def save_workbooks(self):
		p = Prompts()

		try:
			self.west_wb.save(self.west_file)
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Workbook could not save\n')
		try:
			self.east_wb.save(self.east_file)
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Workbook could not save\n')

		try:
			self.chem_wb.save(self.chem_file)
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Chemical Treatment Record could not save\n')

		try:
			self.table_wb.save(self.table_file)
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Chlorine Table could not save\n')

		try:
			self.meter_wb.save(self.meter_file)
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Meter Workbook could not save\n')

		print(p.ok() + 'workbooks saved')


	def get_exceptions(self):
		return self.EXCEPTIONS