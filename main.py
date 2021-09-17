from openpyxl import Workbook, load_workbook
import sys
import os
from datetime import datetime
from loggers import Logger
from transfers import Transfer
from filelib import Directories
from workbooks import Books
from soups import BmrScraper
from colorama import init
from time import sleep
from colors import Prompts

# enable scripts with: Set-ExecutionPolicy RemoteSigned


def main():

	#needed to change text colors in terminal
	init()

	b = Books()
	l = Logger()
	t = Transfer()
	s = BmrScraper()
	d = Directories()
	p = Prompts()

	west_path, east_path, chem_path, table_path, midnight_path = d.get_file_from_date()

	west_wb, east_wb, chem_wb, table_wb, midnight_wb = b.load_workbooks(west_path, east_path, chem_path, table_path, midnight_path)

	bmr_wb = west_wb['BMR']
	w_chem = chem_wb['West']
	e_chem = chem_wb['East']
	west_swor_front = west_wb['SWO&R Front Side']
	west_swor_back = west_wb['SWO&R Back Side']
	east_swor_front = east_wb['SWO&R Front Side']
	east_swor_back = east_wb['SWO&R Back Side']
	west_ifmr = west_wb['IFMR >10,000']
	east_ifmr = east_wb['IFMR >10,000']
	east_table = table_wb['East']
	west_table = table_wb['West']
	midnight_readings = midnight_wb['Midnight']

	w_active, e_active, c_active, table_active, midnight_active = west_wb.active, east_wb.active, chem_wb.active, table_wb.active, midnight_wb.active

	#scan of the health department website for the BMR data
	locations_data = s.scan_health_dep()
	# display_list_of_dicks(locations_data)

	l.log_meters(west_swor_front, east_swor_front, midnight_readings)
	l.log_ammonia(west_swor_front, east_swor_front, midnight_readings)
	l.log_peaks(west_swor_back, east_swor_back, midnight_readings)
	l.log_clearwells(west_swor_back, east_swor_back, midnight_readings)
	l.log_free_chlorine(west_swor_back, east_swor_back, midnight_readings)
	l.log_chlorine_used(west_swor_front, east_swor_front, midnight_readings)
	l.log_hours(west_swor_front, east_swor_front, midnight_readings)

	t.transfer_meters_west(west_swor_front, w_chem)
	t.transfer_meters_east(east_swor_front, e_chem)
	t.transfer_rainfall(west_swor_front, east_swor_front)
	t.transfer_finish_pH(west_swor_front, east_swor_front)
	t.transfer_total(west_swor_front, east_swor_front)
	t.transfer_chloramine(west_swor_front, east_swor_front)

	t.transfer_flow_west(west_swor_front, w_chem)
	t.transfer_flow_east(east_swor_front, e_chem)
	t.transfer_chlorine_west(west_swor_front, w_chem)
	t.transfer_chlorine_East(east_swor_front, e_chem)
	t.transfer_fluoride(west_swor_front, east_swor_front)

	t.transfer_chlorine_res_east(e_chem, east_table)
	t.transfer_chlorine_res_west(w_chem, west_table)

	t.transfer_distribution(w_chem, e_chem)

	l.log_bmr(bmr_wb, locations_data)
	l.log_ifmrs(west_ifmr, east_ifmr)
	b.save_workbooks(west_wb, east_wb, west_path, east_path, chem_wb, chem_path, table_wb, table_path, midnight_wb, midnight_path)

	total_exceptions = b.get_exceptions() + l.get_exceptions() + t.get_exceptions() + s.get_exceptions() + d.get_exceptions()

	if total_exceptions > 0:
		print(f'{p.err()}Errors: {total_exceptions}\n')
	else:
		print(f'{p.ok()}Proccess complete with zero errors\n')

	os.system('pause')

if __name__ == '__main__':
	main()

