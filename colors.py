
prompt = {
	'OK': lambda    : '\033[32m[ OK ]\033[0m',
	'ERROR': lambda : '\033[31m[ X ]\033[0m',
	'WARN': lambda  : '\033[33m[ ! ]\033[0m'
}

class Prompts:
	OK = '\033[32m'
	WARNING = '\033[33m'
	FAIL = '\033[31m'
	RESET = '\033[0m'
	def __init__(self):
		pass
	def ok(self):
		return self.OK + '[ OK ]' + self.RESET
	def err(self):
		return self.FAIL + '[ X ]' + self.RESET
	def warn(self):
		return self.WARNING + '[ ! ]' + self.RESET