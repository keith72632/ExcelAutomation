from colors import Prompts
from filelib import get_month_str, get_prev_month_str, get_year


p = Prompts()
#Transfers rainfall data from West Operations Report to East Operations Report
def log_rainfall(w_active, e_active):
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

		print(f'{p.ok()}Rainfall data successfully transfered\n')
		return west_cells

	except:
		print(f'{p.err()}Error transferring rainfall data\n')




#Transfers fluoride residual data from West Operations Report to the East Operations Report
def log_fluoride(w_active, e_active):
	west_cells = (
		'O9', 'O10', 'O11', 'O12', 'O13',
		'O14', 'O15', 'O16', 'O17', 'O18',
		'O19', 'O20', 'O21', 'O22', 'O23',
		'O24', 'O25', 'O26', 'O27', 'O28',
		'O29', 'O30', 'O31', 'O32', 'O33',
		'O34', 'O35', 'O36', 'O37', 'O38',
		'O39',
	)

	east_cells = (
		'O9', 'O10', 'O11', 'O12', 'O13',
		'O14', 'O15', 'O16', 'O17', 'O18',
		'O19', 'O20', 'O21', 'O22', 'O23',
		'O24', 'O25', 'O26', 'O27', 'O28',
		'O29', 'O30', 'O31', 'O32', 'O33',
		'O34', 'O35', 'O36', 'O37', 'O38',
		'O39',
	)

	try:
		for i, day in enumerate(east_cells):
			e_active[day].value = w_active[west_cells[i]].value
		
		print(f'{p.ok()}Fluoride data successfully transfered\n')	
		return west_cells

	except:
		print(f'{p.err()}Error transferring fluroide data\n')


#Transfers Finish pH data from the West Operations report to the East Operations Report
def log_finish_pH(w_active, e_active):
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

		print(f'{p.ok()}Finish pH data successfully transfered\n')
		return west_cells

	except:
		print(f'{p.err()}Error transferring finish pH data\n')



#Transfer total chlorine data from the West Operations Report to the East Operations Report
def log_total(w_active, e_active):
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

		print(f'{p.ok()}Total chlorine data successfully transfered\n')
		return west_cells
	except:
		print(f'{p.err()}Error transferring total chlorine data\n')



#Copies Chloramine Data from the West Operations Report to the East Operation Report
def log_chloramine(w_active, e_active):
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

		print(f'{p.ok()}Chloramine data successfully transfered\n')
		return west_cells

	except:
		print(f'{p.err()}Error transferring chloramine data\n')





#Data from the Health Department website is passed to this function as an array of dictionaries, and writes the data to the BMR
def log_bmr(bmr_wb, data_objs):
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
		print(f'{p.ok()}BMR saved\n')
	except:
		print(f'{p.err()}Error completing BMR\n')



def log_ifmrs(west_ifmr, east_ifmr):
	month = get_prev_month_str()
	year = get_year()
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






