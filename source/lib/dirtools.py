from tkinter import *
from tkinter import filedialog, messagebox
from openpyxl import Workbook, load_workbook
import os
from datetime import datetime
from pdf2image import convert_from_path
import traceback
import win32com.client

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
	o = win32com.client.Dispatch("Excel.Application")
	o.Visible = False
	wb = o.Workbooks.Open(file_path)
	wb.Worksheets(page_index).Select()
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

	try:
		export_page(file_path=west_path, pdf_path=pdf_paths[0], page_index=3)
		print('bmr pdf success')
	except:
		traceback.print_exc()		

	try:
		export_page(file_path=east_path, pdf_path=pdf_paths[1], page_index=1)
		print('east operations back pdf success')
	except:
		traceback.print_exc()		

	try:
		export_page(file_path=chem_path, pdf_path=pdf_paths[2], page_index=1)
		print('east chemical treatment record pdf success')
	except:
		traceback.print_exc()		

	# try:
	# 	export_page(file_path=east_path, pdf_path=pdf_paths[3], page_index=0)
	# 	print('east operations front pdf success')
	# except:
	# 	traceback.print_exc()		

	try:
		export_page(file_path=west_path, pdf_path=pdf_paths[4], page_index=1)
		print('west operations back pdf success')
	except:
		traceback.print_exc()		

	# try:
	# 	export_page(file_path=chem_path, pdf_path=pdf_paths[5], page_index=0)
	# 	print('west chemical treatment pdf success')
	# except:
	# 	traceback.print_exc()		

	# try:
	# 	export_page(file_path=west_path, pdf_path=pdf_paths[6], page_index=0)
	# 	print('bmr pdf success')
	# except:
	# 	traceback.print_exc()		

	

def convert_pdfs():
	folder = filedialog.askdirectory()
	res = messagebox.askyesno("Continue?", "Are you sure this is the correct working directory?")
	try:
		if res:
			pdflist = os.listdir(folder + "\\DocumentsPDF")
			for i in pdflist:
				print(i)

			for item in pdflist:
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

	
