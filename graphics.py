from tkinter import *

def graphical():
	root = Tk()

	root.title("Excel Automator")
	root.geometry('900x400')

	lbl = Label(root, text="Excel File Automator. Choose Month")
	lbl.grid()

	txt = Entry(root, width=10)
	txt.grid(column=1, row=0)
	print(type(txt))

	def clicked():
		root.destroy()

	btn = Button(root, text="Start", fg="red", command=clicked)

	btn.grid(column=3, row=0)


	root.mainloop()