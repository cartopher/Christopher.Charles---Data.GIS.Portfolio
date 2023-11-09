# ArcGIS Online: Feature Service Backup Script
This script is designed to log into an ArcGIS Online account and back up files. It defines a function login_and_backup that automates the process of exporting and downloading items from a user's content in ArcGIS Online to a local file geodatabase (FGDB). The script uses the ArcGIS Python API to interact with the user's content on ArcGIS Online.

The code you've provided is a Python script designed to work with the ArcGIS platform. Here's what it does step by step:

1. **Import Modules**: It imports necessary Python modules such as `arcgis.gis` for interacting with ArcGIS Online, `datetime` for working with dates and times, and `getpass` for securely getting a password input from the user.

2. **Define download_as_fgdb Function**:
   - This function takes a list of ArcGIS Online items and a backup location as arguments.
   - It iterates through each item in the list and checks if the item is a view-only service. If it's not a view service, it proceeds to export the item as a "File Geodatabase".
   - It names the exported file with the item's title followed by the current date and time to ensure uniqueness.
   - Once the export is complete, it downloads the file to the specified backup location and then deletes the exported file from ArcGIS Online.

3. **Define login_and_backup Function**:
   - This function prompts the user for their ArcGIS Online username and password (securely, without displaying the password).
   - It establishes a connection to an ArcGIS Online account using the provided credentials.
   - It then asks the user for a backup location path where the downloaded geodatabases should be stored and how many items the user wants to back up.
   - A search query is performed on the user's content in ArcGIS Online to find feature services owned by the user. The search results are limited to the number specified by the user.
   - It lists out the items that are found and will be backed up.
   - The user is then asked to confirm if they are ready to download the items.
   - If the user confirms with 'y', the `download_as_fgdb` function is called with the list of items and the backup location to start the download process.

4. **Execute login_and_backup Function**:
   - Finally, the script waits for the user to enter their ArcGIS Online username and then calls the `login_and_backup` function to initiate the backup process.

This script is particularly useful for automating the backup of ArcGIS Online feature services to local storage as file geodatabases, which is a common data backup and disaster recovery practice.

```python
from arcgis.gis import GIS
import datetime as dt
import getpass

def download_as_fgdb(item_list, backup_location):
    for item in item_list:
        try:
            if 'View Service' in item.typeKeywords:
                print(f"{item.title} is a view, not downloading.")
            else:
                print(f"Downloading {item.title}")
                version = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
                result = item.export(f"{item.title}_{version}", "File Geodatabase")
                if result:
                    result.download(backup_location)
                    result.delete()
                    print(f"Successfully downloaded {item.title}")
        except Exception as e:
            print(f"An error occurred downloading {item.title}: {e}")

def login_and_backup(username, portal_url="https://arcgis.com"):
    password = getpass.getpass(prompt='Enter your ArcGIS password: ')
    gis = GIS(portal_url, username, password)
    backup_location = input("Please enter the file location to store the backups: ")
    num_items = int(input("How many items do you want to back up? "))
    query_string = f"type:Feature Service, owner:{username}"
    items = gis.content.search(query=query_string, max_items=num_items, sort_field='modifed', sort_order='desc')
    print(f"{len(items)} items will be backed up to {backup_location}. See the list below:")
    for item in items:
        print(item)
    
    ready = input("Are you ready to download? [y/n]: ").lower().strip()
    while ready not in ['y', 'n']:
        ready = input("Please enter 'y' to proceed or 'n' to cancel: ").lower().strip()
    if ready == 'y':
        download_as_fgdb(items, backup_location)

# Usage
username = input("Enter your ArcGIS Online username: ")
login_and_backup(username)
```
