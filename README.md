# Apple-Hardware-Test-USB-Creator
Create a self contained "Apple Hardware Test" USB flash drive for D.I.Y. Mac® hardware diagnostics and troubleshooting

[Design Doc](https://github.com/DiggerMario2/Apple-Hardware-Test-USB-Creator/blob/master/DESIGNDOC.md) | [Issue Tracker](https://github.com/DiggerMario2/Apple-Hardware-Test-USB-Creator/pulls) | [Coding Style](https://www.python.org/dev/peps/pep-0008/)

Apple Hardware Test USB Creator is a program used to simplify the aquisition and use of the "Apple Hardware Test" suite of Mac hardware diagnostics software. 
* Apples's software is NOT MODIFIED in any way through the use of this tool. 
* The authors of this tool are not affiliated with Apple Inc.
* "Mac" and "Apple Hardware Test" are [registered trademarks of Apple Inc](http://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html).

This software is licensed under the terms of the [GNU General Public License, version 3 or later (GPLv3+)](https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)).

## System Requirements
* OS
    * OS X (10.11 El Capitain or higher).
* Hardware
    * At least one working USB port
    * A flash drive 64MB or greater in size
* Software
    * Python 2.7
    * Python Modules: Colorama, Gdata, and PlistLib

## Installation Steps
* Open "Terminal"
* "cd" to the program's downloaded directory
* Run "sudo Python main.py"

## Change Log
* 0.0.0 Jan 14, 2016 - Design Doc and Prototype
    * Demo
        * Pyusb and usblib to read devices on usb bus
        * Gdata API documented
    * Design doc w/ flowcharting
* 0.1.0 Jan 28, 2016 - Initial Github push
    * CLI formatting of USB drives works    
    * Python 2.7
    * Gdata API used to retrive Google Sheets data
* 0.2.0 Jan 28, 2016 - Migration to Python 3, Optimizations
    * Migrated to Python 3.x
       * urllib replaces gdata for retrieval of data
       * plistlib functions changed to accomodate 3.x deprecations


## Credits and Thanks
* [upekkha](https://github.com/upekkha/AppleHardwareTest) for the initial compilation of information regarding manual creation of Apple Hardware Test USB flash drives.
* [Google ITRP](https://www.google.com/about/careers/search#!t=jo&jid=3395002&): Take chances, make mistakes, get messy
