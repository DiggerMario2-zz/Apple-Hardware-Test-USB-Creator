import urllib.request
import colorama

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

def search_for_mac(desired_model, url):  
    """
    Downloads a "Tab Separate Value" database from the supplied "url",
    searches for the argument supplied "desired_model", and returns the
    associated "download_link" for said model.

    1. The returned value from "urllib.request" is a binary.
    2. This binary must be decoded into a string.
    3. The string is then split on line breaks to make it a searchable list.
    """

    print(set_color('M') +
          "\nAttempting to download database of availible mac models... " +
          set_color('W'))

    #Retrieve binary response from urllib.request
    try:
        binary_response = urllib.request.urlopen(url).read()
    
    except urllib.error.URLError as error:
        exit(set_color('R') +
              "ERROR: Database download failed:\n" +
              str(error) +
              set_color('W'))
    
    print(set_color('G') +
          "Database downloaded" +
          set_color('W'))

    #Decode binary into 'UTF-8' string
    string_response = binary_response.decode('utf-8')

    #Split string on line breaks
    mac_list = string_response.split('\r\n')

    print(set_color('M') +
          "\nSearching database for " +
          set_color('Y') +
          desired_model +
          set_color('M') +
          " download link..." +
          set_color('W'))
    
    #Search "mac_list" for "desired_model", return "download_link"
    download_link = ([x.split('\t')[1]
                      for x in mac_list if x.find(desired_model) != -1])                   
    
    if download_link:
        print(set_color('G') +
              "Successfully found link for model: " +
              set_color('Y') +
              desired_model +
              set_color('G') +
              "\nLink: " +
              set_color('Y') +
              download_link[0] +
              set_color('W'))
        return (download_link[0])
    
    else:
        exit(set_color('R') + 
              "ERROR: Unable to find link for model: " +
              set_color('Y') +
              desired_model +
              set_color('R') +
              ":\nPlease verify manually at https://goo.gl/U1OOJt" +
              set_color('W'))

#url = 'https://docs.google.com/spreadsheets/d/1gOJojOPvraYwDOTVH7aGXrFKMD9xXGJTAUowSY8kHfE/pub?gid=0&single=true&output=tsv'
#model = 'MacMini4,1'

#search_for_mac("Ponies", url)