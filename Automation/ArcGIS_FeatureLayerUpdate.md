
# Automating GIS Feature Layer Updates for Hospice Services

## Objective

Automate the process of updating a GIS feature layer with new hospice services data. The code performs the following:

1. **Read Existing Data**: Reads `Hospice_testing.csv` into a Pandas DataFrame.
2. **Ingest New Data**: Reads new, updated data (`Hospice_update.csv`) into another DataFrame.
3. **Merge & De-duplicate**: Combines both datasets and removes duplicates based on `InstitutionID`.
4. **Data Storage**: Saves the updated dataset in a new folder (`updated_hospice`).
5. **Upload to ArcGIS**: Uploads new CSV to the ArcGIS Online portal with a unique timestamp.
6. **Feature Layer Update**: Overwrites existing feature layer in ArcGIS portal.

## Code Structure

### Import Libraries

```python
import os
import datetime as dt
import pandas as pd
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection

Initialize GIS

gis = GIS("home")

Constants

DATA_PATH = "/arcgis/home/"
TARGET_CSV = 'Hospice_testing.csv'
SOURCE_CSV = 'Hospice_update.csv'
UNIQUE_ID = 'InstitutionID'
NEW_FOLDER = 'updated_hospice'

Functions

Read CSV as DataFrame

def read_csv_as_df(file_path):
    return pd.read_csv(file_path)

Upload CSV to ArcGIS Online

def upload_csv_to_agol(gis, title, file_path):
    item_prop = {'title': title}
    return gis.content.add(item_properties=item_prop, data=file_path)

Create New Folder

def create_new_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

Main Execution

if __name__ == "__main__":
    now = int(dt.datetime.now().timestamp())
    # Further code...

Best Practices

	1.	Organized Imports: Keep imports at the top, neatly arranged.
	2.	Constants: No magic strings or numbers.
	3.	Functions: Modular code for easier testing and debugging.
	4.	Main Execution: Linear and easy-to-follow main function.
