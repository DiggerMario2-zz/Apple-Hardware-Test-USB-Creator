"""Detect Mass Storage devices connected via USB"""

import subprocess
import plistlib
import colorama

def indenter(indent_value):
    """Indent text per its level in the XML file"""
    single_indent = "* "
    indent = ""
    if indent_value > 0:
        while indent_value > 0:
            indent += single_indent
            indent_value -= 1
    else:
        indent = ""
    return indent

def set_color(color):
    """Color text per a supplied argument."""
    if color == 1 or color == 'W' or color == 7:
        new_text_color = colorama.Fore.WHITE
    if color == 2 or color == 'R' or color == 8:
        new_text_color = colorama.Fore.RED
    if color == 3 or color == 'G' or color == 9:
        new_text_color = colorama.Fore.GREEN
    if color == 4 or color == 'Y' or color == 10:
        new_text_color = colorama.Fore.YELLOW
    if color == 5 or color == 'M' or color == 11:
        new_text_color = colorama.Fore.MAGENTA
    if color == 6 or color == 'C' or color == 12:
        new_text_color = colorama.Fore.CYAN
    return new_text_color

def traverse_plist(plist_object, indent_value, plist_map, valid_usb_drives):
    """Crawl supplied plist XML file for USB Mass Storage drives"""
    #indent = indenter(indent_value)
    #indent = indenter(indent_value)

    if  (not isinstance(plist_object, plistlib._InternalDict) or
         not isinstance(plist_object, list)):
        indent_value += 1
        plist_map = plist_map + [plist_object]
        #print (set_color(indent_value) + indenter(indent_value) +
               #(type(plist_object).__name__).upper() + " VAL: " +
               #str(plist_object) + set_color('W')
        #print (set_color(indent_value) + indenter(indent_value) + "PATH: " +
               #str(plist_map) + set_color('W')

    if isinstance(plist_object, list):
        indent_value += 1
        #print (set_color(indent_value) + indenter(indent_value) +
               #"LIST START" + set_color('W')
        for index, item in enumerate(plist_object):
            traverse_plist(item, indent_value, plist_map +
                           [index], valid_usb_drives)

    if isinstance(plist_object, plistlib._InternalDict):
        indent_value += 1
        #print (set_color(indent_value) + indenter(indent_value) +
               #"DICT START" + set_color('W')

        if ('detachable_drive' in plist_object and
                'removable_media' in plist_object):
            #print (set_color('G') +
                    #'\nFound "detachable_drive" and "removable_media"' +
                    #set_color('W')

            if (plist_object['detachable_drive'] == 'yes' and
                    plist_object['removable_media'] == 'yes'):
                #print (set_color('G') +
                 #'Both "detachable_drive" and "removable_media" are "yes"' +
                  #set_color('W')
                valid_usb_drives.append(plist_object)

            #else:
                #print (set_color('R') +
                #'Either "detachable_drive" or "removable_media" are "no"' +
                 #set_color('W')

        for key in plist_object:
            #print (set_color(indent_value) + indenter(indent_value) +
                    #"KEY: " + key + set_color('W')
            traverse_plist(plist_object[key], indent_value, plist_map +
                           [key], valid_usb_drives)
    return valid_usb_drives


def get_usb_drives():
    """Enumerate USB Drives attached to Mac"""
    plist_string = (subprocess.Popen(["system_profiler", "SPUSBDataType",
                                      "-xml"], stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE).communicate())
    plist_object = plistlib.readPlistFromString(plist_string[0])
    valid_usb_drives = traverse_plist(plist_object, 0, [], [])
    return valid_usb_drives
