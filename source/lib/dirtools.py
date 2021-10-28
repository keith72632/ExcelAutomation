from tkinter import *
from tkinter import filedialog, messagebox
import os
from pdf2image import convert_from_path

def create_directory_structure():
	dirs = [
	"West_Plant_Operations_Reports\\",
	"East_Plant_Operations_Reports\\",
	"MangoLogs\\",
	"DocumentsJPG\\files",
	"DocumentsPDF\\",
	"Chemical_Treatment_Records\\Chlorine_Tables\\"
	""
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

	
