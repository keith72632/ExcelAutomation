from lib.colors import Prompts

def process_exceptions(exceptions):
	p = Prompts()
	if exceptions > 0:
		print(f'{p.err()}Errors: {exceptions}\n')
	else:
		print(f'{p.ok()}Proccess complete with zero errors\n')

def cmd_banner(msg):
	print('\033[43m' + ('*' * 60))
	print(msg)
	print(('*' * 60) + '\033[0m')
