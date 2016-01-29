import gdata.spreadsheet
import gdata.spreadsheet.service
import colorama

def download_database(key):
    client = gdata.spreadsheet.service.SpreadsheetsService()
    #worksheets_feed = (client.GetWorksheetsFeed(key, visibility='public',
                                                #projection='values'))
    database = (client.GetCellsFeed(key, wksht_id='default', cell=None,
                                    query=None, visibility='public',
                                    projection='full'))
    return database

def search_for_mac(desired_model, database):
    num = -1

    print(colorama.Fore.MAGENTA + "\nAttempting to locate download link... " +
          colorama.Fore.WHITE)

    for i, item in enumerate(database.entry):
        #print item.cell.inputValue
        if item.cell.inputValue == desired_model:
            num = i + 1
            print(colorama.Fore.GREEN + "Successfully found link for model: " +
                  desired_model + colorama.Fore.WHITE)
            break

    if num == -1:
        print(colorama.Fore.RED + "Error: Model not found" +
              colorama.Fore.WHITE)
    else:
        download_link = database.entry[num].cell.inputValue

    return download_link
