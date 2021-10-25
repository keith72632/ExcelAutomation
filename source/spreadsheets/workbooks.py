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
	EXCEPTIONS = 0

	def load_workbooks(self):
		p = Prompts()
		COLOR = p.DEV
		RESET = p.RESET
		FAIL = p.FAIL
		try:
			west_wb = load_workbook(self.west_file)
			print(f'{p.ok()}West Workbook loaded from:\n{COLOR}{self.west_file}{RESET}\n')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Workbook loading failed from:\n{FAIL}{self.west_file}{RESET}\n')

		try:
			east_wb = load_workbook(self.east_file)
			print(f'{p.ok()}East Workbook loaded from:\n{COLOR}{self.east_file}{RESET}\n')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Workbook loading failed from:\n{FAIL}{self.east_file}{RESET}\n')

		try:
			chem_wb = load_workbook(self.chem_file)
			print(f'{p.ok()}Chemical Treatment Workbook loaded from:\n{COLOR}{self.chem_file}{RESET}\n')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Chemical Treatment Workbook loading failed from:\n{FAIL}{self.chem_file}{RESET}\n')

		try:
			table_wb = load_workbook(self.table_file)
			print(f'{p.ok()}Chlorine Table Workbook loaded from:\n{COLOR}{self.table_file}{RESET}\n')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Chlorine Table Workbook loading failed from:\n{FAIL}{self.table_file}{RESET}\n')

		try:
			meter_wb = load_workbook(self.meter_file)
			print(f'{p.ok()}Meter Workbook loaded from:\n{COLOR}{self.meter_file}{RESET}\n')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Meter Workbook loading failed from:\n{FAIL}{self.meter_file}{RESET}\n')

		return west_wb, east_wb, chem_wb, table_wb, meter_wb

	def individual_pages_init(self):
		pass

	def activate_workbooks(self, west_wb, east_wb, chem_wb):
		return west_wb.active, east_wb.active, chem_wb.active


	def get_sub_workbooks(self, west_wb, chem_wb):
		return west_wb['BMR'], chem_wb['West'], chem_wb['East']


	def save_workbooks(self, west_wb, east_wb, west_path, east_path, chem_wb, chem_path, table_wb, table_path, meter_wb, meter_path):
		p = Prompts()

		try:
			west_wb.save(west_path)
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Workbook could not save\n')
		try:
			east_wb.save(east_path)
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Workbook could not save\n')

		try:
			chem_wb.save(chem_path)
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Chemical Treatment Record could not save\n')

		try:
			table_wb.save(table_path)
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Chlorine Table could not save\n')

		try:
			meter_wb.save(meter_path)
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Meter Workbook could not save\n')

		print(p.ok() + 'workbooks saved')


	def get_exceptions(self):
		return self.EXCEPTIONS