from colors import ok_block, error_block, warning_block

def log_rainfall(w_active, e_active):
	west_rainfall = [
		w_active['G9'].value,
		w_active['G10'].value,
		w_active['G11'].value,
		w_active['G12'].value,
		w_active['G13'].value,
		w_active['G14'].value,
		w_active['G15'].value,
		w_active['G16'].value,
		w_active['G17'].value,
		w_active['G18'].value,
		w_active['G19'].value,
		w_active['G20'].value,
		w_active['G21'].value,
		w_active['G22'].value,
		w_active['G23'].value,
		w_active['G24'].value,
		w_active['G25'].value,
		w_active['G26'].value,
		w_active['G27'].value,
		w_active['G28'].value,
		w_active['G29'].value,
		w_active['G30'].value,
		w_active['G31'].value,
		w_active['G32'].value,
		w_active['G33'].value,
		w_active['G34'].value,
		w_active['G35'].value,
		w_active['G36'].value,
		w_active['G37'].value,
		w_active['G38'].value,
		w_active['G39'].value,
	]

	east_rainfall = [
		e_active['G9'],
		e_active['G10'],
		e_active['G11'],
		e_active['G12'],
		e_active['G13'],
		e_active['G14'],
		e_active['G15'],
		e_active['G16'],
		e_active['G17'],
		e_active['G18'],
		e_active['G19'],
		e_active['G20'],
		e_active['G21'],
		e_active['G22'],
		e_active['G23'],
		e_active['G24'],
		e_active['G25'],
		e_active['G26'],
		e_active['G27'],
		e_active['G28'],
		e_active['G29'],
		e_active['G30'],
		e_active['G31'],
		e_active['G32'],
		e_active['G33'],
		e_active['G34'],
		e_active['G35'],
		e_active['G36'],
		e_active['G37'],
		e_active['G38'],
		e_active['G39'],
	]

	for i, day in enumerate(east_rainfall):
		day.value = west_rainfall[i]

	return west_rainfall


def log_fluoride(w_active, e_active):
	west_fluoride = [
		w_active['O9'].value,
		w_active['O10'].value,
		w_active['O11'].value,
		w_active['O12'].value,
		w_active['O13'].value,
		w_active['O14'].value,
		w_active['O15'].value,
		w_active['O16'].value,
		w_active['O17'].value,
		w_active['O18'].value,
		w_active['O19'].value,
		w_active['O20'].value,
		w_active['O21'].value,
		w_active['O22'].value,
		w_active['O23'].value,
		w_active['O24'].value,
		w_active['O25'].value,
		w_active['O26'].value,
		w_active['O27'].value,
		w_active['O28'].value,
		w_active['O29'].value,
		w_active['O30'].value,
		w_active['O31'].value,
		w_active['O32'].value,
		w_active['O33'].value,
		w_active['O34'].value,
		w_active['O35'].value,
		w_active['O36'].value,
		w_active['O37'].value,
		w_active['O38'].value,
		w_active['O39'].value,
	]

	east_fluoride = [
		e_active['O9'],
		e_active['O10'],
		e_active['O11'],
		e_active['O12'],
		e_active['O13'],
		e_active['O14'],
		e_active['O15'],
		e_active['O16'],
		e_active['O17'],
		e_active['O18'],
		e_active['O19'],
		e_active['O20'],
		e_active['O21'],
		e_active['O22'],
		e_active['O23'],
		e_active['O24'],
		e_active['O25'],
		e_active['O26'],
		e_active['O27'],
		e_active['O28'],
		e_active['O29'],
		e_active['O30'],
		e_active['O31'],
		e_active['O32'],
		e_active['O33'],
		e_active['O34'],
		e_active['O35'],
		e_active['O36'],
		e_active['O37'],
		e_active['O38'],
		e_active['O39'],
	]

	for i, day in enumerate(east_fluoride):
		day.value = west_fluoride[i]
		
	return west_fluoride


