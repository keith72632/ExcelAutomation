from openpyxl import Workbook, load_workbook
import sys
import os
from datetime import datetime
from spreadsheets.loggers import Logger
from spreadsheets.transfers import Transfer
from spreadsheets.filelib import Directories
from spreadsheets.workbooks import Books
from web.soups import BmrScraper
from colorama import init
from time import sleep
from lib.colors import Prompts
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog, messagebox
from gui.visuals import *
from gui.buttons import *
from documentlib.documents import sign_all
from lib.dirtools import *
from lib.helpers import *




#TODO: Move this function somewhere else
def select_work_dir():
	global folder_select
	folder_select = filedialog.askdirectory()
	route = Label(text='Folder Selected (This needs to be your working directory):\n' + str(folder_select))
	route.place(relx=0.28, y=350)
	route.configure(font=(12), fg="green")
	print(f'Folder selected {folder_select}')
	global month_menu
	month_menu = menu()
	global plant_name
	plant_name = bmr_plant_name()
	sign_btn()

#TODO: Move this function somewhere else
def sign_btn():
	btn = Button(root, text="Sign Documents", fg="white", bd=3, bg='grey' ,command=lambda: sign_all(folder_select))
	btn.place(relx=0.893, rely=0.001)
	btn.configure(width=15)

def mainf():
	print("folder_select in main: " + folder_select)

	prog_bar()

	global INC_COUNT
	#this is the number of progress bar increments before the try/excepts for month and working dir
	inc_cnt = 30

	#url for bact sample data
	URL = 'https://www.ark.org/health/eng/autoupdates/bacti/bactic.htm'
	#needed to change text colors in terminal
	init()

	INC_COUNT += inc_status_bar(msg="terminal colors initialized")

	
	dirs = Directories()
	INC_COUNT += inc_status_bar(msg="Directories instance created")
	
	p = Prompts()

	#takes folder selected in select_work_dir() filedialog
	try:
		dirs.set_working_dir(folder_select)
	except NameError:
		print(f'{p.err()}Please select a working directory')


	INC_COUNT += inc_status_bar(msg="working directory set")

	try:
		west_path, east_path, chem_path, table_path, midnight_path = dirs.get_file_from_date(month_menu=month_menu.get())
	except KeyError:
		prompt_error("No month selected. Please select month, then click Start again")
		#resets the progress bar
		pb1['value'] -= inc_cnt

	except NameError:
		prompt_error("Please select the Working_Directory")
		#resets the progress bar
		inc_cnt += 10
		pb1['value'] -= inc_cnt

	wbooks = Books(west_file=west_path, east_file=east_path, chem_file=chem_path,
		table_file=table_path, meter_file=midnight_path)
	INC_COUNT += inc_status_bar(msg="Workbook instance created")


	west_wb, east_wb, chem_wb, table_wb, midnight_wb = wbooks.load_workbooks()

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


	INC_COUNT += inc_status_bar(msg="workbooks loaded")

	w_active, e_active, c_active, table_active, midnight_active = west_wb.active, east_wb.active, chem_wb.active, table_wb.active, midnight_wb.active

	#scan of the health department website for the BMR data
	hd_scraper = BmrScraper(url=URL, name=plant_name.get())
	INC_COUNT += inc_status_bar(msg="BmrScraper instance created")

	locations_data = hd_scraper.scan_health_dep()
	# display_list_of_dicks(locations_data)
	INC_COUNT += inc_status_bar(msg="BMR data gathered from health department")
	loggers = Logger(west_front=west_swor_front, east_front=east_swor_front, west_back=west_swor_back, east_back=east_swor_back, midnight=midnight_readings)
	INC_COUNT += inc_status_bar(msg="Logger instance created")
	transfers = Transfer(west_front=west_swor_front, east_front=east_swor_front, w_chem=w_chem, e_chem=e_chem, west_table=west_table, east_table=east_table)
	INC_COUNT += inc_status_bar(msg="Transfer instance created")


	loggers.log_all()
	loggers.log_ifmrs(west_ifmr, east_ifmr, month=month_menu.get())
	loggers.log_bmr(bmr_wb, locations_data)
	INC_COUNT += inc_status_bar(msg="BMR data logged to spreadsheet")
	INC_COUNT += inc_status_bar(msg="All data logged successfully")


	transfers.transfer_all()

	INC_COUNT += inc_status_bar(msg="transfering complete")

	wbooks.save_workbooks(west_wb, east_wb, west_path, east_path, chem_wb, chem_path, table_wb, table_path, midnight_wb, midnight_path)

	process_exceptions(wbooks.get_exceptions() + loggers.get_exceptions() + transfers.get_exceptions() + hd_scraper.get_exceptions() + dirs.get_exceptions())

	INC_COUNT += inc_status_bar(msg="exceptions counted")
	
	cmd_banner('DATES ON MIDNIGHT SPREADSHEET ARE SUPPOSE TO BE OFF BY A DAY')
	INC_COUNT += inc_status_bar(msg="finished")

	print(f'Inc count {INC_COUNT}')
	program_finish()

if __name__ == '__main__':
	root.title("Excel Automator")
	root.geometry('1100x500+375+225')

	header()
	#pass functions as argument to be used as commands in gui buttons
	#Start button calls mainf
	start_btn(cmd=mainf)
	dir_btn(cmd=select_work_dir)
	create_dirs_btn(cmd=create_directory_structure)

	
	root.mainloop()


