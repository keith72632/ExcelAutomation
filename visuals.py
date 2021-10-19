from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Menubutton
import sys

INC_COUNT = 0

root = Tk()
pb1 = Progressbar(root, orient=HORIZONTAL, length=293, mode='determinate')

def start_btn(cmd):
	start = Button(root, text="Start", fg="lime green", command=cmd, bd=3, bg='grey')
	start.place(relx=0.355, y=410)
	start.configure(width=40)

def dir_btn(cmd):
	btn = Button(root, text="Select Working Directory", fg="lime green", command=cmd, bd=3, bg='grey')
	btn.place(relx=0.4, rely=0.1)
	btn.configure(width=25)

def browse_button():
	btn = Button(root, text="Browse", fg="white", command=clicked, bd=3, bg='grey')
	btn.place(x=500, y=30)

def prog_bar():
	pb1.pack(expand=True)
	pb1.place(relx=0.355, y=450)

def inc_status_bar(msg):
	root.update_idletasks()
	pb1['value'] += 5
	txt = Text(root)
	txt.insert(INSERT, msg)
	txt.configure(height=1, width=36)
	txt.place(relx=0.355, y=320)
	return 1

def throw_error(msg):
	messagebox.showerror(title="Error", message=msg)

def get_inc_value(inc_count):
	return 100/inc_count

def program_finish():
	messagebox.showinfo("Done", "Done")
	root.destroy()


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
	om.place(relx=0.4, rely=0.20)
	om.configure(width=24)

	return month


def header():
	hd = Label(root, text="Monthly Report Spreadsheet Automator")
	hd.place(relx=0.315, rely=0.0)
	hd.configure(font=("Helvetica", 16), fg="green")