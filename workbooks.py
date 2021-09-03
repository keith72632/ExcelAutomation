from openpyxl import Workbook, load_workbook
from colors import Prompts

def load_workbooks(west_file, east_file, chem_file):
	p = Prompts()
	west_wb = load_workbook(west_file)
	print(f'{p.ok()}West Workbook loaded from:\n\t{west_file}\n')
	
	east_wb = load_workbook(east_file)
	print(f'{p.ok()}East Workbook loaded from:\n\t{east_file}\n')

	chem_wb = load_workbook(chem_file)
	print(f'{p.ok()}Chemical Treatment Workbook loaded from:\n\t{chem_file}\n')

	return west_wb, east_wb, chem_wb


def activate_workbooks(west_wb, east_wb, chem_wb):
	return west_wb.active, east_wb.active, chem_wb.active


def get_sub_workbooks(west_wb, chem_wb):
	return west_wb['BMR'], chem_wb['West'], chem_wb['East']


def save_workbooks(west_wb, east_wb, west_path, east_path, chem_wb, chem_path):
	p = Prompts()
	west_wb.save(west_path)
	east_wb.save(east_path)
	chem_wb.save(chem_path)
	print(p.ok() + 'workbooks saved\n')

