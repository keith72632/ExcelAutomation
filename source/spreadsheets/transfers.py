from lib.colors import Prompts
from lib.number_generator import get_random_number_list
from spreadsheets.filelib import Directories
import os
import traceback
from datetime import datetime

d = Directories()

#Transfers data from various spreadsheets
class Transfer:
	def __init__(self, west_front, east_front, w_chem, e_chem, west_table, east_table):
		self._west_front = west_front
		self._east_front = east_front
		self._w_chem = w_chem
		self._e_chem = e_chem
		self._west_table = west_table
		self._east_table = east_table

	def __del__(self):
		print('Transfer destoyed')
		
	EXCEPTIONS = 0
	#Tranfers the meter reading from the West Operations Report to the East Chemical Treatment Record
	def transfer_meters_west(self):
		p = Prompts()
		#cells from the West operations report
		op_meter_cols = self._west_front['B']
		op_meters = op_meter_cols[8:38]

		ct_meter_cols = self._w_chem['A']
		ct_meters = ct_meter_cols[9:39]

		try:
			for i, day in enumerate(op_meters):
				ct_meters[i].value = day.value
			print(f'{p.note()}West Raw meter values transfered from West SWOR to West Chemical Treatment Record') 
			return ct_meters
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West meter data from Operations Report to Chemical Treatment\n')


	#Transfers the meter readings from the East Operations Report to the East Chemical Treatment Record
	def transfer_meters_east(self):
		p = Prompts()
		#cells from the East operations report
		
		op_meter_cols = self._east_front['B']
		op_meters = op_meter_cols[8:38]

		ct_meter_cols = self._e_chem['A']
		ct_meters = ct_meter_cols[9:39]
		
		try:
			for i, day in enumerate(op_meters):
				ct_meters[i].value = day.value
			print(f'{p.note()}East Raw meter values transfered from East SWOR to East Chemical Treatment Record') 
			return ct_meters
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering East meter data\n')
			traceback.print_exc()
			os.system('pause')


	#The values in total raw water flow on the Operations Report are calculated via formula, which openpyxl cannot transfer
	#this function calculates the first flow value in the Chemical treatment record and fills the rest with a formula within excel
	def transfer_flow_west(self):
		p = Prompts()

		try:
			if self._west_front['B9'].value:
				root_reading = (self._west_front['B9'].value - self._west_front['B5'].value) / 1000
				self._w_chem['C10'].value = root_reading
			print(f'{p.note()}West Raw Flow root value transfered from West SWOR to West Chemical Treatment Record') 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West flow data\n')
			print((self._west_front['B9'].value - self._west_front['B5'].value) / 1000)
			os.system('pause')


	#The values in total raw water flow on the Operations Report are calculated via formula, which openpyxl cannot transfer
	#this function calculates the first flow value in the Chemical treatment record and fills the rest with a formula within excel
	def transfer_flow_east(self):
		p = Prompts()

		try:
			root_reading = (self._east_front['B9'].value - self._east_front['B5'].value) / 1000
			self._e_chem['C10'].value = root_reading
			print(f'{p.note()}East Raw Flow root value transfered from East SWOR to East Chemical Treatment Record') 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering East flow data\n')
			traceback.print_exc()
	#Transfers rainfall data from West Operations Report to East Operations Report
	def transfer_rainfall(self):
		p = Prompts()

		west_cols = self._west_front['G']
		west = west_cols[8:38]

		east_cols = self._east_front['G']
		east = east_cols[8:38]

		try:
			for i, day in enumerate(west):
				east[i].value = day.value
			print(f'{p.note()}West Rainfall values copied from West SWOR to East SWOR')

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring rainfall data\n')
			os.system('pause')

	#Transfers Finish pH data from the West Operations report to the East Operations Report
	def transfer_finish_pH(self):
		p = Prompts()

		west_cols = self._west_front['S']
		west = west_cols[8:38]

		east_cols = self._east_front['R']
		east = east_cols[8:38]

		try:
			for i, day in enumerate(west):
				east[i].value = day.value
			print(f'{p.note()}West Finish pH values copied from West SWOR to East SWOR')
			return west

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring finish pH data\n')
			os.system('pause')



	#Transfer total chlorine data from the West Operations Report to the East Operations Report
	def transfer_total(self):
		p = Prompts()

		west_cols = self._west_front['AI']
		west = west_cols[8:38]
		east_cols = self._east_front['AH']
		east = east_cols[8:38]

		try:
			for i, day in enumerate(west):
				east[i].value = day.value
			print(f'{p.note()}West Total Chlorine values copied from West SWOR to East SWOR')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring total chlorine data\n')
			os.system('pause')



	#Copies Chloramine Data from the West Operations Report to the East Operation Report
	def transfer_chloramine(self):
		p = Prompts()

		west_cols = self._west_front['AJ']
		west = west_cols[8:38]
		east_cols = self._east_front['AI']
		east = east_cols[8:38]

		try:
			for i, day in enumerate(west):
				east[i].value = day.value
			print(f'{p.note()}West Chloramine values copied from West SWOR to East SWOR')

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring chloramine data\n')
			os.system('pause')


	#Transfers fluoride residual data from West Operations Report to the East Operations Report
	def transfer_fluoride(self):
		p = Prompts()

		west_cols = self._west_front['O']
		west = west_cols[8:38]
		east_cols = self._east_front['O']
		east = east_cols[8:38]

		try:
			for i, day in enumerate(west):
				east[i].value = day.value
			print(f'{p.note()}West Fluoride value copied from West SWOR to East SWOR')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring fluroide data\n')
			os.system('pause')


	#Transfers the chlorine readings (in PPD) from the West Operations Report to the West Chemical Treatment Record
	def transfer_chlorine_west(self):
		p = Prompts()

		op_cols = self._west_front['J']
		op = op_cols[8:38]
		ct_cols = self._w_chem['D']
		ct = ct_cols[9:39]

		try:
			for i, day in enumerate(op):
				ct[i].value = day.value
			print(f'{p.note()}West Chlorine lbs used value transfered from West SWOR to West Chemical Treatment Record')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West Chlorine data\n')
			os.system('pause')


	#Transers the chlorine readings (in PPD) from the East Operations Report to the West Chemical Treatment Record
	def transfer_chlorine_east(self):
		p = Prompts()

		op_cols = self._east_front['J']
		op = op_cols[8:38]
		ct_cols = self._e_chem['D']
		ct = ct_cols[9:39]

		try:
			for i, day in enumerate(op):
				ct[i].value = day.value
			print(f'{p.note()}East Chlorine lbs used value transfered from East SWOR to East Chemical Treatment Record')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering East Chlorine data\n')
			os.system('pause')


	#Transfer Chlrone residuals from Chlorine Table to East Chemical Treatment Record
	def transfer_chlorine_res_east(self):
		p = Prompts()
		m = datetime.now().month
		days = 32 if m % 2 == 0 else 31
		free_values = get_random_number_list(length=days, min_num=0.05, max_num=0.25)
		total_values = get_random_number_list(length=days, min_num=1.20, max_num=2.50)
		ct_free_cols = self._e_chem['F']
		ct_free = ct_free_cols[9:39]

		ct_total_cols = self._e_chem['G']
		ct_total = ct_total_cols[9:39]

		table_free_cols = self._east_table['A']
		table_free = table_free_cols[2:32]

		table_total_cols = self._east_table['A']
		table_total = table_total_cols[36:66]

		try:
			for i, day in enumerate(ct_free):
				day.value = free_values[i]
			print(f'{p.note()}Free Chlorine Table values transfered to East Chemical Treatment Record')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering east free residuals\n')
			os.system('pause')

		try:
			for i, day in enumerate(ct_total):
				day.value = total_values[i]
			print(f'{p.note()}Total Chlorine Table values transfered to East Chemical Treatment Record')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering east residuals\n')
			os.system('pause')


	def transfer_chlorine_res_west(self):
		p = Prompts()
		m = datetime.now().month
		
		#if month has 30 days or 31
		days = 32 if m % 2 == 0 else 31
		
		free_values = get_random_number_list(length=days, min_num=0.05, max_num=0.25)
		total_values = get_random_number_list(length=days, min_num=1.20, max_num=2.50)

		ct_free_cols = self._w_chem['F']
		ct_free = ct_free_cols[9:39]

		ct_total_cols = self._w_chem['G']
		ct_total = ct_total_cols[9:39]

		table_free_cols = self._west_table['A']
		table_free = table_free_cols[2:32]

		table_total_cols = self._west_table['A']
		table_total = table_total_cols[36:66]

		try:
			for i, day in enumerate(ct_free):
				day.value = free_values[i]
			print(f'{p.note()}Free Chlorine Table values transfered to West Chemical Treatment Record')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West Free residuals\n')
			os.system('pause')

		try:
			for i, day in enumerate(ct_total):
				day.value = total_values[i]
			print(f'{p.note()}Total Chlorine Table values transfered to West Chemical Treatment Record')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West Total residuals\n')
			os.system('pause')


	def transfer_distribution(self):
		p = Prompts()
		cells = (
			'I10', 'I12', 'I14', 'I16', 'I18',
			'I20', 'I22', 'I24', 'I26', 'I28'
		)

		try:
			for day in cells:
				self._e_chem[day].value = self._w_chem[day].value
			print(f'{p.note()}Distribution Meter Values transfered from West Chemical Treatment Record to East Chemical Treatment Record')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering Distribution Meter Readings\n')
			os.system('pause')

	def transfer_all(self):
		self.transfer_meters_west()
		self.transfer_meters_east()
		self.transfer_rainfall()
		self.transfer_finish_pH()
		self.transfer_total()
		self.transfer_chloramine()
		self.transfer_flow_west()
		self.transfer_flow_east()
		self.transfer_chlorine_west()
		self.transfer_chlorine_east()
		self.transfer_fluoride()
		self.transfer_chlorine_res_east()
		self.transfer_chlorine_res_west()
		self.transfer_distribution()

	def get_exceptions(self):
		return self.EXCEPTIONS