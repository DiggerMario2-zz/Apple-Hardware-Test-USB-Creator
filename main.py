import subprocess

from yes_no import query_yes_no
from usb_detection import set_color, get_usb_drives
from tsv_parse import search_for_mac

def main():
    # Check what model Mac AHT USB is running on
    detected_model = ((subprocess.check_output(['sysctl',
                                               'hw.model'])).split()[1]).decode('utf-8')

    # Prompt user, ask if they would like to create a USB drive for this Mac
    question = ("\nWould you like to create an AHT USB drive for this Mac?" +
                set_color('Y') + " (" + detected_model + ")" + set_color('W'))
    
    answer = query_yes_no(question, default="no")

    if not answer:
        exit("Exiting...")

    # Download database from Google Drive and search for the model of mac
    url = "https://docs.google.com/spreadsheets/d/1gOJojOPvraYwDOTVH7aGXrFKMD9xXGJTAUowSY8kHfE/pub?gid=0&single=true&output=tsv"

    download_link = search_for_mac(detected_model, url)

    # Download DMG of AHT for the specific Mac Model
    print((set_color('M') +
           "\nDownloading appropriate Apple Hardware Test DMG image..."))
    download_status = subprocess.call(['curl', '-O', download_link])

    if download_status == 0:
        print((set_color('G') +
              "Downloaded Apple Hardware Test DMG image successfully" +
              set_color('W')))
    else:
        print((set_color('R') + "\nDownload failed :( " + set_color('W')))

    # Query system_profiler for valid removable USB media
    print((set_color('M') + "\nLooking for USB drives..." + set_color('W')))

    valid_usb_drives = get_usb_drives()

    if len(valid_usb_drives) != 0:
        print((set_color('G') + "Found " + str(len(valid_usb_drives)) +
              " USB drive(s)" + set_color('W')))
    else:
        quit(set_color('R') + "No USB drives found!" + set_color('W'))

    # Query user to choose USB media
    print('\nWhich USB drive would you like to use?\n')

    select = 1
    for drive in valid_usb_drives:
        print(("  " + str(select) + ".) " + set_color('Y') + '"' +
               drive["volumes"][0]["_name"] + '" ' +set_color('W') +
               drive["size"] + " " + drive["bsd_name"] + "\n"))
        select += 1

    usb_selection = int(eval(input("Please enter a number: ")))

    # If an invalid answer is given, exit the program
    if usb_selection > len(valid_usb_drives) or usb_selection < 1:
        quit("\nInvalid Answer...")

    # Double check with the user, ensure they are ok wiping there flashdrive
    question = (set_color('Y') + '\n"' +
                valid_usb_drives[usb_selection - 1]["volumes"][0]["_name"] +
                '" ' + set_color('W') +
                "will be completely erased. Are you sure?")

    answer = query_yes_no(question, default="no")

    if answer:
        # Create a string to address the USB disk by it's disk name
        valid_disk_string = ('/dev/' +
                             str(valid_usb_drives[usb_selection - 1]
                                 ["bsd_name"]))
        
        # Grab the name of the DMG file from the old download link
        dmg_image_string = download_link[51:]

        # Unmount the USB disk prior to wiping
        print((set_color('M') + "\nStarting unmount of " +
               valid_disk_string + "..." + set_color('G')))

        print(subprocess.check_output(['sudo', 'diskutil', 'unmountDisk', valid_disk_string]).decode('utf-8') + set_color('W'))

        # Re-Partition the disk w/ a GUID table and single primary HFS+ J partition

        print((set_color('M') + "Starting erasure/partitioning of " +
               valid_disk_string + "..." + set_color('G')))

        print((subprocess.check_output(['sudo', 'diskutil', 'partitionDisk',
                                        valid_disk_string, 'GPT', 'JHFS+',
                                        'AHT_USB', '0b']).decode('utf-8') + set_color('W')))

        # Mount disk image that contain the AHT suite, also extra string split magic
        print((set_color('M') + "\nStarting mount of " + dmg_image_string +
               "..."))
        mount_output_string = subprocess.check_output(['sudo', 'hdiutil',
                                                       'mount',
                                                       dmg_image_string]).decode('utf-8')

        disk_image_mount = ((("/Volumes/" +
                              mount_output_string.split("/Volumes/")[1])
                             .split("\n"))[0] + "/")
        print((set_color('G') + dmg_image_string + " is mounted at " +
               disk_image_mount + set_color('W')))

        # Copy files from mounted AHT disk image to newly partitioned USB drive
        print((set_color('M') + "\nStarting copying of " + dmg_image_string +
               " contents to " + "/Volumes/AHT_USB/" + "..." + set_color('M')))
        print((set_color('G') + "Copy Complete :)" +
               subprocess.check_output(['cp', '-r', disk_image_mount,
                                        "/Volumes/AHT_USB/"]).decode('utf-8') + set_color('W')))

        volume_name_string = ("/Volumes/" + valid_usb_drives[usb_selection-1]
                              ["volumes"][0]["_name"] + "/")

        efi_label = detected_model + " AHT USB"

        # "Bless" parts of the new USB disk to make it selectable at EFI boot menU
        print((set_color('M') + "\nStarting blessing of " +
               volume_name_string + "..." + set_color('W')))

        print((set_color('G') +
               "In the name of the Father, Son, and Holy Spirt :D\n" +
               set_color('W') +
               subprocess.check_output(['sudo', 'bless', '--folder',
                                        '/Volumes/AHT_USB/', '--file',
                                        '/Volumes/AHT_USB/System/Library' +
                                        '/CoreServices/.diagnostics' +
                                        '/diags.efi', '--label',
                                        efi_label]).decode('utf-8')))

if __name__ == "__main__":
    main()
