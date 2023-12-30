Analyst Project for Minnesota Twins by Roy Krishnan.

Return from Injury (RFI) metric check over time to look at player metrics is done in three parts. 

The first, data_clean_sort.py is done to clean up our data, empty null values, round to correct significant figures etc. 

PlayerSort.py then sorts files out using PlayerID as this is the unique identifier and primary key 
in separating each players respective data, each time this script is run it will update player files 
accordingly as well as account for any new players. 

This script also further cleans by removing any tests that are sequence "4" or higher.
The reason: research has shown that after four or so trials metric reliability is becomes slightly more questionable due to athlete fatigue. 


Finally, RFI_check in PlayerID_RFI creates the visuals for variables we deem as important in a player's return from injury. Files are run in the following order: data_clean_sort.py, PlayerSort.py, and then RFI_check.py. Running the main.py assures that the files are run in the correct order. 
