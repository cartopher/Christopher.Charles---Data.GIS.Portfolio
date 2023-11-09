# ArcGIS Online: Data Management and Backup Automation

This code automates the process of exporting a GIS data item, managing the resulting files, and then cleaning up unnecessary files from the GIS content. 
It's structured to carry out several GIS data management tasks in sequence. Here's a step-by-step explanation:


1. **Import Libraries:** Loads required Python libraries for the script to function.
    - `arcgis.gis` for interacting with ArcGIS Online or Portal for ArcGIS.
    - `IPython.display` for displaying outputs in an IPython environment such as Jupyter notebooks.
    - `os` for interacting with the operating system, e.g., file paths.
    - `datetime` for working with dates and times.
    - `pandas` for data manipulation and analysis.
    - `zipfile` for working with zip files.

2. **Function Definitions:**
    - `create_gis_connection`: Creates a connection to an ArcGIS Online account or portal. If no credentials are provided, it connects to the default 'home' account.
    - `export_data_item`: Exports a GIS data item by its ID to a specified format (CSV by default) and returns the export result.
    - `download_and_extract_data_item`: Downloads the exported data item and extracts it from a zip file to a specified output path.
    - `read_data_to_dataframe`: Reads a CSV file into a pandas DataFrame.
    - `clean_up_content_item`: Searches for and deletes GIS content items that match a specific title pattern.

3. **Main Process (`main` function):**
    - Establishes a GIS connection.
    - Defines an `item_id` to work with.
    - Sets an `output_path` for downloaded files.
    - Executes the export of the specified data item.
    - If the export is successful, it proceeds to download and extract the data item.
    - Reads the extracted CSV file into a DataFrame.
    - Displays the head (first few lines) of the DataFrame.
    - Isolates and displays useful columns from the DataFrame.
    - Cleans up any old content items that match the pattern 'Assessment_Backup'.
    - Uploads the CSV file back to the GIS content.
    - Displays the new GIS content item for the uploaded CSV.

4. **Execution Control:** The script will only run the `main` function if it is the main module executed by Python (not if it's imported as a module in another script).

```python
# IMPORT LIBRARIES
from arcgis.gis import GIS
from IPython.display import display
import os
import datetime as dt
import pandas as pd
import zipfile

# Function definitions for operations
def create_gis_connection(portal=None, username=None, password=None):
    if portal and username and password:
        return GIS(portal, username, password)
    else:
        return GIS("home")

def export_data_item(gis, item_id, export_format='CSV'):
    try:
        data_item = gis.content.get(item_id)
        export_title = 'Assessment_Backup_' + dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        export_result = data_item.export(export_title, export_format, parameters=None, wait=True)
        return export_result
    except Exception as e:
        print(f"An error occurred while exporting: {e}")
        return None

def download_and_extract_data_item(export_result, output_path):
    try:
        export_result.download(save_path=output_path)
        with zipfile.ZipFile(os.path.join(output_path, export_result.name + '.zip')) as zip_ref:
            zip_ref.extractall(output_path)
        return True
    except Exception as e:
        print(f"An error occurred while downloading or extracting: {e}")
        return False

def read_data_to_dataframe(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"An error occurred while reading CSV to DataFrame: {e}")
        return None

def clean_up_content_item(gis, title_pattern):
    search_result = gis.content.search(query=f"title:{title_pattern}_*", item_type='CSV')
    for item in search_result:
        item.delete()

# Main process flow
def main():
    gis = create_gis_connection()
    item_id = 'cb879255641849418c185e5b27dac97d'
    output_path = '/arcgis/home/'

    # Export data item and download it
    export_result = export_data_item(gis, item_id)
    if export_result:
        success = download_and_extract_data_item(export_result, output_path)
        if success:
            file_path = os.path.join(output_path, export_result.name + '.csv')
            df = read_data_to_dataframe(file_path)
            if df is not None:
                display(df.head())
                useful_columns = df[["InstitutionName", "ProviderCountCode", "MailingAddress"]]
                display(useful_columns)

                # Clean up after the process
                clean_up_content_item(gis, 'Assessment_Backup')

                # Add the CSV from unzipped file to content
                csv_item_properties = {'title': 'Assessment CSV Backup', 'type': 'CSV'}
                csv_item = gis.content.add(item_properties=csv_item_properties, data=file_path)
                display(csv_item)
            else:
                print("DataFrame is empty.")
        else:
            print("Failed to download and extract data item.")
    else:
        print("Failed to export data item.")

# Run the main process
if __name__ == "__main__":
    main()
```


