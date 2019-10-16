This is the ETL portion of my project

for convenience sake, I'm not forcing users to get the repository where
the uniqueTable.tsv is from. Instead I've made a folder for it.
This makes it much easier for Peers to review it. In production that folder 
would house the repository and the relative data file path of Get_DnD_Raw_From_Repos.py
would be different. Furthermore, that would allow for automatic updates
when the remote repository updates.

Purpose of these the files in these folders is to show the data pipeline and under normal circumstances 
wouldn't likely be unecessary to house on a local machine.

THE POWERSHELL SCRIPT LIKELY NEEDS TO BE MANUALLY EXECUTED
NOTE: ALL PATHS ARE RELATIVE WHERE APPLICABLE
    -some may need changing
    -Also the Powershell script may need to be manually run

Pre-reqs:
    python version 3.7
    access to Google Cloud Platform
        -only requires a gmail account
    GitHub repository 


folders:
    Atempt_1 is a previous attempt at making an e-sports data warehouse and is only included as an indication 
        of where the project started
    DnD_Data is a folder of data b efore is uploaded to Google's Cloud Platform

Data pipeline:


Scheduler (Windows Task Scheduler):
    -runs once every week on mondays
    -the .bat file will attempt to find path to python with "where python" command
    -Get_DnD_Raw_From_Repos.py
        -NOTE: requires local repository of "https://github.com/oganm/dnddata"and path to local repository file docs\\uniquetable.tsv
        -imports:
            -re
    -CSV_to_JSON.py
        -requires:
            -json library
            -csv library
            -IO library
    -Remove_column.py
        -imports:
            -csv
    -Clean_and_Make_KVPairs.py
        -imports:
            -json library
            -string library
    -DeleteNullPlayers.ps1
        -likely needs to be run manually, if you have your PC set up that way
Scheduled 