@echo off
If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory" && echo "Working_Directory created"
) Else echo "C:\Users\Carroll Boone Water\Documents\Working_Directory already exists" 

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\Chemical_Treatment_Records" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\Chemical_Treatment_Records" && echo "Chemical_Treatment_Records created"
) Else echo "C:\Users\Carroll Boone Water\Documents\Working_Directory\Chemical_Treatment_Records already exists"

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\East_Plant_Operations_Reports" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\East_Plant_Operations_Reports" && echo "East_Plant_Operations_Reports created"
) Else echo "C:\Users\Carroll Boone Water\Documents\Working_Directory\East_Plant_Operations_Reports already exists"

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\MangoLogs" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\MangoLogs" && echo "MangoLogs created"
) Else echo "C:\Users\Carroll Boone Water\Documents\Working_Directory\MangoLogs already exists"

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\West_Plant_Operations_Reports" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\West_Plant_Operations_Reports" && echo "West_Plant_Operations_Reports created"
) Else echo "C:\Users\Carroll Boone Water\Documents\Working_Directory\West_Plant_Operations_Reports already exists"

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\Chemical_Treatment_Records\Chlorine_Tables" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\Chemical_Treatment_Records\Chlorine_Tables" && echo "Chlorine_Tables created"
) Else echo "C:\Users\Carroll Boone Water\Documents\Working_Directory\Chemical_Treatment_Records\Chlorine_Tables already exists"

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\DocumentsPDFS\files" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\DocumentsPDFS\files" && echo "Files created"
) Else echo "C:\Users\Carroll Boone Water\Documents\Working_Directory\DocumentsPDFS\files already exists"

If not exist "C:\Users\Carroll Boone Water\Documents\Working_Directory\DocumentsPDFS\finals" (
	mkdir "C:\Users\Carroll Boone Water\Documents\Working_Directory\DocumentsPDFS\finals" && echo "Finals created"
) Else echo "C:\Users\Carroll Boone Water\Documents\Working_Directory\DocumentsPDFS\finals already exists"

echo "finished"
pause
