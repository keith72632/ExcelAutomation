from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Menubutton, Style
import sys
from documentlib.documents import sign_all
from PIL import Image, ImageTk

INC_COUNT = 0

root = Tk()
s = Style()
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
pb1 = Progressbar(root, orient=HORIZONTAL, length=373, mode='determinate', style="red.Horizontal.TProgressbar")

def create_icon(path):
	root.iconbitmap(path)

def center_img(path):
	myimg = ImageTk.PhotoImage(Image.open(path))
	mylabel= Label(root, image=myimg)
	mylabel.configure(width=220, height=220)
	mylabel.place(relx=.38, rely=.3)

def prog_bar_init():
	pb1.pack(expand=True)
	pb1.place(relx=0.5, rely=0.97, anchor='center')

def inc_status_bar(message, inc_no)->int:
	root.update_idletasks()
	pb1['value'] += inc_no
	txt = Text(root)
	txt.insert(INSERT, message)
	txt.configure(height=1, width=36)
	txt.place(relx=0.5, rely=0.84, anchor='center')
	return 1

def prompt_error(msg):
	messagebox.showerror(title="Error", message=msg)

def get_inc_value(inc_count)->int:
	return 100/inc_count

def program_finish():
	messagebox.showinfo("Spreadsheet", "Done")
	pb1['value'] = 0

def log_error(message):
	res = messagebox.askquestion('Yes|No', str(message))
	if res == 'yes':
		pass
	if res == 'no':
		sys.exit()

def menu():
	MONTHS = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
	]
	month = StringVar(root)
	month.set("Select Month")

	om = OptionMenu(root, month, *MONTHS)
	om.place(relx=0.35, rely=0.21, anchor='center')
	om.configure(width=33)

	return month

def bmr_plant_name():
	NAMES = [
	"CARROLL-BOONE WATER DISTRICT",
	]
	name = StringVar(root)
	name.set("Choose BMR")

	om = OptionMenu(root, name, *NAMES)
	om.place(relx=0.625, rely=0.21, anchor='center')
	om.configure(width=33)
	return name

def meter_fields():
	west = IntVar(root)
	east = IntVar(root)
	lbl1 = Label(root, text="Enter last West Plant Raw Meter Reading")
	lbl1.place(relx=0.35, rely=0.275, anchor='center')
	lbl1.configure(bg='SpringGreen4', fg='white', borderwidth=2, relief="raised")
	entry1 = Entry(root, bd=3, textvariable=west).place(relx=0.35, rely=0.325, anchor='center', width=242)
	lbl2 = Label(root, text="Enter last East Plant Raw Meter Reading")
	lbl2.place(relx=0.625, rely=0.275, anchor='center')
	lbl2.configure(bg='SpringGreen4', fg='white', borderwidth=2, relief="raised")
	entry2 = Entry(root, bd=3, textvariable=east).place(relx=0.625, rely=0.325, anchor='center', width=242)
	return west, east

def check_meter_fields(west, east):
	if west or east == 0:
		prompt_error('Invalid Meter Number')
		sys.exit()