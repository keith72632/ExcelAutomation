from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Menubutton
import sys
from gui.visuals import root
from pdf2image import convert_from_path

def start_btn(cmd):
	start = Button(root, text="Start", fg="white", command=cmd, bd=3, bg='grey', font=12)
	start.place(relx=0.5, rely=0.91, anchor='center')
	start.configure(width=40)

def dir_btn(cmd):
	btn = Button(root, text="Select Working Directory", fg="white", command=cmd, bd=3, bg='grey', font=12)
	btn.place(relx=0.5, rely=0.04, anchor='center')
	btn.configure(width=25)

def print_pdf_btn(cmd):
	btn = Button(root, text="Print PDFs", fg='white', command=cmd, bd=3, bg='grey')
	btn.place(relx=0.861, rely=0.06)
	btn.configure(width=20)

def convert_btn(cmd):
	btn = Button(root, text="Convert PDFs to JPGs", fg='white', command=cmd, bd=3, bg='grey')
	btn.place(relx=0.861, rely=0.12)
	btn.configure(width=20)

def create_dirs_btn(cmd):
	btn = Button(root, text="Create Directory Structure", fg="white", bd=3, bg='grey', command=cmd)
	btn.place(relx=0.861, rely=0.001)
	btn.configure(width=20)