def log_finish_pH(w_active, e_active):
	west_finishPH = [
		w_active['S9'].value,
		w_active['S10'].value,
		w_active['S11'].value,
		w_active['S12'].value,
		w_active['S13'].value,
		w_active['S14'].value,
		w_active['S15'].value,
		w_active['S16'].value,
		w_active['S17'].value,
		w_active['S18'].value,
		w_active['S19'].value,
		w_active['S20'].value,
		w_active['S21'].value,
		w_active['S22'].value,
		w_active['S23'].value,
		w_active['S24'].value,
		w_active['S25'].value,
		w_active['S26'].value,
		w_active['S27'].value,
		w_active['S28'].value,
		w_active['S29'].value,
		w_active['S30'].value,
		w_active['S31'].value,
		w_active['S32'].value,
		w_active['S33'].value,
		w_active['S34'].value,
		w_active['S35'].value,
		w_active['S36'].value,
		w_active['S37'].value,
		w_active['S38'].value,
		w_active['S39'].value,
	]

	east_finish_PH = [
		e_active['R9'],
		e_active['R10'],
		e_active['R11'],
		e_active['R12'],
		e_active['R13'],
		e_active['R14'],
		e_active['R15'],
		e_active['R16'],
		e_active['R17'],
		e_active['R18'],
		e_active['R19'],
		e_active['R20'],
		e_active['R21'],
		e_active['R22'],
		e_active['R23'],
		e_active['R24'],
		e_active['R25'],
		e_active['R26'],
		e_active['R27'],
		e_active['R28'],
		e_active['R29'],
		e_active['R30'],
		e_active['R31'],
		e_active['R32'],
		e_active['R33'],
		e_active['R34'],
		e_active['R35'],
		e_active['R36'],
		e_active['R37'],
		e_active['R38'],
		e_active['R39'],
	]

	for i, day in enumerate(east_finish_PH):
		day.value = west_finishPH[i]

	return west_finishPH

def log_total(w_active, e_active):
	west_total = [
		w_active['AI9'].value,
		w_active['AI10'].value,
		w_active['AI11'].value,
		w_active['AI12'].value,
		w_active['AI13'].value,
		w_active['AI14'].value,
		w_active['AI15'].value,
		w_active['AI16'].value,
		w_active['AI17'].value,
		w_active['AI18'].value,
		w_active['AI19'].value,
		w_active['AI20'].value,
		w_active['AI21'].value,
		w_active['AI22'].value,
		w_active['AI23'].value,
		w_active['AI24'].value,
		w_active['AI25'].value,
		w_active['AI26'].value,
		w_active['AI27'].value,
		w_active['AI28'].value,
		w_active['AI29'].value,
		w_active['AI30'].value,
		w_active['AI31'].value,
		w_active['AI32'].value,
		w_active['AI33'].value,
		w_active['AI34'].value,
		w_active['AI35'].value,
		w_active['AI36'].value,
		w_active['AI37'].value,
		w_active['AI38'].value,
		w_active['AI39'].value,
	]

	east_total = [
		e_active['AH9'],
		e_active['AH10'],
		e_active['AH11'],
		e_active['AH12'],
		e_active['AH13'],
		e_active['AH14'],
		e_active['AH15'],
		e_active['AH16'],
		e_active['AH17'],
		e_active['AH18'],
		e_active['AH19'],
		e_active['AH20'],
		e_active['AH21'],
		e_active['AH22'],
		e_active['AH23'],
		e_active['AH24'],
		e_active['AH25'],
		e_active['AH26'],
		e_active['AH27'],
		e_active['AH28'],
		e_active['AH29'],
		e_active['AH30'],
		e_active['AH31'],
		e_active['AH32'],
		e_active['AH33'],
		e_active['AH34'],
		e_active['AH35'],
		e_active['AH36'],
		e_active['AH37'],
		e_active['AH38'],
		e_active['AH39']
	]

	for i, day in enumerate(east_total):
		day.value = west_total[i]

	return west_total

