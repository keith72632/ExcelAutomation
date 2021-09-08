from openpyxl import Workbook, load_workbook
import os
from datetime import datetime
from loggers import (
	log_rainfall,
	log_fluoride,
	log_finish_pH,
	log_total,
	log_chloramine,
	log_bmr,
	log_ifmrs
)
from transfers import (
	transfer_flow_east,
	transfer_flow_west, 
	transfer_meters_east, 
	transfer_meters_west, 
	transfer_chlorine_East, 
	transfer_chlorine_west,
	transfer_chlorine_res_east,
	transfer_chlorine_res_west,
	transfer_distribution
)
from filelib import get_file_from_date
from workbooks import load_workbooks, save_workbooks
from soups import scan_health_dep, display_list_of_dicks
from colorama import init
from time import sleep
from weather import get_temp

# enable scripts with: Set-ExecutionPolicy RemoteSigned


def main():

	#needed to change text colors in terminal
	init()

	west_path, east_path, chem_path, table_path = get_file_from_date()

	west_wb, east_wb, chem_wb, table_wb = load_workbooks(west_path, east_path, chem_path, table_path)

	bmr_wb = west_wb['BMR']
	w_chem = chem_wb['West']
	e_chem = chem_wb['East']
	west_swor = west_wb['SWO&R Front Side']
	east_swor = east_wb['SWO&R Front Side']
	west_ifmr = west_wb['IFMR >10,000']
	east_ifmr = east_wb['IFMR >10,000']
	east_table = table_wb['East']
	west_table = table_wb['West']

	w_active, e_active, c_active, table_active = west_wb.active, east_wb.active, chem_wb.active, table_wb.active

	#scan of the health department website for the BMR data
	locations_data = scan_health_dep()
	# display_list_of_dicks(locations_data)

	log_rainfall(west_swor, east_swor)
	log_fluoride(west_swor, east_swor)
	log_finish_pH(west_swor, east_swor)
	log_total(west_swor, east_swor)
	log_chloramine(west_swor, east_swor)

	transfer_meters_west(west_swor, w_chem)
	transfer_meters_east(east_swor, e_chem)
	transfer_flow_west(west_swor, w_chem)
	transfer_flow_east(east_swor, e_chem)
	transfer_chlorine_west(west_swor, w_chem)
	transfer_chlorine_East(east_swor, e_chem)

	transfer_chlorine_res_east(e_chem, east_table)
	transfer_chlorine_res_west(w_chem, west_table)

	transfer_distribution(w_chem, e_chem)

	#TODO change dates for BMR because it uses previous month
	log_bmr(bmr_wb, locations_data)
	log_ifmrs(west_ifmr, east_ifmr)
	save_workbooks(west_wb, east_wb, west_path, east_path, chem_wb, chem_path, table_wb, table_path)

	# get_temp()
	os.system('pause')

if __name__ == '__main__':
	main()

