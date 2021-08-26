class bcolors:
	OK = '\033[32m'
	WARNING = '\033[33m'
	FAIL = '\033[31m'
	RESET = '\033[0m'

def ok_block():
	return bcolors.OK + '[ OK ]' + bcolors.RESET

def error_block():
	return bcolors.FAIL + '[ X ]' + bcolors.RESET

def warning_block():
	return bcolors.WARNING + '[ ! ]' + bcolors.RESET1