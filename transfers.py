from colors import Prompts
from filelib import Directories
import os

d = Directories()

#Transfers data from various spreadsheets
class Transfer:
	def __init__(self):
		pass
	EXCEPTIONS = 0
	#Tranfers the meter reading from the West Operations Report to the East Chemical Treatment Record
	def transfer_meters_west(self, w_active, w_chem):
		p = Prompts()
		#cells from the West operations report
		op_meter_cols = w_active['B']
		op_meters = op_meter_cols[8:38]

		ct_meter_cols = w_chem['A']
		ct_meters = ct_meter_cols[9:39]

		try:
			for i, day in enumerate(op_meters):
				ct_meters[i].value = day.value
			print("West Raw meter values transfered from West SWOR to West Chemical Treatment Record") 
			return ct_meters
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West meter data from Operations Report to Chemical Treatment\n')
		os.system('pause')


	#Transfers the meter readings from the East Operations Report to the East Chemical Treatment Record
	def transfer_meters_east(self, e_active, e_chem):
		p = Prompts()
		#cells from the East operations report
		
		op_meter_cols = e_active['B']
		op_meters = op_meter_cols[8:38]

		ct_meter_cols = e_chem['A']
		ct_meters = ct_meter_cols[9:39]
		
		try:
			for i, day in enumerate(op_meters):
				ct_meters[i].value = day.value
			print("East Raw meter values transfered from East SWOR to East Chemical Treatment Record") 
			return ct_meters
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering East meter data\n')
			traceback.print_exc()
			os.system('pause')


	#The values in total raw water flow on the Operations Report are calculated via formula, which openpyxl cannot transfer
	#this function calculates the first flow value in the Chemical treatment record and fills the rest with a formula within excel
	def transfer_flow_west(self, w_active, w_chem):
		p = Prompts()

		try:
			if w_active['B9'].value:
				root_reading = (w_active['B9'].value - w_active['B5'].value) / 1000
				w_chem['C10'].value = root_reading
			print("West Raw Flow root value transfered from West SWOR to West Chemical Treatment Record") 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West flow data\n')
			os.system('pause')


	#The values in total raw water flow on the Operations Report are calculated via formula, which openpyxl cannot transfer
	#this function calculates the first flow value in the Chemical treatment record and fills the rest with a formula within excel
	def transfer_flow_east(self, e_active, e_chem):
		p = Prompts()

		try:
			root_reading = (e_active['B9'].value - e_active['B5'].value) / 1000
			e_chem['C10'].value = root_reading
			print("East Raw Flow root value transfered from East SWOR to East Chemical Treatment Record") 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering East meter data\n')
			os.system('pause')

	#Transfers rainfall data from West Operations Report to East Operations Report
	def transfer_rainfall(self, w_active, e_active):
		p = Prompts()

		west_cols = w_active['G']
		west = west_cols[8:38]

		east_cols = e_active['G']
		east = east_cols[8:38]

		try:
			for i, day in enumerate(west):
				east[i].value = day.value
			print("West Rainfall values copied from West SWOR to East SWOR")

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring rainfall data\n')
			os.system('pause')

	#Transfers Finish pH data from the West Operations report to the East Operations Report
	def transfer_finish_pH(self, w_active, e_active):
		p = Prompts()

		west_cols = w_active['S']
		west = west_cols[8:38]

		east_cols = e_active['R']
		east = east_cols[8:38]

		try:
			for i, day in enumerate(west):
				east[i].value = day.value
			print("West Finish pH values copied from West SWOR to East SWOR")
			return west

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring finish pH data\n')
			os.system('pause')



	#Transfer total chlorine data from the West Operations Report to the East Operations Report
	def transfer_total(self, w_active, e_active):
		p = Prompts()

		west_cols = w_active['AI']
		west = west_cols[8:38]
		east_cols = e_active['AH']
		east = east_cols[8:38]

		try:
			for i, day in enumerate(west):
				east[i].value = day.value
			print("West Total Chlorine values copied from West SWOR to East SWOR")
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring total chlorine data\n')
			os.system('pause')



	#Copies Chloramine Data from the West Operations Report to the East Operation Report
	def transfer_chloramine(self, w_active, e_active):
		p = Prompts()

		west_cols = w_active['AJ']
		west = west_cols[8:38]
		east_cols = e_active['AI']
		east = east_cols[8:38]

		try:
			for i, day in enumerate(west):
				east[i].value = day.value
			print("West Chloramine values copied from West SWOR to East SWOR")

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring chloramine data\n')
			os.system('pause')


	#Transfers fluoride residual data from West Operations Report to the East Operations Report
	def transfer_fluoride(self, w_active, e_active):
		p = Prompts()

		west_cols = w_active['O']
		west = west_cols[8:38]
		east_cols = e_active['O']
		east = east_cols[8:38]

		try:
			for i, day in enumerate(west):
				east[i].value = day.value
			print("West Fluoride value copied from West SWOR to East SWOR")
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring fluroide data\n')
			os.system('pause')


	#Transfers the chlorine readings (in PPD) from the West Operations Report to the West Chemical Treatment Record
	def transfer_chlorine_west(self, w_active, w_chem):
		p = Prompts()

		op_cols = w_active['J']
		op = op_cols[8:38]
		ct_cols = w_chem['D']
		ct = ct_cols[9:39]

		try:
			for i, day in enumerate(op):
				ct[i].value = day.value
			print("West Chlorine lbs used value transfered from West SWOR to West Chemical Treatment Record")
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West Chlorine data\n')
			os.system('pause')


	#Transers the chlorine readings (in PPD) from the East Operations Report to the West Chemical Treatment Record
	def transfer_chlorine_East(self, e_active, e_chem):
		p = Prompts()

		op_cols = e_active['J']
		op = op_cols[8:38]
		ct_cols = e_chem['D']
		ct = ct_cols[9:39]

		try:
			for i, day in enumerate(op):
				ct[i].value = day.value
			print("East Chlorine lbs used value transfered from East SWOR to East Chemical Treatment Record")
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering East Chlorine data\n')
			os.system('pause')


	#Transfer Chlrone residuals from Chlorine Table to East Chemical Treatment Record
	def transfer_chlorine_res_east(self, east_chem, east_table):
		p = Prompts()

		ct_free_cols = east_chem['F']
		ct_free = ct_free_cols[9:39]

		ct_total_cols = east_chem['G']
		ct_total = ct_total_cols[9:39]

		table_free_cols = east_table['A']
		table_free = table_free_cols[2:32]

		table_total_cols = east_table['A']
		table_total = table_total_cols[36:66]

		try:
			for i, day in enumerate(ct_free):
				day.value = table_free[i].value
			print("Free Chlorine Table values transfered to East Chemical Treatment Record")
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering east free residuals\n')
			os.system('pause')

		try:
			for i, day in enumerate(ct_total):
				day.value = table_total[i].value
			print("Total Chlorine Table values transfered to East Chemical Treatment Record")
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering east residuals\n')
			os.system('pause')


	def transfer_chlorine_res_west(self, west_chem, west_table):
		p = Prompts()

		ct_free_cols = west_chem['F']
		ct_free = ct_free_cols[9:39]

		ct_total_cols = west_chem['G']
		ct_total = ct_total_cols[9:39]

		table_free_cols = west_table['A']
		table_free = table_free_cols[2:32]

		table_total_cols = west_table['A']
		table_total = table_total_cols[36:66]

		try:
			for i, day in enumerate(ct_free):
				day.value = table_free[i].value
			print("Free Chlorine Table values transfered to West Chemical Treatment Record")
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West Free residuals\n')
			os.system('pause')

		try:
			for i, day in enumerate(ct_total):
				day.value = table_total[i].value
			print("Total Chlorine Table values transfered to West Chemical Treatment Record")
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West Total residuals\n')
			os.system('pause')


	def transfer_distribution(self, west_chem, east_chem):
		p = Prompts()
		cells = (
			'I10', 'I12', 'I14', 'I16', 'I18',
			'I20', 'I22', 'I24', 'I26', 'I28'
		)

		try:
			for day in cells:
				east_chem[day].value = west_chem[day].value
			print("Distribution Meter Values transfered from West Chemical Treatment Record to East Chemical Treatment Record")
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering Distribution Meter Readings\n')
			os.system('pause')

	def get_exceptions(self):
		return self.EXCEPTIONS