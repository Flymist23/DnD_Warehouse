@echo off 

where python > tmpFile 
set /p myvar= < tmpFile 



%myvar% "PyScripts\Get_DnD_Raw_From_Repos.py"
ECHO raw data from repository archived as Raw_GitHub_Dataset CSV

%myvar% "PyScripts\Remove_column.py"
ECHO columns have been removed and data is now stored in buffer CSV

%myvar% "PyScripts\CSV_to_JSON.py"
ECHO file data format has been changed to JSON and stored in nd-proceesed-dnd_players JSON


PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& {Start-Process PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File "".\DeleteNullPlayers.ps1""' -Verb RunAs}"

%myvar% "PyScripts\Clean_and_Make_KVPairs.py"
ECHO file data has been filered, cleaned, and preped to be pushed to bucket

ECHO push data to bucket by manually running Push_DnD_Data_to_GCP PY
del tmpFile 
pause
ECHO
ECHO Continue if you want to delete all data; Otherwise, exit
del "DnD_Data\*.*" /s /f /q
del "DnD_DataBuffers\*.*" /s /f /q
echo Done!