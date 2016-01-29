# Apple Hardware Test USB Creator

* Status: Draft
* Authors: jakecoggiano@gmail.com
* Last Updated: 2015-01-14

### Objective
Allow OS X users to quickly and easily create Apple Hardware Test USB flash drives to diagnose issues with outdated Apple hardware.

### Background
Apple Hardware Test (henceforth referred to as AHT) is a troubleshooting tool used to verify the integrity of hardware components found in Intel Apple Macs manufactured between 2007 and 2013.

The AHT suite is accessed by holding the “D” key at boot time. The tool then attempts to boot from the factory installed location of: /System/Library/CoreServices/.diagnostics

Unfortunately, OS X upgrades do not account for the presence of this tool. Often times users will unknowingly delete the AHT suite upon the clean install of a new version of OS X.

As of June 2013 Apple has replaced the Apple Hardware Test suite with a new suite of diagnostic tools known as “Apple Diagnostics”. Apple Diagnostics is only compatible with Macs manufactured post June 2013- older Macs still need the AHT suite.

###Overview
The Apple Hardware Test USB tool, is an application designed to restore the functionality of the AHT suite through the use of a portable USB flash drive. The USB tool downloads the appropriate version of the AHT suite, write it to a USB flash drive, and allow users to boot from the drive at startup.

A current application of this project can be found at the following github page:
https://github.com/upekkha/AppleHardwareTest/blob/master/Readme.markdown 

Apple Hardware Test USB is an attempt to roll the functionality of these instructions into an easy “Point and Click” application for OS X. The application should be easy enough for a novice to wield, yet useful enough for the lazy sysadmin.

### Detailed Design Flow
https://drive.google.com/open?id=13j950hTZJLbgcB8Qs7sKNt99sb3GFS1VSrWvdfLkHCI

### Project Information
* Python 2.7
* Google Cloud SQL
* Python GUI of Some Sort?

### Caveats
Creating an attractive GUI will be challenging. A simple CLI interface is doable for a prototype, but only a GUI interface will be something novice users are comfortable with.

### Security Considerations
The script requires superuser privileges in order to perform certain core functions:
* Flash drive unmount/mount, partitioning, and blessing

### Privacy Considerations
Users need to understand that the only statistical data send back to the App Devs is the following:
	* Mac Model
	* Did the script fail and if so why...

## Testing Plan
Build CLI prototype and run it against multiple Mac models. When the CLI version is solid I can consider creating a GUI
