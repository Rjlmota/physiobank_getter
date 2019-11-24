# physiobank_getter

These are some simple scripts used to request data from Physiobank ATM: https://archive.physionet.org/cgi-bin/atm/ATM, which has a large database on biosignals. But, requesting them one by one was boring and repetitive, so I created these scripts. 

## How to use
At this point, it still is a little bit harsh and not very user friendly (feel free to improve it, if you want). 
If you wanna use it, you first need to make sure that you have some things installed:
### Requirements
- Selenium: pip install selenium
- WFDB package on Physiobank website: https://archive.physionet.org/physiotools/wfdb.shtml 

### Requesting data
In order to request data, you'll have to run navigator.py, wait for the browser to open, go back to the terminal in which you ran the command and select the database you want. After this, the output will be directed to a file named "databases.txt".
Now, you'll have to edit the file make_request.py and adjust the function "make_request" according to the command you generated in the ATM webiste and the way you want the files to be named and saved.
After this, you should be able to run make_request.py without problems and the script will make the requests for you.


