from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Menubutton
import sys
from gui.visuals import root

def start_btn(cmd):
	start = Button(root, text="Start", fg="white", command=cmd, bd=3, bg='grey', font=12)
	start.place(relx=0.5, rely=0.91, anchor='center')
	start.configure(width=40)

def dir_btn(cmd):
	btn = Button(root, text="Select Working Directory", fg="white", command=cmd, bd=3, bg='grey', font=12)
	btn.place(relx=0.5, rely=0.04, anchor='center')
	btn.configure(width=25)

def sign_btn(cmd):
	btn = Button(root, text="Sign Documents", fg="white", command=cmd, bd=3, bg='grey')
	btn.place(relx=0.893, rely=0.2)
	btn.configure(width=15)

def create_dirs_btn(cmd):
	btn = Button(root, text="Create Directory Structure", fg="white", bd=3, bg='grey', command=cmd)
	btn.place(relx=0.861, rely=0.001)
	btn.configure(width=20)