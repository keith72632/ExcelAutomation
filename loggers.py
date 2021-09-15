from colors import Prompts
from filelib import Directories
import traceback

d = Directories()


class Logger:
	def __init__(self):
		pass

	EXCEPTIONS = 0

	#logs meter numbers to SWOR from mango spreadshett
	def log_meters(self, west_swor, east_swor, midnight):
		p = Prompts()

		west_raw_cols = midnight['B']
		west_raw = west_raw_cols[6:36]

		west_swor_meter_cols = west_swor['B']
		west_swor_raw = west_swor_meter_cols[9:39]

		east_raw_cols = midnight['I']
		east_raw = east_raw_cols[6:36]

		east_swor_meter_cols = east_swor['B']
		east_swor_raw = east_swor_meter_cols[9:36]
		
		try:
			for i, day in enumerate(west_swor_raw):
				day.value = west_raw[i].value 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Raw Meter numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()

		try:
			for i, day in enumerate(east_swor_raw):
				day.value = east_raw[i].value 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Raw Meter numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()

	#logs ammonia readings from midnight sheet to SWOR
	def log_ammonia(self, west_swor, east_swor, midnight):
		p = Prompts()

		west_ammonia_cols = midnight['G']
		west_ammonia = west_ammonia_cols[6:36]

		west_swor_ammonia_cols = west_swor['M']
		west_swor_ammonia = west_swor_ammonia_cols[9:39]

		east_ammonia_cols = midnight['N']
		east_ammonia = east_ammonia_cols[6:36]

		east_swor_ammonia_cols = east_swor['M']
		east_swor_ammonia = east_swor_ammonia_cols[9:36]
		
		try:
			for i, day in enumerate(west_swor_ammonia):
				day.value = west_ammonia[i].value 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Ammonia Meter numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()

		try:
			for i, day in enumerate(east_swor_ammonia):
				day.value = east_ammonia[i].value 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Ammonia Meter numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()

	#Transfers rainfall data from West Operations Report to East Operations Report
	def log_rainfall(self, w_active, e_active):
		p = Prompts()
		west_cells = (
			'G9', 'G10', 'G11', 'G12', 'G13',
			'G14', 'G15', 'G16', 'G17', 'G18',
			'G19', 'G20', 'G21', 'G22', 'G23',
			'G24', 'G25', 'G26', 'G27', 'G28',
			'G29', 'G30', 'G31', 'G32', 'G33',
			'G34', 'G35', 'G36', 'G37', 'G38',
			'G39',
		)

		east_cells = (
			'G9', 'G10', 'G11', 'G12', 'G13',
			'G14', 'G15', 'G16', 'G17', 'G18',
			'G19', 'G20', 'G21', 'G22', 'G23',
			'G24', 'G25', 'G26', 'G27', 'G28',
			'G29', 'G30', 'G31', 'G32', 'G33',
			'G34', 'G35', 'G36', 'G37', 'G38',
			'G39',
		)

		try:
			for i, day in enumerate(east_cells):
				e_active[day].value = w_active[west_cells[i]].value

			return west_cells

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring rainfall data\n')



	#Transfers Finish pH data from the West Operations report to the East Operations Report
	def log_finish_pH(self, w_active, e_active):
		p = Prompts()
		west_cells = (
			'S9', 'S10', 'S11', 'S12', 'S13',
			'S14', 'S15', 'S16', 'S17', 'S18',
			'S19', 'S20', 'S21', 'S22', 'S23', 
			'S24', 'S25', 'S26', 'S27', 'S28',
			'S29', 'S30', 'S31', 'S32', 'S33',
			'S34', 'S35', 'S36', 'S37', 'S38',
			'S39',
		)

		east_cells = (
			'R9', 'R10', 'R11', 'R12', 'R13',
			'R14', 'R15', 'R16', 'R17', 'R18',
			'R19', 'R20', 'R21', 'R22', 'R23',
			'R24', 'R25', 'R26', 'R27', 'R28',
			'R29', 'R30', 'R31', 'R32', 'R33',
			'R34', 'R35', 'R36', 'R37', 'R38',
			'R39',
		)

		try:
			for i, day in enumerate(east_cells):
				e_active[day].value = w_active[west_cells[i]].value

			return west_cells

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring finish pH data\n')



	#Transfer total chlorine data from the West Operations Report to the East Operations Report
	def log_total(self, w_active, e_active):
		p = Prompts()
		west_cells = (
			'AI9', 'AI10', 'AI11', 'AI12', 'AI13',
			'AI14', 'AI15', 'AI16', 'AI17', 'AI18',
			'AI19', 'AI20', 'AI21', 'AI22', 'AI23',
			'AI24', 'AI25', 'AI26', 'AI27', 'AI28',
			'AI29', 'AI30', 'AI31', 'AI32', 'AI33',
			'AI34', 'AI35', 'AI36', 'AI37', 'AI38',
			'AI39',
		)

		east_cells = (
			'AH9', 'AH10', 'AH11', 'AH12', 'AH13',
			'AH14', 'AH15', 'AH16', 'AH17', 'AH18',
			'AH19', 'AH20', 'AH21', 'AH22', 'AH23',
			'AH24', 'AH25', 'AH26', 'AH27', 'AH28',
			'AH29', 'AH30', 'AH31', 'AH32', 'AH33',
			'AH34', 'AH35', 'AH36', 'AH37', 'AH38',
			'AH39'
		)

		try:
			for i, day in enumerate(east_cells):
				e_active[day].value = w_active[west_cells[i]].value

			return west_cells
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring total chlorine data\n')



	#Copies Chloramine Data from the West Operations Report to the East Operation Report
	def log_chloramine(self, w_active, e_active):
		p = Prompts()
		west_cells = (
			'AJ9', 'AJ10', 'AJ11', 'AJ12', 'AJ13',
			'AJ14', 'AJ15', 'AJ16', 'AJ17', 'AJ18', 
			'AJ19', 'AJ20', 'AJ21', 'AJ22', 'AJ23',
			'AJ24', 'AJ25', 'AJ26', 'AJ27', 'AJ28',
			'AJ29', 'AJ30', 'AJ31', 'AJ32', 'AJ33',
			'AJ34', 'AJ35', 'AJ36', 'AJ37', 'AJ38',
			'AJ39',
		)

		east_cells = (
			'AI9', 'AI10', 'AI11', 'AI12', 'AI13',
			'AI14', 'AI15', 'AI16', 'AI17','AI18',
			'AI19', 'AI20', 'AI21', 'AI22', 'AI23',
			'AI24', 'AI25', 'AI26', 'AI27', 'AI28',
			'AI29', 'AI30', 'AI31', 'AI32', 'AI33',
			'AI34', 'AI35', 'AI36', 'AI37', 'AI38',
			'AI39',
		)

		try:
			for i, day in enumerate(east_cells):
				e_active[day].value = w_active[west_cells[i]].value

			return west_cells

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring chloramine data\n')





	#Data from the Health Department website is passed to this function as an array of dictionaries, and writes the data to the BMR
	def log_bmr(self, bmr_wb, data_objs):
		p = Prompts()

		dates =             ( 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', )

		sample_sites =      ( 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18' )

		sample_type =       ( 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18' )

		chlorine_res =      ( 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18' )

		lab_results =       ( 'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18' )

		lab_num =           ( 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18' )

		date_results_recv = ( 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18' )

		#TODO add try and except block
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
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error completing BMR\n')



	def log_ifmrs(self, west_ifmr, east_ifmr):
		p = Prompts()
		month = d.get_prev_month_str()
		year = d.get_year()
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

	#logs peak flow levels from midnight sheet to SWOR
	def log_peaks(self, west_swor, east_swor, midnight):
		p = Prompts()

		#Raw Peak data from the Midnight Spreadsheet
		west_raw_cols = midnight['C']
		west_raw_peaks = west_raw_cols[6:36]

		east_raw_cols = midnight['J']
		east_raw_peaks = east_raw_cols[6:36]

		#High Service Peak data from the Midnight Spreadsheet
		west_fin_cols = midnight['D']
		west_fin_peaks = west_fin_cols[6:36]

		east_fin_cols = midnight['K']
		east_fin_peaks = east_fin_cols[6:36]

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
				west_swor[swor_raw_peaks[i]].value = day.value 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Raw Peak numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()

		#log raw peak numbers to East SWOR
		try:
			for i, day in enumerate(east_raw_peaks):
				east_swor[swor_raw_peaks[i]].value = day.value 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Raw Peak numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()

		#log finish peak numbers to West SWOR
		try:
			for i, day in enumerate(west_fin_peaks):
				west_swor[swor_fin_peaks[i]].value = day.value
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Finish Peak numbers from Midnight spread sheet transfer unsuccessful\n')

		#log finish peak numbers to East SWOR
		try:
			for i, day in enumerate(east_fin_peaks):
				east_swor[swor_fin_peaks[i]].value = day.value
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Finish Peak numbers from Midnight spread sheet transfer unsuccessful\n')

	#Logs lowest clearwell levels from Midnight sheet to SWOR
	def log_clearwells(self, west_swor, east_swor, midnight):
		p = Prompts()

		#Raw Peak data from the Midnight Spreadsheet
		west_cw_cols = midnight['E']
		west_clearwell = west_cw_cols[6:36]

		east_cw_cols = midnight['L']
		east_clearwell = east_cw_cols[6:36]


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



		#log raw peak numbers to West SWOR
		try:
			for i, day in enumerate(west_clearwell):
				west_swor[swor_cw[i]].value = day.value 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Clearwell numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()

		#log raw peak numbers to East SWOR
		try:
			for i, day in enumerate(east_clearwell):
				east_swor[swor_cw[i]].value = day.value 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Clear numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()

	#logs free chlorine from midnight sheet to SWOR
	def log_free_chlorine(self, west_swor, east_swor, midnight):
		p = Prompts()

		#Raw Peak data from the Midnight Spreadsheet
		west_cl_cols = midnight['F']
		west_cl = west_cl_cols[6:36]

		east_cl_cols = midnight['M']
		east_cl = east_cl_cols[6:36]


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



		#log raw peak numbers to West SWOR
		try:
			for i, day in enumerate(west_cl):
				west_swor[swor_cl[i]].value = day.value 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}West Free Chlorine numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()

		#log raw peak numbers to East SWOR
		try:
			for i, day in enumerate(east_cl):
				east_swor[swor_cl[i]].value = day.value 
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}East Free Chlorine numbers from Midnight spread sheet transfer unsuccessful\n')
			traceback.print_exc()


	def get_exceptions(self):
		return self.EXCEPTIONS