def log_chloramine(w_active, e_active):
	west_chloramine_cl2 = [
		w_active['AJ9'].value,
		w_active['AJ10'].value,
		w_active['AJ11'].value,
		w_active['AJ12'].value,
		w_active['AJ13'].value,
		w_active['AJ14'].value,
		w_active['AJ15'].value,
		w_active['AJ16'].value,
		w_active['AJ17'].value,
		w_active['AJ18'].value,
		w_active['AJ19'].value,
		w_active['AJ20'].value,
		w_active['AJ21'].value,
		w_active['AJ22'].value,
		w_active['AJ23'].value,
		w_active['AJ24'].value,
		w_active['AJ25'].value,
		w_active['AJ26'].value,
		w_active['AJ27'].value,
		w_active['AJ28'].value,
		w_active['AJ29'].value,
		w_active['AJ30'].value,
		w_active['AJ31'].value,
		w_active['AJ32'].value,
		w_active['AJ33'].value,
		w_active['AJ34'].value,
		w_active['AJ35'].value,
		w_active['AJ36'].value,
		w_active['AJ37'].value,
		w_active['AJ38'].value,
		w_active['AJ39'].value,
	]

	east_chloramine_cl2 = [
		e_active['AI9'] ,
		e_active['AI10'],
		e_active['AI11'],
		e_active['AI12'],
		e_active['AI13'],
		e_active['AI14'],
		e_active['AI15'],
		e_active['AI16'],
		e_active['AI17'],
		e_active['AI18'],
		e_active['AI19'],
		e_active['AI20'],
		e_active['AI21'],
		e_active['AI22'],
		e_active['AI23'],
		e_active['AI24'],
		e_active['AI25'],
		e_active['AI26'],
		e_active['AI27'],
		e_active['AI28'],
		e_active['AI29'],
		e_active['AI30'],
		e_active['AI31'],
		e_active['AI32'],
		e_active['AI33'],
		e_active['AI34'],
		e_active['AI35'],
		e_active['AI36'],
		e_active['AI37'],
		e_active['AI38'],
		e_active['AI39'],
	]

	for i, day in enumerate(east_chloramine_cl2):
		day.value = west_chloramine_cl2[i]

	return west_chloramine_cl2

def log_bmr(bmr_wb, data_objs):
	dates = [
		'A11',
		'A12',
		'A13',
		'A14',
		'A15',
		'A16',
		'A17',
		'A18',
	]

	sample_sites = [
		'B11',
		'B12',
		'B13',
		'B14',
		'B15',
		'B16',
		'B17',
		'B18'
	]

	sample_type = [
		'C11',
		'C12',
		'C13',
		'C14',
		'C15',
		'C16',
		'C17',
		'C18'
	]

	chlorine_res = [
		'D11',
		'D12',
		'D13',
		'D14',
		'D15',
		'D16',
		'D17',
		'D18'
	]

	lab_results = [
		'E11',
		'E12',
		'E13',
		'E14',
		'E15',
		'E16',
		'E17',
		'E18'
	]

	lab_num = [
		'F11',
		'F12',
		'F13',
		'F14',
		'F15',
		'F16',
		'F17',
		'F18'
	]

	date_results_recv = [
		'H11',
		'H12',
		'H13',
		'H14',
		'H15',
		'H16',
		'H17',
		'H18'
	]

	#TODO add try and except block
	bmr_wb['H5'].value = 'Carroll'
	for i, data in enumerate(data_objs):
		# print(bmr_wb[dates[i]].value)
		# print(data['date_collected'])
		bmr_wb[dates[i]].value = data['date_collected']
		bmr_wb[sample_sites[i]].value = data['location_id']
		bmr_wb[sample_type[i]].value = data['sample_type']
		bmr_wb[chlorine_res[i]].value = data['chlorine']
		bmr_wb[lab_results[i]].value = data['result']
		bmr_wb[lab_num[i]].value = data['lab_no']
		bmr_wb[date_results_recv[i]] = data['date_recv']
	print(f'{ok_block()}BMR saved\n')