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
from visuals import log_error

def inc_status_bar():
	root.update_idletasks()
	pb1['value'] += 30

def program_finish():
	messagebox.showinfo("Done", "Done")
	root.destroy()

def clicked():
	global folder_select
	folder_select = filedialog.askdirectory()
	route = Label(text='Folder Selected (This needs to be your working directory):\n' + str(folder_select))
	route.place(relx=0.30, rely=0.20)
	print(f'Folder selected {folder_select}')



def main():

	inc_status_bar()

	#constants
	#url for bact sample data
	URL = 'https://www.ark.org/health/eng/autoupdates/bacti/bactic.htm'
	#needed to change text colors in terminal
	init()

	inc_status_bar()

	wbooks = Books()
	loggers = Logger()
	transfers = Transfer()
	dirs = Directories()
	p = Prompts()

	try:
		dirs.set_working_dir(folder_select)
	except NameError:
		print(f'{p.err()}Please select a working directory')


	inc_status_bar()

	west_path, east_path, chem_path, table_path, midnight_path = dirs.get_file_from_date()

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

	inc_status_bar()

	w_active, e_active, c_active, table_active, midnight_active = west_wb.active, east_wb.active, chem_wb.active, table_wb.active, midnight_wb.active

	#scan of the health department website for the BMR data
	hd_scraper = BmrScraper(URL)
	locations_data = hd_scraper.scan_health_dep()
	# display_list_of_dicks(locations_data)

	inc_status_bar()

	loggers.log_meters(west_swor_front, east_swor_front, midnight_readings)
	loggers.log_ammonia(west_swor_front, east_swor_front, midnight_readings)
	loggers.log_peaks(west_swor_back, east_swor_back, midnight_readings)
	loggers.log_clearwells(west_swor_back, east_swor_back, midnight_readings)
	loggers.log_free_chlorine(west_swor_back, east_swor_back, midnight_readings)
	loggers.log_chlorine_used(west_swor_front, east_swor_front, midnight_readings)
	loggers.log_hours(west_swor_front, east_swor_front, midnight_readings)
	loggers.log_pac(west_swor_front, east_swor_front, midnight_readings)
	loggers.log_lime(west_swor_front, east_swor_front, midnight_readings)

	inc_status_bar()

	transfers.transfer_meters_west(west_swor_front, w_chem)
	transfers.transfer_meters_east(east_swor_front, e_chem)
	transfers.transfer_rainfall(west_swor_front, east_swor_front)
	transfers.transfer_finish_pH(west_swor_front, east_swor_front)
	transfers.transfer_total(west_swor_front, east_swor_front)
	transfers.transfer_chloramine(west_swor_front, east_swor_front)

	inc_status_bar()

	transfers.transfer_flow_west(west_swor_front, w_chem)
	transfers.transfer_flow_east(east_swor_front, e_chem)
	transfers.transfer_chlorine_west(west_swor_front, w_chem)
	transfers.transfer_chlorine_East(east_swor_front, e_chem)
	transfers.transfer_fluoride(west_swor_front, east_swor_front)

	transfers.transfer_chlorine_res_east(e_chem, east_table)
	transfers.transfer_chlorine_res_west(w_chem, west_table)

	transfers.transfer_distribution(w_chem, e_chem)

	inc_status_bar()

	loggers.log_bmr(bmr_wb, locations_data)
	loggers.log_ifmrs(west_ifmr, east_ifmr)
	wbooks.save_workbooks(west_wb, east_wb, west_path, east_path, chem_wb, chem_path, table_wb, table_path, midnight_wb, midnight_path)

	total_exceptions = wbooks.get_exceptions() + loggers.get_exceptions() + transfers.get_exceptions() + hd_scraper.get_exceptions() + dirs.get_exceptions()

	if total_exceptions > 0:
		print(f'{p.err()}Errors: {total_exceptions}\n')
	else:
		print(f'{p.ok()}Proccess complete with zero errors\n')

	inc_status_bar()
	
	print('\033[43m' + ('*' * 60))
	print('DATES ON MIDNIGHT SPREADSHEET ARE SUPPOSE TO BE OFF BY A DAY')
	print(('*' * 60) + '\033[0m')

	inc_status_bar()
	program_finish()

if __name__ == '__main__':
	root = Tk()

	root.title("Excel Automator")
	root.geometry('1100x500+100+100')

	lbl = Label(root, text="Select the working directory", font=('Arial', 14))
	lbl.place(x=410, rely=0.0)

	btn = Button(root, text="Browse", fg="white", command=clicked, bd=3, bg='grey')
	start = Button(root, text="Start", fg="white", command=main, bd=3, bg='grey')

	btn.place(x=500, y=30)
	start.place(x=385, y=150)
	start.configure(width=40)

	pb1 = Progressbar(root, orient=HORIZONTAL, length=293, mode='determinate')
	pb1.pack(expand=True)
	pb1.place(x=385, y=200)

	
	root.mainloop()


