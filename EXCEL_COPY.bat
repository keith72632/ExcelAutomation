if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
@echo off
python "C:\Users\Carroll Boone Water\Desktop\2021_ADH_Reports\Working_Directory\ExcelAuto\main.py" "CARROLL-BOONE WATER DISTRICT" "TEST"
exit

