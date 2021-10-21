from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Menubutton
import sys
from documentlib.documents import sign_all

INC_COUNT = 0

root = Tk()
pb1 = Progressbar(root, orient=HORIZONTAL, length=373, mode='determinate')

def background_image():
	img = PhotoImage(file="./excel_logo.png")
	canvas = Canvas(root, width=100, height=100)
	canvas.pack(expand=True, fill=BOTH)
	canvas.create_image(0, 0, image=img)

def start_btn(cmd):
	start = Button(root, text="Start", fg="green2", command=cmd, bd=3, bg='grey', font=12)
	start.place(relx=0.315, y=410)
	start.configure(width=40)

def dir_btn(cmd):
	btn = Button(root, text="Select Working Directory", fg="green2", command=cmd, bd=3, bg='grey', font=12)
	btn.place(relx=0.375, rely=0.1)
	btn.configure(width=25)


def sign_btn(cmd):
	btn = Button(root, text="Sign Documents", fg="white", command=cmd, bd=3, bg='grey')
	btn.place(relx=0.893, rely=0.001)
	btn.configure(width=15)

def prog_bar():
	pb1.pack(expand=True)
	pb1.place(relx=0.315, y=450)

def inc_status_bar(msg):
	root.update_idletasks()
	pb1['value'] += 7
	txt = Text(root)
	txt.insert(INSERT, msg)
	txt.configure(height=1, width=36)
	txt.place(relx=0.355, y=320)
	return 1

def prompt_error(msg):
	messagebox.showerror(title="Error", message=msg)

def get_inc_value(inc_count):
	return 100/inc_count

def program_finish():
	messagebox.showinfo("Spreadsheet", "Done")
	pb1['value'] = 0


def log_error(message):
	res = messagebox.askquestion('Yes|No', str(message))
	if res == 'yes':
		sys.exit()
	if res == 'no':
		sys.exit()

def menu():
	MONTHS = [
	"January",
	"February",
	"March",
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
	om.place(relx=0.25, rely=0.20)
	om.configure(width=33)

	return month

def bmr_plant_name():
	NAMES = [
	"CARROLL-BOONE WATER DISTRICT",
	]
	name = StringVar(root)
	name.set("Choose BMR")

	om = OptionMenu(root, name, *NAMES)
	om.place(relx=0.5, rely=0.20)
	om.configure(width=33)
	return name


def header():
	hd = Label(root, text="Monthly Report Spreadsheet Automator")
	hd.place(relx=0.315, rely=0.0)
	hd.configure(font=("Helvetica", 16), fg="green")