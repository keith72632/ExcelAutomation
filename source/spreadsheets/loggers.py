from lib.colors import Prompts
from spreadsheets.filelib import Directories
import traceback
import os
from gui.visuals import prompt_error
from datetime import datetime

d = Directories()

#Logs data to spreadsheets from various sources
class Logger:
	_row_len = 38
	def __init__(self, west_front, east_front, west_back, east_back, midnight, prevwest, preveast, month):
		self._west_front = west_front
		self._east_front = east_front
		self._west_back = west_back
		self._east_back = east_back
		self._midnight = midnight
		self._prevwest = prevwest
		self._preveast = preveast
		self._month = month

	def __del__(self):
		print('Logger Destroyed')

	EXCEPTIONS = 0

	#logs meter numbers to SWOR from mango spreadshett
	def log_meters(self):
		p = Prompts()

		west_raw_cols = self._midnight['B']
		west_raw = west_raw_cols[5:35]

		west_swor_meter_cols = self._west_front['B']
		west_swor_raw = west_swor_meter_cols[8:self._row_len]

		east_raw_cols = self._midnight['I']
		east_raw = east_raw_cols[5:35]

		east_swor_meter_cols = self._east_front['B']
		east_swor_raw = east_swor_meter_cols[8:self._row_len]

		try:
			self._west_front['AI50'].value = datetime.today()
			self._east_front['AH50'].value = datetime.today()
		except:
			print(f'{p.err()}Could not log date on front of SWOR')
			traceback.print_exc()

		try:
			self._west_front['AG2'].value = self._month
			self._east_front['AF2'].value = self._month
		except:
			print(f'{p.err()}Could not log month on front of SWOR')
			traceback.print_exc()

		try:
			self._west_front['B5'].value = self._prevwest
			self._east_front['B5'].value = self._preveast
		except:
			print(f'{p.err()}Could not log previous meter numbers')
			traceback.print_exc()
			prompt_error("Could not log previous meter number")

		
		try:
			for i, day in enumerate(west_swor_raw):
				day.value = west_raw[i].value 
			print(f'{p.note()}West meter numbers from Midnight readings successfully logged')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Raw Meter numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()
			prompt_error("Error reading West Raw Meter value from Midnight Spreadsheet")

		try:
			for i, day in enumerate(east_swor_raw):
				day.value = east_raw[i].value 
			print(f'{p.note()}East meter numbers from Midnight Readings successfully logged')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Raw Meter numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()
			prompt_error("Error reading Easr Raw Meter value from Midnight Spreadsheet")
			

	#logs ammonia readings from midnight sheet to SWOR
	def log_ammonia(self):
		p = Prompts()

		west_ammonia_cols = self._midnight['G']
		west_ammonia = west_ammonia_cols[5:35]

		west_swor_ammonia_cols = self._west_front['M']
		west_swor_ammonia = west_swor_ammonia_cols[8:self._row_len]

		east_ammonia_cols = self._midnight['N']
		east_ammonia = east_ammonia_cols[5:35]

		east_swor_ammonia_cols = self._east_front['M']
		east_swor_ammonia = east_swor_ammonia_cols[8:self._row_len]
		
		try:
			for i, day in enumerate(west_swor_ammonia):
				day.value = west_ammonia[i].value 
			print(f'{p.note()}West ammonia from Midnight Readings logged successfully')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Ammonia Meter numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()
			prompt_error("Error reading West Ammonia value from Midnight Spreadsheet")
			

		try:
			for i, day in enumerate(east_swor_ammonia):
				day.value = east_ammonia[i].value 
			print(f'{p.note()}East ammonia from Midnight Readings logged successfully')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Ammonia Meter numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()
			prompt_error("Error reading East Ammonia value from Midnight Spreadsheet")
			




	#Data from the Health Department website is passed to this function as an array of dictionaries, and writes the data to the BMR
	def log_bmr(self, bmr_wb, data_objs):
		p = Prompts()

		dates =             ( 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A21')

		sample_sites =      ( 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21')

		sample_type =       ( 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21')

		chlorine_res =      ( 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21')

		lab_results =       ( 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21')

		lab_num =           ( 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21')

		date_results_recv = ( 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21')

		try:
			bmr_wb['H5'].value = 'Carroll'
			for i, data in enumerate(data_objs):
				bmr_wb[dates[i]].value = data['date_collected']
				bmr_wb[sample_sites[i]].value = data['location_id']
				bmr_wb[sample_type[i]].value = data['sample_type']
				bmr_wb[chlorine_res[i]].value = data['chlorine']
				bmr_wb[lab_results[i]].value = data['result']
				bmr_wb[lab_num[i]].value = data['lab_no']
				bmr_wb[date_results_recv[i]] = data['date_recv']
			print(f'{p.note()}Data logged to BMR')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error completing BMR\n')
			prompt_error("Error logging BMR data")
			traceback.print_exc()



	def log_ifmrs(self, west_ifmr, east_ifmr, month):
		p = Prompts()
		if month != d.get_prev_month_str(): prompt_error("The month being logged in the IFMR is not the previous month")
		try:
			year = d.get_year()
		except:
			print(f'{p.err()}Could not get year in log_ifms functions')
		try:
			west_ifmr['O4'].value = month
			east_ifmr['O4'].value = month

			west_ifmr['H7'].value = 4
			east_ifmr['H7'].value = 4

			west_ifmr['S7'].value = 4
			east_ifmr['S7'].value = 4

			west_ifmr['L9'].value = "1, 2, 3, 4"
			east_ifmr['L9'].value = "1, 2, 3, 4"

			west_ifmr['N12'].value = 'X'
			east_ifmr['N12'].value = 'X'

			west_ifmr['K17'].value = 4
			east_ifmr['K17'].value = 4

			west_ifmr['O60'].value = 'General Manager'
			east_ifmr['O60'].value = 'General Manager'

			west_ifmr['O65'].value = month
			east_ifmr['O65'].value = month

			west_ifmr['S65'].value = year
			east_ifmr['S65'].value = year


			west_ifmr['F65'].value = 'Carroll Boone Water District'
			east_ifmr['F65'].value = 'Carroll Boone Water District'

			west_ifmr['D66'].value = '675'
			east_ifmr['D66'].value = '675'

			west_ifmr['M66'].value = 'Freeman-Raney Water Treatment Facility'
			east_ifmr['M66'].value = 'East Plant'

			west_ifmr['O111'].value = 'General Manager'
			east_ifmr['O111'].value = 'General Manager'

			print(f'{p.note()}Info for IFMRs complete')
		except:
			print(f'{p.err()}Could not complete IFMR')
			prompt_error("Could not complete IFMR")

	#logs peak flow levels from midnight sheet to SWOR
	def log_peaks(self):
		p = Prompts()

		#Raw Peak data from the Midnight Spreadsheet
		west_raw_cols = self._midnight['C']
		west_raw_peaks = west_raw_cols[5:35]

		east_raw_cols = self._midnight['J']
		east_raw_peaks = east_raw_cols[5:35]

		#High Service Peak data from the Midnight Spreadsheet
		west_fin_cols = self._midnight['D']
		west_fin_peaks = west_fin_cols[5:35]

		east_fin_cols = self._midnight['K']
		east_fin_peaks = east_fin_cols[5:35]

		#Hardcoded cells because spreadsheet cells on the SWOR are not sequential
		swor_raw_peaks = [
			'T13', 'T14', 'T15', 'T16', 'T17',
			'T18', 'T19', 'T20', 'T21', 'T22', 
			'T23', 'T24', 'T25', 'T26', 'T27', 
			'T28', 'T29', 'T30', 'T31', 'T32',
			'T33', 'T34', 'T35', 'T36', 'T38',
			'T40', 'T42', 'T44', 'T46', 'T48',
			'T50'
		] 

		swor_fin_peaks = [
			'U13', 'U14', 'U15', 'U16', 'U17',
			'U18', 'U19', 'U20', 'U21', 'U22', 
			'U23', 'U24', 'U25', 'U26', 'U27', 
			'U28', 'U29', 'U30', 'U31', 'U32',
			'U33', 'U34', 'U35', 'U36', 'U38',
			'U40', 'U42', 'U44', 'U46', 'U48',
			'U50'
		] 

		#log raw peak numbers to West SWOR
		try:
			for i, day in enumerate(west_raw_peaks):
				self._west_back[swor_raw_peaks[i]].value = day.value 
			print(f'{p.note()}West Raw Peaks logged successfully')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Raw Peak values from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()
			prompt_error("Error while logging West Raw Peak values from Midnight readings")

		#log raw peak values to East SWOR
		try:
			for i, day in enumerate(east_raw_peaks):
				self._east_back[swor_raw_peaks[i]].value = day.value 
			print(f'{p.note()}East Raw Peaks logged successfully')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Raw Peak values from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()
			prompt_error("Error while logging East Raw Peak values from Midnight readings")
			

		#log finish peak values to West SWOR
		try:
			for i, day in enumerate(west_fin_peaks):
				self._west_back[swor_fin_peaks[i]].value = day.value
			print(f'{p.note()}West High Service Peaks logged successfully')

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Finish Peak values from Midnight spread sheet transfer unsuccessful\n')
			prompt_error("Error while logging West Finish Peak values from Midnight readings")
			

		#log finish peak values to East SWOR
		try:
			for i, day in enumerate(east_fin_peaks):
				self._east_back[swor_fin_peaks[i]].value = day.value
			print(f'{p.note()}East High Service Peaks logged successfully')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Finish Peak values from Midnight spread sheet transfer unsuccessful\n')
			prompt_error("Error while logging East Finish Peak values from Midnight readings")
			

	#Logs lowest clearwell levels from Midnight sheet to SWOR
	def log_clearwells(self):
		p = Prompts()

		#Raw Peak data from the Midnight Spreadsheet
		west_cw_cols = self._midnight['E']
		west_clearwell = west_cw_cols[5:35]

		east_cw_cols = self._midnight['L']
		east_clearwell = east_cw_cols[5:35]


		#Hardcoded cells because spreadsheet cells on the SWOR are not sequential
		swor_cw = [
			'V13', 'V14', 'V15', 'V16', 'V17',
			'V18', 'V19', 'V20', 'V21', 'V22', 
			'V23', 'V24', 'V25', 'V26', 'V27', 
			'V28', 'V29', 'V30', 'V31', 'V32',
			'V33', 'V34', 'V35', 'V36', 'V38',
			'V40', 'V42', 'V44', 'V46', 'V48',
			'V50'
		] 



		#log lowest clearwell reading for west plant
		try:
			for i, day in enumerate(west_clearwell):
				self._west_back[swor_cw[i]].value = day.value 
			print(f'{p.note()}Lowest Clearwell reading for West Plant logged successfully')

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Clearwell values from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()
			prompt_error("Error while logging West Clearwell values from Midnight readings")
			

		#log lowest clearwell reading for east plat
		try:
			for i, day in enumerate(east_clearwell):
				self._east_back[swor_cw[i]].value = day.value 
			print(f'{p.note()}Lowest Clearwell reading for East Plant logged successfully')

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Clear values from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()
			prompt_error("Error while logging East Clearwell values from Midnight readings")
			

	#logs free chlorine from midnight sheet to SWOR
	def log_free_chlorine(self):
		p = Prompts()

		#Raw Peak data from the Midnight Spreadsheet
		west_cl_cols = self._midnight['F']
		west_cl = west_cl_cols[5:35]

		east_cl_cols = self._midnight['M']
		east_cl = east_cl_cols[5:35]


		#Hardcoded cells because spreadsheet cells on the SWOR are not sequential
		swor_cl = [
			'Y13', 'Y14', 'Y15', 'Y16', 'Y17',
			'Y18', 'Y19', 'Y20', 'Y21', 'Y22', 
			'Y23', 'Y24', 'Y25', 'Y26', 'Y27', 
			'Y28', 'Y29', 'Y30', 'Y31', 'Y32',
			'Y33', 'Y34', 'Y35', 'Y36', 'Y38',
			'Y40', 'Y42', 'Y44', 'Y46', 'Y48',
			'Y50'
		] 



		#log free chlorine for west
		try:
			for i, day in enumerate(west_cl):
				self._west_back[swor_cl[i]].value = day.value 
			print(f'{p.note()}Lowest Free Chlorine for West Plant logged successfully logged successfully')

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Free Chlorine numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()
			prompt_error("Error while logging West Chlorine Low values from Midnight readings")
			

		#log free chlorine for eat
		try:
			for i, day in enumerate(east_cl):
				self._east_back[swor_cl[i]].value = day.value 
			print(f'{p.note()}Lowest Free Chlorine for East Plant logged successfully')

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Free Chlorine numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()
			prompt_error("Error while logging East Chlorine Low values from Midnight readings")
			


	#Logs chlorine fed in pounds to West and East SWOR\
	def log_chlorine_used(self):
		p = Prompts()

		w_cl_cols = self._west_front['J']
		w_cl = w_cl_cols[8:self._row_len]

		e_cl_cols = self._east_front['J']
		e_cl = e_cl_cols[8:self._row_len]

		w_midnight_cols = self._midnight['R']
		w_midnight = w_midnight_cols[5:35]

		e_midnight_cols = self._midnight['S']
		e_midnight = e_midnight_cols[5:35]

		#midnight west chlorine usage -> west swor
		try:
			for i, day in enumerate(w_cl):
				day.value = w_midnight[i].value
			print(f'{p.note()}West chlorine usage logged')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Chlorine usage could not be logged\n')
			traceback.print_exc()
			prompt_error("Error while logging West Chlorine Used (lbs) values from Midnight readings")
			

		#midnight east chlorine usage -> west swor
		try:
			for i, day in enumerate(e_cl):
				day.value = e_midnight[i].value
			print(f'{p.note()}East chlorine usage logged')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Chlorine usage could not be logged\n')
			traceback.print_exc()
			prompt_error("Error while logging West Chlorine Used (lbs) values from Midnight readings")
			

	#logs hours run from midnight sheet -> SWORs
	def log_hours(self):
		p = Prompts()

		w_hours_cols = self._west_front['F']
		w_hours = w_hours_cols[8:self._row_len]

		e_hours_cols = self._east_front['F']
		e_hours = e_hours_cols[8:self._row_len]

		w_midnight_cols = self._midnight['P']
		w_midnight = w_midnight_cols[5:35]

		e_midnight_cols = self._midnight['Q']
		e_midnight = e_midnight_cols[5:35]

		#midnight west chlorine usage -> west swor
		try:
			for i, day in enumerate(w_hours):
				day.value = w_midnight[i].value
			print(f'{p.note()}Hours run for West Plant')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West hours could not be logged\n')
			traceback.print_exc()
			prompt_error("Error while logging West Plant Hours ran")
			

		#midnight west chlorine usage -> west swor
		try:
			for i, day in enumerate(e_hours):
				day.value = e_midnight[i].value
			print(f'{p.note()}Hours run for West Plant')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East hours could not be logged\n')
			traceback.print_exc()
			prompt_error("Error while logging East Plant Hours ran")
			

	def log_pac(self):
		p = Prompts()

		w_pac_cols = self._west_front['K']
		w_pac = w_pac_cols[8:self._row_len]

		e_pac_cols = self._east_front['K']
		e_pac = e_pac_cols[8:self._row_len]

		mid_west_cols = self._midnight['X']
		mid_west = mid_west_cols[5:36]

		mid_east_cols = self._midnight['Y']
		mid_east = mid_east_cols[5:36]

		try:
			for i, day in enumerate(w_pac):
				day.value = mid_west[i].value
			print(f'{p.note()}West pac successfully logged')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error in logging west PAC')
			traceback.print_exc()
			prompt_error("Error while logging West PAC used")
			

		try:
			for i, day in enumerate(e_pac):
				day.value = mid_east[i].value
			print(f'{p.note()}East pac successfully logged')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error in logging east PAC')
			traceback.print_exc()
			prompt_error("Error while logging East PAC used")
			

	def log_lime(self):
		p = Prompts()

		west_lime_columns = self._west_front['L']
		w_lime = west_lime_columns[8:self._row_len]

		east_lime_columns = self._east_front['L']
		e_lime = east_lime_columns[8:self._row_len]

		mid_west_cols = self._midnight['T']
		mid_west = mid_west_cols[5:36]

		mid_east_cols = self._midnight['U']
		mid_east = mid_east_cols[5:35]

		try:
			for i, day in enumerate(w_lime):
				day.value = mid_west[i].value
			print(f'{p.note()}West lime successfully logged')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error logging west lime')
			traceback.print_exc()
			prompt_error("Error while logging West Lime used")
			
		try:
			for i, day in enumerate(e_lime):
				day.value = mid_east[i].value
			print(f'{p.note()}East lime successfully logged')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error logging east lime')
			traceback.print_exc()
			prompt_error("Error while logging East Lime used")
			

	def log_fluoride(self):
		p = Prompts()

		west_fl_columns = self._west_front['N']
		w_fl = west_fl_columns[8:self._row_len]

		east_fl_columns = self._east_front['N']
		e_fl = east_fl_columns[8:self._row_len]

		mid_west_cols = self._midnight['H']
		mid_west = mid_west_cols[5:36]

		mid_east_cols = self._midnight['O']
		mid_east = mid_east_cols[5:35]

		try:
			for i, day in enumerate(w_fl):
				day.value = mid_west[i].value
			print(f'{p.note()}West fluoride successfully logged')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error logging west fluoride')
			traceback.print_exc()
			prompt_error("Error while logging West Fluoride used")
			
		try:
			for i, day in enumerate(e_fl):
				day.value = mid_east[i].value
			print(f'{p.note()}East fluoride successfully logged')
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error logging east fluoride')
			traceback.print_exc()
			prompt_error("Error while logging East Fluoride used")

	def log_all(self):
		self.log_meters()
		self.log_ammonia()
		self.log_peaks()
		self.log_clearwells()
		self.log_free_chlorine()
		self.log_chlorine_used()
		self.log_hours()
		self.log_pac()
		self.log_lime()
		self.log_fluoride()

	def get_exceptions(self):
		return self.EXCEPTIONS