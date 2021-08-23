from openpyxl import Workbook, load_workbook

def activate_workbooks(west_file, east_file, chem_file):
	west_wb = load_workbook(west_file)
	east_wb = load_workbook(east_file)
	chem_wb = load_workbook(chem_file)

	return west_wb, east_wb, chem_wb


def save_workbooks(west_wb, east_wb, west_path, east_path):
	west_wb.save(west_path)
	east_wb.save(east_path)