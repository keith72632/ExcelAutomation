from colors import Prompts
from filelib import Directories

d = Directories()

class Transfer:
	def __init__(self):
		pass
	EXCEPTIONS = 0
	#Tranfers the meter reading from the West Operations Report to the East Chemical Treatment Record
	def transfer_meters_west(self, w_active, w_chem):
		p = Prompts()
		#cells from the West operations report
		op_meter_cells = (
			'B9', 'B10', 'B11', 'B12', 'B13',
			'B14', 'B15', 'B16', 'B17','B18',
			'B19', 'B20', 'B21', 'B22', 'B23',
			'B24', 'B25', 'B26', 'B27', 'B28',
			'B29', 'B30', 'B31', 'B32', 'B33',
			'B34', 'B35', 'B36', 'B37', 'B38',
			'B39',
		)

		ct_meter_cells = (
			'A10', 'A11', 'A12', 'A13','A14', 
			'A15', 'A16', 'A17','A18', 'A19', 
			'A20', 'A21', 'A22', 'A23', 'A24', 
			'A25', 'A26', 'A27', 'A28', 'A29', 
			'A30', 'A31', 'A32', 'A33', 'A34', 
			'A35', 'A36', 'A37', 'A38', 'A39',
			'A40'
		)

		try:
			for i, day in enumerate(op_meter_cells):
				w_chem[ct_meter_cells[i]].value = w_active[day].value 
			return ct_meter_cells
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West meter data from Operations Report to Chemical Treatment\n')


	#Transfers the meter readings from the East Operations Report to the East Chemical Treatment Record
	def transfer_meters_east(self, e_active, e_chem):
		p = Prompts()
		#cells from the East operations report
		op_meter_cells = (
			'B9', 'B10', 'B11', 'B12', 'B13',
			'B14', 'B15', 'B16', 'B17','B18',
			'B19', 'B20', 'B21', 'B22', 'B23',
			'B24', 'B25', 'B26', 'B27', 'B28',
			'B29', 'B30', 'B31', 'B32', 'B33',
			'B34', 'B35', 'B36', 'B37', 'B38',
			'B39',
		)

		ct_meter_cells = (
			'A10', 'A11', 'A12', 'A13','A14', 
			'A15', 'A16', 'A17','A18', 'A19', 
			'A20', 'A21', 'A22', 'A23', 'A24', 
			'A25', 'A26', 'A27', 'A28', 'A29', 
			'A30', 'A31', 'A32', 'A33', 'A34', 
			'A35', 'A36', 'A37', 'A38', 'A39',
			'A40'
		)

		try:
			for i, day in enumerate(op_meter_cells):
				e_chem[ct_meter_cells[i]].value = e_active[day].value 
			return ct_meter_cells
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering East meter data\n')
			traceback.print_exc()


	#The values in total raw water flow on the Operations Report are calculated via formula, which openpyxl cannot transfer
	#this function calculates the first flow value in the Chemical treatment record and fills the rest with a formula within excel
	def transfer_flow_west(self, w_active, w_chem):
		p = Prompts()

		try:
			if w_active['B9'].value:
				root_reading = (w_active['B9'].value - w_active['B5'].value) / 1000
				w_chem['C10'].value = root_reading
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West flow data\n')



	#The values in total raw water flow on the Operations Report are calculated via formula, which openpyxl cannot transfer
	#this function calculates the first flow value in the Chemical treatment record and fills the rest with a formula within excel
	def transfer_flow_east(self, e_active, e_chem):
		p = Prompts()

		try:
			root_reading = (e_active['B9'].value - e_active['B5'].value) / 1000
			e_chem['C10'].value = root_reading
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering East meter data\n')


	#Transfers fluoride residual data from West Operations Report to the East Operations Report
	def transfer_fluoride(self, w_active, e_active):
		p = Prompts()
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
			
			return west_cells

		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transferring fluroide data\n')


	#Transfers the chlorine readings (in PPD) from the West Operations Report to the West Chemical Treatment Record
	def transfer_chlorine_west(self, w_active, w_chem):
		p = Prompts()
		op_chlorine_cells = (
			'J9', 'J10', 'J11', 'J12', 'J13',
			'J14', 'J15', 'J16', 'J17','J18',
			'J19', 'J20', 'J21', 'J22', 'J23',
			'J24', 'J25', 'J26', 'J27', 'J28',
			'J29', 'J30', 'J31', 'J32', 'J33',
			'J34', 'J35', 'J36', 'J37', 'J38',
			'J39',
		)
		
		ct_chlorine_cells = (
			'D10', 'D11', 'D12', 'D13','D14', 
			'D15', 'D16', 'D17','D18', 'D19', 
			'D20', 'D21', 'D22', 'D23', 'D24', 
			'D25', 'D26', 'D27', 'D28', 'D29', 
			'D30', 'D31', 'D32', 'D33', 'D34', 
			'D35', 'D36', 'D37', 'D38', 'D39',
			'D40'
		)

		try:
			for i, day in enumerate(op_chlorine_cells):
				w_chem[ct_chlorine_cells[i]].value = w_active[day].value
			return ct_chlorine_cells		
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West Chlorine data\n')


	#Transers the chlorine readings (in PPD) from the East Operations Report to the West Chemical Treatment Record
	def transfer_chlorine_East(self, e_active, e_chem):
		p = Prompts()
		op_chlorine_cells = (
			'J9', 'J10', 'J11', 'J12', 'J13',
			'J14', 'J15', 'J16', 'J17','J18',
			'J19', 'J20', 'J21', 'J22', 'J23',
			'J24', 'J25', 'J26', 'J27', 'J28',
			'J29', 'J30', 'J31', 'J32', 'J33',
			'J34', 'J35', 'J36', 'J37', 'J38',
			'J39',
		)
		
		ct_chlorine_cells = (
			'D10', 'D11', 'D12', 'D13','D14', 
			'D15', 'D16', 'D17','D18', 'D19', 
			'D20', 'D21', 'D22', 'D23', 'D24', 
			'D25', 'D26', 'D27', 'D28', 'D29', 
			'D30', 'D31', 'D32', 'D33', 'D34', 
			'D35', 'D36', 'D37', 'D38', 'D39',
			'D40'
		)

		try:
			for i, day in enumerate(op_chlorine_cells):
				e_chem[ct_chlorine_cells[i]].value = e_active[day].value
			return ct_chlorine_cells		
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering East Chlorine data\n')


	def transfer_chlorine_res_east(self, east_chem, east_table):
		p = Prompts()
		free_cells = (
			'F10', 'F11', 'F12', 'F13','F14', 
			'F15', 'F16', 'F17','F18', 'F19', 
			'F20', 'F21', 'F22', 'F23', 'F24', 
			'F25', 'F26', 'F27', 'F28', 'F29', 
			'F30', 'F31', 'F32', 'F33', 'F34', 
			'F35', 'F36', 'F37', 'F38', 'F39',
			'F40'
		)

		total_cells = (
			'G10', 'G11', 'G12', 'G13','G14', 
			'G15', 'G16', 'G17','G18', 'G19', 
			'G20', 'G21', 'G22', 'G23', 'G24', 
			'G25', 'G26', 'G27', 'G28', 'G29', 
			'G30', 'G31', 'G32', 'G33', 'G34', 
			'G35', 'G36', 'G37', 'G38', 'G39',
			'G40'
		)

		free_table = (
			'A2', 'A3', 'A4', 'A5', 'A6',
			'A7', 'A8', 'A9', 'A10', 'A11', 
			'A12', 'A13', 'A14', 'A15', 'A16', 
			'A17', 'A18', 'A19', 'A20', 'A21', 
			'A22', 'A23', 'A24', 'A25', 'A26', 
			'A27', 'A28', 'A29', 'A30', 'A31', 
			'A32'
		)

		total_table = (
			'A36', 'A37', 'A38', 'A39', 'A40',
			'A41', 'A42', 'A43', 'A44', 'A45',
			'A46', 'A47', 'A48', 'A49', 'A50',
			'A51', 'A52', 'A53', 'A54', 'A55',
			'A56', 'A57', 'A58', 'A59', 'A60',
			'A61', 'A62', 'A63', 'A64', 'A65',
			'A66'
		)

		try:
			for i, day in enumerate(free_cells):
				east_chem[day].value = east_table[free_table[i]].value
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering east residuals\n')

		try:
			for i, day in enumerate(total_cells):
				east_chem[day].value = east_table[total_table[i]].value
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering east residuals\n')


	def transfer_chlorine_res_west(self, west_chem, west_table):
		p = Prompts()
		free_cells = (
			'F10', 'F11', 'F12', 'F13','F14', 
			'F15', 'F16', 'F17','F18', 'F19', 
			'F20', 'F21', 'F22', 'F23', 'F24', 
			'F25', 'F26', 'F27', 'F28', 'F29', 
			'F30', 'F31', 'F32', 'F33', 'F34', 
			'F35', 'F36', 'F37', 'F38', 'F39',
			'F40'
		)

		total_cells = (
			'G10', 'G11', 'G12', 'G13','G14', 
			'G15', 'G16', 'G17','G18', 'G19', 
			'G20', 'G21', 'G22', 'G23', 'G24', 
			'G25', 'G26', 'G27', 'G28', 'G29', 
			'G30', 'G31', 'G32', 'G33', 'G34', 
			'G35', 'G36', 'G37', 'G38', 'G39',
			'G40'
		)

		free_table = (
			'A2', 'A3', 'A4', 'A5', 'A6',
			'A7', 'A8', 'A9', 'A10', 'A11', 
			'A12', 'A13', 'A14', 'A15', 'A16', 
			'A17', 'A18', 'A19', 'A20', 'A21', 
			'A22', 'A23', 'A24', 'A25', 'A26', 
			'A27', 'A28', 'A29', 'A30', 'A31', 
			'A32'
		)

		total_table = (
			'A36', 'A37', 'A38', 'A39', 'A40',
			'A41', 'A42', 'A43', 'A44', 'A45',
			'A46', 'A47', 'A48', 'A49', 'A50',
			'A51', 'A52', 'A53', 'A54', 'A55',
			'A56', 'A57', 'A58', 'A59', 'A60',
			'A61', 'A62', 'A63', 'A64', 'A65',
			'A66'
		)

		try:
			for i, day in enumerate(free_cells):
				west_chem[day].value = west_table[free_table[i]].value
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West residuals\n')

		try:
			for i, day in enumerate(total_cells):
				west_chem[day].value = west_table[total_table[i]].value
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering West residuals\n')


	def transfer_distribution(self, west_chem, east_chem):
		p = Prompts()
		cells = (
			'I10', 'I12', 'I14', 'I16', 'I18',
			'I20', 'I22', 'I24', 'I26', 'I28'
		)

		try:
			for day in cells:
				east_chem[day].value = west_chem[day].value
		except:
			self.EXCEPTIONS += 1
			print(f'{p.err()}Error transfering Distribution Meter Readings\n')

	def get_exceptions(self):
		return self.EXCEPTIONS