from openpyxl import Workbook, load_workbook
import os
from datetime import datetime
from loggers import *
from filelib import *
from workbooks import *



def main():

	west_path, east_path = get_file_from_date()

	west_wb, east_wb = activate_workbooks(west_path, east_path)
	w_active = west_wb.active
	e_active = east_wb.active

	log_rainfall(w_active, e_active)

	save_workbooks(west_wb, east_wb, west_path, east_path)


if __name__ == '__main__':
	main()

