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
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog, messagebox
from visuals import *


def select_work_dir():
	global folder_select
	folder_select = filedialog.askdirectory()
	route = Label(text='Folder Selected (This needs to be your working directory):\n' + str(folder_select))
	route.place(relx=0.25, y=350)
	route.configure(font=(12), fg="green")
	print(f'Folder selected {folder_select}')
	global month_menu
	month_menu = menu()




def mainf():

	global INC_COUNT
	INC_COUNT += inc_status_bar("starting...")

	print(month_menu.get())

	#constants
	#url for bact sample data
	URL = 'https://www.ark.org/health/eng/autoupdates/bacti/bactic.htm'
	#needed to change text colors in terminal
	init()

	INC_COUNT += inc_status_bar("terminal colors initialized")

	wbooks = Books()
	loggers = Logger()
	transfers = Transfer()
	dirs = Directories()
	p = Prompts()

	try:
		dirs.set_working_dir(folder_select)
	except NameError:
		print(f'{p.err()}Please select a working directory')


	INC_COUNT += inc_status_bar("working directory set")

	west_path, east_path, chem_path, table_path, midnight_path = dirs.get_file_from_date(month_menu.get())

	west_wb, east_wb, chem_wb, table_wb, midnight_wb = wbooks.load_workbooks(west_path, east_path, chem_path, table_path, midnight_path)

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

	INC_COUNT += inc_status_bar("workbooks loaded")

	w_active, e_active, c_active, table_active, midnight_active = west_wb.active, east_wb.active, chem_wb.active, table_wb.active, midnight_wb.active

	#scan of the health department website for the BMR data
	hd_scraper = BmrScraper(URL)
	locations_data = hd_scraper.scan_health_dep()
	# display_list_of_dicks(locations_data)

	INC_COUNT += inc_status_bar("BMR data gathered from health department")

	loggers.log_meters(west_swor_front, east_swor_front, midnight_readings)
	loggers.log_ammonia(west_swor_front, east_swor_front, midnight_readings)
	loggers.log_peaks(west_swor_back, east_swor_back, midnight_readings)
	loggers.log_clearwells(west_swor_back, east_swor_back, midnight_readings)
	loggers.log_free_chlorine(west_swor_back, east_swor_back, midnight_readings)
	loggers.log_chlorine_used(west_swor_front, east_swor_front, midnight_readings)
	loggers.log_hours(west_swor_front, east_swor_front, midnight_readings)
	loggers.log_pac(west_swor_front, east_swor_front, midnight_readings)
	loggers.log_lime(west_swor_front, east_swor_front, midnight_readings)

	INC_COUNT += inc_status_bar("data logged")

	transfers.transfer_meters_west(west_swor_front, w_chem)
	transfers.transfer_meters_east(east_swor_front, e_chem)
	transfers.transfer_rainfall(west_swor_front, east_swor_front)
	transfers.transfer_finish_pH(west_swor_front, east_swor_front)
	transfers.transfer_total(west_swor_front, east_swor_front)
	transfers.transfer_chloramine(west_swor_front, east_swor_front)

	INC_COUNT += inc_status_bar("data transfered")

	transfers.transfer_flow_west(west_swor_front, w_chem)
	transfers.transfer_flow_east(east_swor_front, e_chem)
	transfers.transfer_chlorine_west(west_swor_front, w_chem)
	transfers.transfer_chlorine_East(east_swor_front, e_chem)
	transfers.transfer_fluoride(west_swor_front, east_swor_front)

	transfers.transfer_chlorine_res_east(e_chem, east_table)
	transfers.transfer_chlorine_res_west(w_chem, west_table)

	transfers.transfer_distribution(w_chem, e_chem)

	INC_COUNT += inc_status_bar("transfering complete")

	loggers.log_bmr(bmr_wb, locations_data)
	loggers.log_ifmrs(west_ifmr, east_ifmr)
	wbooks.save_workbooks(west_wb, east_wb, west_path, east_path, chem_wb, chem_path, table_wb, table_path, midnight_wb, midnight_path)

	total_exceptions = wbooks.get_exceptions() + loggers.get_exceptions() + transfers.get_exceptions() + hd_scraper.get_exceptions() + dirs.get_exceptions()

	if total_exceptions > 0:
		print(f'{p.err()}Errors: {total_exceptions}\n')
	else:
		print(f'{p.ok()}Proccess complete with zero errors\n')

	INC_COUNT += inc_status_bar("exceptions counted")
	
	print('\033[43m' + ('*' * 60))
	print('DATES ON MIDNIGHT SPREADSHEET ARE SUPPOSE TO BE OFF BY A DAY')
	print(('*' * 60) + '\033[0m')

	INC_COUNT += inc_status_bar("finished")
	program_finish()
	print(f'Increment counter = {INC_COUNT}')

if __name__ == '__main__':

	root.title("Excel Automator")
	root.geometry('1100x500+375+225')

	header()
	prog_bar()

	#pass functions as argument to be used as commands in gui buttons
	start_btn(mainf)
	dir_btn(select_work_dir)
	
	root.mainloop()


