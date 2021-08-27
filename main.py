from openpyxl import Workbook, load_workbook
import os
from datetime import datetime
from loggers import *
from filelib import get_file_from_date
from workbooks import *
from soups import scan_health_dep, display_list_of_dicks
from colorama import init
from colors import bcolors, ok_block
from time import sleep

# enable scripts with: Set-ExecutionPolicy RemoteSigned


def main():

	#needed to change text colors in terminal
	init()

	west_path, east_path, chem_path = get_file_from_date()

	west_wb, east_wb, chem_wb = activate_workbooks(west_path, east_path, chem_path)
	w_active = west_wb.active
	e_active = east_wb.active
	c_active = chem_wb.active
	bmr_wb = west_wb['BMR']
	w_chem = chem_wb['West']
	e_chem = chem_wb['East']

	#scan of the health department website for the BMR data
	locations_data = scan_health_dep()
	display_list_of_dicks(locations_data)

	log_rainfall(w_active, e_active)
	log_fluoride(w_active, e_active)
	log_finish_pH(w_active, e_active)
	log_total(w_active, e_active)
	log_chloramine(w_active, e_active)

	transfer_meters_west(w_active, w_chem)
	transfer_meters_east(e_active, e_chem)
	transfer_flow_west(w_active, w_chem)
	transfer_flow_east(e_active, e_chem)
	transfer_chlorine_west(w_active, w_chem)
	transfer_chlorine_East(e_active, e_chem)


	#TODO change dates for BMR because it uses previous month
	log_bmr(bmr_wb, locations_data)

	# print(bmr_wb['A11'].value)

	save_workbooks(west_wb, east_wb, west_path, east_path, chem_wb, chem_path)

	os.system('pause')

if __name__ == '__main__':
	main()

