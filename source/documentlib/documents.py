import traceback
from PIL import Image
from tkinter import messagebox
from pdf2image import convert_from_path

class Document:
	file = ' '
	file_out = ' '
	directory = ' '
	sig_width = 340
	sig_height = 40
	def __init__(self, file, file_out, directory):
		self.directory = directory
		self.file = self.directory + file
		self.file_out = self.directory + file_out
	


	def signDocs(self, x_pos, y_pos):

		signature = Image.open(self.directory + "\\DocumentsJPG\\files\\barry_signature_clean.jpg")
		newsize = (self.sig_width, self.sig_height)
		img1 = signature.resize(newsize)
		img2 = Image.open(self.file)
		area = (x_pos, y_pos, (x_pos + self.sig_width), (y_pos + self.sig_height))
		img2.paste(img1, area)
		print(f'img1 format: {signature.format} img1 size: {signature.size}')
		print(f'img2 format: {img2.format} img2 size:{img2.size}')

		print(f'signature size {img1.size}')
		img2.save(self.file_out, "JPEG")
		print('Saved')

	def get_file(self):
		print("self.file = " + self.file)
		return self.file

def sign_all(working_dir):
	print(f'Photoshop working dir {working_dir}')
	confirm = messagebox.askquestion('DocAuto Sign', "You are fixing to sign the documents in files. Continue?")
	if confirm =='yes':
		try:
			bmr_y_pos = 1900
			bmr_x_pos = 850
			bmr_file_in = "\\DocumentsJPG\\files\\bmr.jpeg"
			bmr_file_out = "\\DocumentsJPG\\finals\\bmrFinale.jpeg"
			bmr = Document(bmr_file_in, bmr_file_out, directory=working_dir)
			bmr.get_file()
			bmr.signDocs(bmr_x_pos, bmr_y_pos)
		except:
			print('Trouble opening BMR')
			messagebox.showinfo('BMR', "Could not sign BMR")
			traceback.print_exc()

		try:
			swor_front_y = 1945
			swor_front_x = 2100
			west_front_file_in = "\\DocumentsJPG\\files\\west_front.jpeg"
			west_front_file_out = "\\DocumentsJPG\\finals\\west_frontFinale.jpeg"
			west_front = Document(west_front_file_in, west_front_file_out, directory=working_dir)
			west_front.get_file()
			west_front.signDocs(swor_front_x, swor_front_y)
		except:
			print('Trouble opening West Surface Water Front')
			messagebox.showinfo('West Surface Water Operation Report(Front)', "Could not sign East Surface Water Operation Report")
			traceback.print_exc()


		try:
			swor_back_y = 1974
			swor_back_x = 2000
			west_back_file_in = "\\DocumentsJPG\\files\\west_back.jpeg"
			west_back_file_out = "\\DocumentsJPG\\finals\\west_backFinale.jpeg"
			west_back = Document(west_back_file_in, west_back_file_out, directory=working_dir)
			west_back.get_file()
			west_back.signDocs(swor_back_x, swor_back_y)
		except:
			print('Trouble opening West Surface Back')
			messagebox.showinfo('West Surface Water Operation Report(Back)', "Could not sign West Surface Water Operation Report")
			traceback.print_exc()


		try:
			swor_front_y = 1945
			swor_front_x = 2100
			west_front_file_in = "\\DocumentsJPG\\files\\east_front.jpeg"
			west_front_file_out = "\\DocumentsJPG\\finals\\east_frontFinale.jpeg"
			west_front = Document(west_front_file_in, west_front_file_out, directory=working_dir)
			west_front.get_file()
			west_front.signDocs(swor_front_x, swor_front_y)
		except:
			print('Trouble opening East Surface Water Front')
			messagebox.showinfo('East Surface Water Operation Report(Front)', "Could not sign East Surface Water Operation Report")
			traceback.print_exc()


		try:
			swor_back_y = 1975
			swor_back_x = 2000
			west_back_file_in = "\\DocumentsJPG\\files\\east_back.jpeg"
			west_back_file_out = "\\DocumentsJPG\\finals\\east_backFinale.jpeg"
			west_back = Document(west_back_file_in, west_back_file_out, directory=working_dir)
			west_back.get_file()
			west_back.signDocs(swor_back_x, swor_back_y)
		except:
			print('Trouble opening East Surface Water back')
			messagebox.showinfo('East Surface Water Operation Report(Back)', "Could not sign East Surface Water Operation Report")
			traceback.print_exc()

		try:
			ifmr_y = 1975
			ifmr_x = 350
			west_ifmr_first = "\\DocumentsJPG\\files\\west_ifmr_one.jpeg"
			west_ifmr_first_out = "\\DocumentsJPG\\finals\\west_ifmr_oneFinale.jpeg"
			w_ifmr_first = Document(west_ifmr_first, west_ifmr_first_out, directory=working_dir)
			w_ifmr_first.get_file()
			w_ifmr_first.signDocs(ifmr_x, ifmr_y)
		except:
			print('Trouble opening first page of West IFMR')
			messagebox.showinfo('West IFMR(First)', "Could not sign West IFMR")
			traceback.print_exc()

		try:
			ifmr_two_y = 1720
			ifmr_two_x = 350
			west_ifmr_second = "\\DocumentsJPG\\files\\west_ifmr_two.jpeg"
			west_ifmr_second_out = "\\DocumentsJPG\\finals\\west_ifmr_twoFinale.jpeg"
			w_ifmr_first = Document(west_ifmr_second, west_ifmr_second_out, directory=working_dir)
			w_ifmr_first.get_file()
			w_ifmr_first.signDocs(ifmr_two_x, ifmr_two_y)
		except:
			print('Trouble opening second page of West IFMR')
			messagebox.showinfo('West IFMR(First)', "Could not sign West IFMR")
			traceback.print_exc()


		try:
			ifmr_y = 1975
			ifmr_x = 350
			east_ifmr_first = "\\DocumentsJPG\\files\\east_ifmr_one.jpeg"
			east_ifmr_first_out = "\\DocumentsJPG\\finals\\east_ifmr_oneFinale.jpeg"
			e_ifmr_first = Document(east_ifmr_first, east_ifmr_first_out, directory=working_dir)
			e_ifmr_first.get_file()
			e_ifmr_first.signDocs(ifmr_x, ifmr_y)
		except:
			print('Trouble opening first page of East IFMR')
			messagebox.showinfo('East IFMR(First)', "Could not sign East IFMR")
			traceback.print_exc()


		try:
			ifmr_two_y = 1720
			ifmr_two_x = 350
			east_ifmr_second = "\\DocumentsJPG\\files\\east_ifmr_two.jpeg"
			east_ifmr_second_out = "\\DocumentsJPG\\finals\\east_ifmr_twoFinale.jpeg"
			e_ifmr_second = Document(east_ifmr_second, east_ifmr_second_out, directory=working_dir)
			e_ifmr_second.get_file()
			e_ifmr_second.signDocs(ifmr_two_x, ifmr_two_y)
		except:
			print('Trouble opening second page of East IFMR')
			messagebox.showinfo('East IFMR(Second)', "Could not sign East IFMR")
	messagebox.showinfo("DocAuto Sing", "Done")

	if confirm == 'no':
		pass