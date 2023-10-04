# Automating ArcGIS Feature Layer Updates for Hospice Services

## Objective
The primary objective of this code is to automate the process of updating a GIS (Geographical Information Systems) feature layer with new data. Specifically, it deals with datasets related to hospice services. Here's how it works:

### Steps
1. **Read Existing Data**: It first reads an existing dataset (`Hospice_testing.csv`) into a Pandas DataFrame.
2. **Ingest New Data**: It reads new, updated data (`Hospice_update.csv`) into another DataFrame.
3. **Merge & De-duplicate**: Combines both datasets and removes duplicates based on a unique ID (`InstitutionID`).
4. **Data Storage**: Saves this updated dataset to a new folder (`updated_hospice`).
5. **Upload to ArcGIS**: Uploads the new CSV file to the ArcGIS Online portal with a unique timestamp.
6. **Feature Layer Update**: Finally, it overwrites an existing feature layer in the ArcGIS portal with the new, updated data.

By structuring it this way, the code efficiently updates GIS data while ensuring data integrity and making the process easily repeatable.

### Code
```python
# Import Libraries
import os
import datetime as dt
import pandas as pd
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection
```

```python
# Initialize GIS
gis = GIS("home")
```

```python
# Constants
DATA_PATH = "/arcgis/home/"
TARGET_CSV = 'Hospice_testing.csv'
SOURCE_CSV = 'Hospice_update.csv'
UNIQUE_ID = 'InstitutionID'
NEW_FOLDER = 'updated_hospice'
```

```python
# Function to read CSV as DataFrame
def read_csv_as_df(file_path):
    return pd.read_csv(file_path)
```

```python
# Function to upload CSV to ArcGIS Online
def upload_csv_to_agol(gis, title, file_path):
    item_prop = {'title': title}
    return gis.content.add(item_properties=item_prop, data=file_path)
```

```python
# Function to create a new directory
def create_new_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
```

```python
# Main Execution
if __name__ == "__main__":
    # Create a unique timestamp
    now = int(dt.datetime.now().timestamp())
    
    # Read Target and Source DataFrames
    target_df = read_csv_as_df(os.path.join(DATA_PATH, TARGET_CSV))
    source_df = read_csv_as_df(os.path.join(DATA_PATH, SOURCE_CSV))
    
    # Append and Remove Duplicates
    updated_df = target_df.append(source_df)
    updated_df.drop_duplicates(subset=UNIQUE_ID, keep='last', inplace=True)
    
    # Create New Folder for Updated Data
    new_folder_path = os.path.join(DATA_PATH, NEW_FOLDER)
    create_new_folder(new_folder_path)
    
    # Save Updated DataFrame as CSV
    updated_csv_path = os.path.join(new_folder_path, TARGET_CSV)
    updated_df.to_csv(updated_csv_path, index=False)
    
    # Upload Updated CSV to ArcGIS Online
    upload_csv_to_agol(gis, f'hopicestarget{now}', updated_csv_path)
    
    # Overwrite Feature Layer
    fl_item = gis.content.get("4ffdafc5461d48ecb13d854fede083bf")
    flayer_collection = FeatureLayerCollection.fromitem(fl_item)
    flayer_collection.manager.overwrite(updated_csv_path)
```

### Best Practices
1. **Organized Imports**: Keep all your imports at the top, neatly arranged.
2. **Constants**: No magic strings or numbers. Define them once, reuse them.
3. **Functions**: Modularize your code into functions for easier testing, debugging, and understanding.
4. **Main Execution**: Everything kicks off here, in a linear and easy-to-follow manner.

---
