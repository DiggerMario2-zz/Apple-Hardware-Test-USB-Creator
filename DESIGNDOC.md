# Apple Hardware Test USB Creator

* Status: Draft
* Authors: jakecoggiano@gmail.com
* Last Updated: 2015-01-28

### Objective
Enable users of OS X to quickley and easily create a self contained "Apple Hardware Test" USB flash drive for D.I.Y. Mac® hardware diagnostics and troubleshooting

### Background
Apple Hardware Test (henceforth referred to as AHT) is an Apple hardware diagnostics and troubleshooting tool designed for for use with Macs manufactered between 2007 and 2013.

The tool is factory installed in the "/System/Library/CoreServices/.diagnostics" directory of OS X, and can be accessed at boot by holding the “D” key during the classic Mac startup chime. 

Unfortunaley, like any other file on your hard drive, the AHT directory can inadvertantly be trashed. Often times this will occur during an OS reinstallation, leaving the new Mac OS X install without a functioning AHT Suite.

###Overview

The Apple Hardware Test USB Creator restores the fuctionality of the AHT suite by downloading a fresh copy from Apple servers, and saving it to a portable USB thumb drive that users can store away for safe keeping. 

Instructions for the manual creation of a flash frive based AHT suite can be found at the following github page:
https://github.com/upekkha/AppleHardwareTest/blob/master/Readme.markdown

Apple Hardware Test USB Creator is an attempt to roll the functionality of these instructions into an easy “Point and Click” application for OS X. The application should be easy enough for a novice to wield, yet useful enough for the lazy sysadmin.

### Detailed Design Flow
https://drive.google.com/open?id=13j950hTZJLbgcB8Qs7sKNt99sb3GFS1VSrWvdfLkHCI

### Project Information
* Python 3.x (Core functionality)
* Bash (Commands sent via Python Subprocess)
* Google Sheets (Rudimentary database)
* PyQt x.x (GUI)

### Caveats
A rock solid CLI version must be created before embarking on the PyQt portion of this project. However,  without a PyQt version of this program, the core Mac audience will be uncomfortable weilding this tool.

### Security Considerations
The script requires superuser privileges in order to perform certain core functions:
* Flash drive unmount/mount, partitioning, and blessing

### Privacy Considerations
Users need to understand that the only statistical data send back to the App Devs is the following:
* Mac Model
* Version of program
* Did the script fail and if so why...

### Testing Plan
Build CLI prototype and run it against multiple Mac models. Once a rock solid CLI tool has been created development can shift to creating a PyQtbased GUI.

###Resources
* [Python Style Guide](https://google.github.io/styleguide/pyguide.html)
* [Python Exception Handling](http://www.programiz.com/python-programming/exception-handling)
* [Python CSV imports](https://www.quora.com/Why-is-my-Python-code-not-downloading-the-CSV-file)
* [Strings Python 2 vs 3](http://chimera.labs.oreilly.com/books/1230000000393/ch05.html#_solution_73)

####Working with Gdata
* [Retrieve Data from Public Google Spreadsheet Using Gdata Library](http://stackoverflow.com/questions/7561148/retrieve-data-from-public-google-spreadsheet-using-gdata-library)
* [Getting the worksheet feed for a given spreadsheet](http://gdatatips.blogspot.com/2008/08/getting-worksheet-feed-for-given.html)
* [Using-the-Google-Drive-Spreadsheet-API](http://heinrichhartmann.com/2015/05/17/Using-the-Google-Drive-Spreadsheet-API.html)
* [gdata.spreadsheet.service.CellQuery](http://nullege.com/codes/search/gdata.spreadsheet.service.CellQuery)
* [using-google-python-api-to-get-rows-from-a-google](http://mrwoof.tumblr.com/post/1004514567/using-google-python-api-to-get-rows-from-a-google)
* [Google Spreadsheets API Chapter 17](http://mashupguide.net/1.0/html/ch17s08.xhtml)

####Yes/No Python Function
[python-command-line-yes-no-input](http://stackoverflow.com/questions/3041986/python-command-line-yes-no-input)

####CLI Formatting of Drives
[Part 1](http://www.theinstructional.com/guides/disk-management-from-the-command-line-part-1)
[Part 2](http://www.theinstructional.com/guides/disk-management-from-the-command-line-part-2)
[Part 3](http://www.theinstructional.com/guides/disk-management-from-the-command-line-part-3)
[Using the hidutil](http://commandlinemac.blogspot.com/2008/12/using-hdiutil.html)

####plist Lib
[PSTLib.py](https://hg.python.org/cpython/file/2.7/Lib/plistlib.py)
[plistlib changes from Python 2 to 3](https://docs.python.org/3/library/plistlib.html#plistlib.load)
