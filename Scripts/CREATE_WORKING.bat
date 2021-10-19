@echo off
If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory" && echo "Working_Directory created"
)

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\Chemical_Treatment_Records" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\Chemical_Treatment_Records" && echo "Chemical_Treatment_Records created"
)

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\East_Plant_Operations_Reports" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\East_Plant_Operations_Reports" && echo "East_Plant_Operations_Reports created"
)

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\MangoLogs" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\MangoLogs" && echo "MangoLogs created"
)

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\West_Plant_Operations_Reports" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\West_Plant_Operations_Reports" && echo "West_Plant_Operations_Reports created"
)

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\Chlorine_Tables" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\Chlorine_Tables" && echo "Chlorine_Tables created"
)
echo "finished"
pause
