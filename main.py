from openpyxl import Workbook, load_workbook
import os
from datetime import datetime
from loggers import *
from filelib import *
from workbooks import *
from soups import scan_health_dep, display_list_of_dicks

# enable scripts with: Set-ExecutionPolicy RemoteSigned


def main():

	print('Opening workbooks...\n')
	west_path, east_path, chem_path = get_file_from_date()

	west_wb, east_wb, chem_wb = activate_workbooks(west_path, east_path, chem_path)
	w_active = west_wb.active
	e_active = east_wb.active
	c_active = chem_wb.active

	log_rainfall(w_active, e_active)
	log_fluoride(w_active, e_active)
	log_finish_pH(w_active, e_active)
	log_total(w_active, e_active)
	log_chloramine(w_active, e_active)

	save_workbooks(west_wb, east_wb, west_path, east_path)
	locations_data = scan_health_dep()
	display_list_of_dicks(locations_data)
	os.system("pause")

	print('workbooks saved\n')


if __name__ == '__main__':
	main()

