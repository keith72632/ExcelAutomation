from tkinter import *
from tkinter import filedialog, messagebox
import os

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