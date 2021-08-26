from openpyxl import Workbook, load_workbook
from colors import ok_block, error_block, warning_block

def activate_workbooks(west_file, east_file, chem_file):
	west_wb = load_workbook(west_file)
	print(f'{ok_block()}West Workbook loaded from:\n\t{west_file}\n')
	
	east_wb = load_workbook(east_file)
	print(f'{ok_block()}East Workbook loaded from:\n\t{east_file}\n')

	chem_wb = load_workbook(chem_file)
	print(f'{ok_block()}Chemical Treatment Workbook loaded from:\n\t{chem_file}\n')

	return west_wb, east_wb, chem_wb


def save_workbooks(west_wb, east_wb, west_path, east_path, chem_wb, chem_path):
	west_wb.save(west_path)
	east_wb.save(east_path)
	chem_wb.save(chem_path)

	print(ok_block() + 'workbooks saved\n')
