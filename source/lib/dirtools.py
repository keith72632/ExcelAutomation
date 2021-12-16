from tkinter import *
from tkinter import filedialog, messagebox
from openpyxl import Workbook, load_workbook
import os
from datetime import datetime
from pdf2image import convert_from_path
import traceback
import win32com.client
from gui.visuals import pb1, prog_bar_init, inc_status_bar

def create_directory_structure():
	dirs = [
	"West_Plant_Operations_Reports\\",
	"East_Plant_Operations_Reports\\",
	"MangoLogs\\",
	"DocumentsJPG\\files",
	"DocumentsPDF\\",
	"Chemical_Treatment_Records\\Chlorine_Tables\\"
	]
	folder = filedialog.askdirectory()
	res = messagebox.askyesno("Continue?", "Are you sure this is the correct location for Working_Directory ?")
	if res:
		try:
			for i in dirs:
				os.makedirs(folder + "\\Working_Directory\\" + i)
			messagebox.showinfo('Done', 'Directories Created')
		except FileExistsError:
			messagebox.showerror("Error", "Directories already exist")
	else:
		pass

def export_page(file_path, pdf_path, page_index):
	files = os.listdir('.')
	o = win32com.client.Dispatch("Excel.Application")
	o.Visible = False
	wb = o.Workbooks.Open(file_path)
	wb.Worksheets(int(page_index)).Select()
	wb.ActiveSheet.ExportAsFixedFormat(0, pdf_path)

def print_pdfs():
	dirs = [
	"/West_Plant_Operations_Reports/",
	"/East_Plant_Operations_Reports/",
	"/Chemical_Treatment_Records/"
	]
	working_dir = filedialog.askdirectory()
	west_files = os.listdir(working_dir + dirs[0])
	east_files = os.listdir(working_dir + dirs[1])
	chem_files = os.listdir(working_dir + dirs[2])

	month = (datetime.now().month) - 1

	west_file = [file for file in west_files if file.startswith(str(month))]
	east_file = [file for file in east_files if file.startswith(str(month))]
	chem_file = [file for file in chem_files if file.startswith(str(month))]

	west_path = working_dir + dirs[0] + west_file[0]
	east_path = working_dir + dirs[1] + east_file[0]
	chem_path = working_dir + dirs[2] + chem_file[0]

	pdf_paths = [
		r"c:\\Users\\Carroll Boone Water\\Documents\\Working_Directory\\DocumentsPDF\\bmr.pdf",
		r"c:\\Users\\Carroll Boone Water\\Documents\\Working_Directory\\DocumentsPDF\\east_back.pdf",
		r"c:\\Users\\Carroll Boone Water\\Documents\\Working_Directory\\DocumentsPDF\\east_chemical_treatment.pdf",
		r"c:\\Users\\Carroll Boone Water\\Documents\\Working_Directory\\DocumentsPDF\\east_front.pdf",
		r"c:\\Users\\Carroll Boone Water\\Documents\\Working_Directory\\DocumentsPDF\\west_back.pdf",
		r"c:\\Users\\Carroll Boone Water\\Documents\\Working_Directory\\DocumentsPDF\\west_chemical_treatment.pdf",
		r"c:\\Users\\Carroll Boone Water\\Documents\\Working_Directory\\DocumentsPDF\\west_front.pdf",
	]
	
	res = messagebox.askyesno("Continue?", "Are you sure this is the correct location for Working_Directory ?")

	if res:
		prog_bar_init()

		try:
			msg = 'bmr pdf success'
			export_page(file_path=west_path, pdf_path=pdf_paths[0], page_index=3)
			print(msg)
			inc_status_bar(message=msg, inc_no=15)
		except:
			traceback.print_exc()		

		try:
			msg = 'east operations back pdf success'
			export_page(file_path=east_path, pdf_path=pdf_paths[1], page_index=1)
			print(msg)
			inc_status_bar(message=msg, inc_no=15)
		except:
			traceback.print_exc()		

		try:
			msg = 'east chemical treatment record pdf success'
			export_page(file_path=chem_path, pdf_path=pdf_paths[2], page_index=1)
			print(msg)
			inc_status_bar(message=msg, inc_no=15)
		except:
			traceback.print_exc()		

		try:
			msg = 'east operations report front pdf success'
			o = win32com.client.Dispatch("Excel.Application")
			o.Visible = False
			wb = o.Workbooks.Open(east_path)
			sheet_names = [sheet.Name for sheet in wb.Sheets]
			index = sheet_names.index('SWO&R Front Side')
			wb.Worksheets('SWO&R Front Side').Select()
			wb.ActiveSheet.ExportAsFixedFormat(0, pdf_paths[3])
			print(msg)
			inc_status_bar(message=msg, inc_no=15)
		except:
			traceback.print_exc()


		try:
			msg = 'west operations back pdf success'
			export_page(file_path=west_path, pdf_path=pdf_paths[4], page_index=1)
			print(msg)
			inc_status_bar(message=msg, inc_no=15)
		except:
			traceback.print_exc()	

		try:
			msg = 'west chemical treatment record pdf success'
			o = win32com.client.Dispatch("Excel.Application")
			o.Visible = False
			wb = o.Workbooks.Open(chem_path)
			sheet_names = [sheet.Name for sheet in wb.Sheets]
			index = sheet_names.index('West')
			wb.Worksheets('West').Select()
			wb.ActiveSheet.ExportAsFixedFormat(0, pdf_paths[5])
			print(msg)
			inc_status_bar(message=msg, inc_no=15)
		except:
			traceback.print_exc()	

		try:
			msg = 'west operations report front pdf success'
			o = win32com.client.Dispatch("Excel.Application")
			o.Visible = False
			wb = o.Workbooks.Open(west_path)
			sheet_names = [sheet.Name for sheet in wb.Sheets]
			index = sheet_names.index('SWO&R Front Side')
			wb.Worksheets('SWO&R Front Side').Select()
			wb.ActiveSheet.ExportAsFixedFormat(0, pdf_paths[6])
			print(msg)
			inc_status_bar(message=msg, inc_no=15)
		except:
			traceback.print_exc()

		messagebox.showinfo("Done", "PDFs printed")


def convert_pdfs():
	prog_bar_init()
	folder = filedialog.askdirectory()
	res = messagebox.askyesno("Continue?", "Are you sure this is the correct working directory?")
	try:
		if res:
			pdflist = os.listdir(folder + "\\DocumentsPDF")
			for i in pdflist:
				print(i)

			for item in pdflist:
				msg = f'{item} converted to jpeg'
				inc_status_bar(message=msg, inc_no=12)
				pth = folder + "\\DocumentsPDF\\" + item
				savepath = folder + "\\DocumentsJPG\\files\\" + item
				pages = convert_from_path(pth)
				img = savepath.replace(".pdf", "")
				for page in pages:
					jpeg_file = img + '.jpeg'
					page.save(jpeg_file)
		messagebox.showinfo("Done", "PDF file Converted to JPEG")
	except:
		messagebox.showerror("Error", "Could not convert pdf files to jpeg")

	
