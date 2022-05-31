from spreadsheets.loggers import Logger
from spreadsheets.transfers import Transfer
from spreadsheets.filelib import Directories
from spreadsheets.workbooks import Books
from web.soups import BmrScraper
from colorama import init
from lib.colors import Prompts
from tkinter import *
from tkinter import filedialog
from gui.visuals import *
from gui.buttons import *
from documentlib.documents import sign_all
from lib.dirtools import *
from lib.helpers import *
from PIL import Image, ImageTk


#TODO: Move this function somewhere else
def select_work_dir():
	global folderselect
	folderselect = filedialog.askdirectory()
	route = Label(text='Folder Selected (This needs to be your working directory):\n' + str(folderselect))
	route.place(relx=0.5, rely=0.13, anchor='center')
	route.configure(font=(12), fg="white", bg='SpringGreen4', borderwidth=2, relief="raised")
	print(f'Folder selected {folderselect}')
	global monthmenu
	monthmenu = menu()
	global plantname
	plantname = bmr_plant_name()
	sign_btn()
	global west, east
	west, east = meter_fields()


#TODO: Move this function somewhere else
def sign_btn():
	btn = Button(root, text="Sign Documents", fg="white", bd=3, bg='grey' ,command=lambda: sign_all(folderselect))
	btn.place(relx=0.861, rely=0.18)
	btn.configure(width=20)

def mainf():
	prog_bar_init()
	
	# check_meter_fields(west.get(), east.get())
	global INC_COUNT
	#url for bact sample data
	#needed to change text colors in terminal
	init()

	INC_COUNT += inc_status_bar(message="terminal colors initialized", inc_no=7)

	####################################################################################################
	#################            DIRECTORIES INIT                                       ################
	####################################################################################################
	
	dirs = Directories()
	INC_COUNT += inc_status_bar(message="Directories instance created", inc_no=7)
	
	p = Prompts()

	#takes folder selected in select_work_dir() filedialog
	try:
		dirs.set_working_dir(folderselect)
	except NameError:
		print(f'{p.err()}Please select a working directory')


	INC_COUNT += inc_status_bar(message="working directory set", inc_no=7)

	try:
		westpath, eastpath, chempath, tablepath, midnightpath = dirs.get_file_from_date(monthmenu=monthmenu.get())
	except KeyError:
		prompt_error("No month selected. Please select month, then click Start again")
		#resets the progress bar

	except NameError:
		prompt_error("Please select the Working_Directory")
		#resets the progress bar

	####################################################################################################
	#################            BOOKS INIT                                             ################
	####################################################################################################
	wbooks = Books(westpath, eastpath, chempath, tablepath, midnightpath)

	INC_COUNT += inc_status_bar(message="Workbook instance created", inc_no=7)
	wbooks.load_workbooks()
	wbooks.individual_pages_init()


	INC_COUNT += inc_status_bar(message="workbooks loaded", inc_no=7)

	w_active, e_active, c_active, table_active, midnight_active = \
		wbooks.west_wb.active, wbooks.east_wb.active, wbooks.chem_wb.active, wbooks.table_wb.active, wbooks.meter_wb.active

	####################################################################################################
	#################            BmrScraper INIT                                             ################
	####################################################################################################
	#scan of the health department website for the BMR data
	hd_scraper = BmrScraper(name=plantname.get())
	INC_COUNT += inc_status_bar(message="BmrScraper instance created", inc_no=7)

	locations_data = hd_scraper.scan_health_dep()
	hd_scraper.display_list_of_dicks(locations_data)
	INC_COUNT += inc_status_bar(message="BMR data gathered from health department", inc_no=7)


	####################################################################################################
	#################            LOGGER INIT                                            ################
	####################################################################################################
	loggers = Logger(
		west_front=wbooks.west_swor_front,
		east_front=wbooks.east_swor_front, 
		west_back=wbooks.west_swor_back,
		east_back=wbooks.east_swor_back, 
		midnight=wbooks.midnight_readings, 
		prevwest=int(west.get()), 
		preveast=int(east.get()), 
		month=monthmenu.get()
		)

	INC_COUNT += inc_status_bar(message="Logger instance created", inc_no=7)

	loggers.log_all()
	loggers.log_ifmrs(wbooks.west_ifmr, wbooks.east_ifmr, month=monthmenu.get())
	loggers.log_bmr(wbooks.bmr_wb, locations_data)


	INC_COUNT += inc_status_bar(message="BMR data logged to spreadsheet", inc_no=7)
	INC_COUNT += inc_status_bar(message="All data logged successfully", inc_no=7)


	####################################################################################################
	#################            TRANSFERS INIT                                         ################
	####################################################################################################
	transfers = Transfer(
		west_front=wbooks.west_swor_front, 
		east_front=wbooks.east_swor_front, 
		w_chem=wbooks.w_chem, 
		e_chem=wbooks.e_chem,
		west_table=wbooks.west_table, 
		east_table=wbooks.east_table
		)

	INC_COUNT += inc_status_bar(message="Transfer instance created", inc_no=7)

	transfers.transfer_all()

	INC_COUNT += inc_status_bar(message="transfering complete", inc_no=7)

	# wbooks.save_workbooks()
	# INC_COUNT += inc_status_bar(message="Workbooks Saved", inc_no=7)

	process_exceptions(wbooks.get_exceptions() + loggers.get_exceptions() + transfers.get_exceptions() + hd_scraper.get_exceptions() + dirs.get_exceptions())

	####################################################################################################
	#################            CLEANUP                                                ################
	####################################################################################################

	del loggers, wbooks, transfers, hd_scraper

	INC_COUNT += inc_status_bar(message="exceptions counted", inc_no=7)
	
	cmd_banner('DATES ON MIDNIGHT SPREADSHEET ARE SUPPOSE TO BE OFF BY A DAY')
	INC_COUNT += inc_status_bar(message="finished", inc_no=7)

	program_finish()

if __name__ == '__main__':
	root.title("ExcelAuto")
	root.geometry('1100x500+375+225')
	iconpath='C:\\Users\\CBWD\\Documents\\Old PC\\Projects\\Python\\ExcelAuto\\Photos\\excelicon.ico'
	imgpath = 'C:\\Users\\CBWD\\Documents\\Old PC\\Projects\\Python\\ExcelAuto\\Photos\\excelimg.png'
	logopath = 'C:\\Users\\CBWD\\Documents\\Old PC\\Projects\\Python\\ExcelAuto\\Photos\\black_python.png'
	# header()
	#pass functions as argument to be used as commands in gui buttons
	#Start button calls mainf
	start_btn(cmd=mainf)
	dir_btn(cmd=select_work_dir)
	convert_btn(cmd=convert_pdfs)
	print_pdf_btn(cmd=print_pdfs)
	create_dirs_btn(cmd=create_directory_structure)
	create_icon(path=iconpath)
	
	myimg = ImageTk.PhotoImage(Image.open(imgpath))
	mylabel= Label(root, image=myimg)
	mylabel.configure(width=220, height=220)
	mylabel.place(relx=.5, rely=.59, anchor='center')

	pimg = ImageTk.PhotoImage(Image.open(logopath))
	lbl = Label(root, image=pimg)
	lbl.place(relx=0, rely=0)	


	root.mainloop()

#174705
#555372
