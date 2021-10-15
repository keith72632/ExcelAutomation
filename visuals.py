from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar

root = Tk()
pb1 = Progressbar(root, orient=HORIZONTAL, length=293, mode='determinate')

def browse_button():
	btn = Button(root, text="Browse", fg="white", command=clicked, bd=3, bg='grey')
	btn.place(x=500, y=30)

def prog_bar():
	pb1.pack(expand=True)
	pb1.place(x=385, y=200)

def inc_status_bar(msg):
	root.update_idletasks()
	pb1['value'] += 12
	txt = Text(root)
	txt.insert(INSERT, msg)
	txt.configure(height=1, width=36)
	txt.place(x=385, y=180)


def program_finish():
	messagebox.showinfo("Done", "Done")
	root.destroy()


def log_error(root, message):
	lbl = Label(root, text="Select the working directory", font=('Arial', 14))



