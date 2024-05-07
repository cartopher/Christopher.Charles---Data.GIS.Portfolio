# Automate Feature Layer Processing, Export to Excel, and Upload to AWS Bucket and Folder

### Introduction:
This notebook automates the processing of feature layers in ArcGIS Online, specifically targeting fields related to sponsors. It fetches data from two different feature layers: "Home Form Sponsor" and "Filter Form Sponsor", filters the data based on whether the sponsor field is NULL or NOT NULL, processes it, and exports it to Microsoft Excel format. The notebook handles any existing Excel files by updating them if they already exist in the ArcGIS Online Content. Additionally, the last section of the notebook demonstrates automated uploading of specified Excel files to the designated S3 bucket and folder.


```python
# import modules
from arcgis.gis import GIS
import pandas as pd
import warnings
```


```python
# Suppress the UserWarning
warnings.filterwarnings("ignore", category=UserWarning)

# authenticate
gis = GIS("home")
```

# Home Form Sponsor

### Description:
The Home Form Sponsor Processing section of the notebook automates the retrieval, filtering, processing, and export of feature layer data from the "Home Form Sponsor" layer in ArcGIS Online. It targets features where the sponsor field is NULL, extracts relevant attribute data, renames fields, exports the data to an Excel worksheet named "Houses Unassigned," and uploads the Excel file to ArcGIS Online, handling updates if the file already exists. Additionally, it retrieves features where the "sponsor" field is NOT NULL, processes them similarly, and appends the data to the same Excel file under the worksheet named "Houses Assigned," before uploading the updated file to ArcGIS Online.


```python
# Define the Folder Name to Upload Excel Files
folder_id = "05bd20b5275e4f309b1195c73756f094"
```


```python
# Define the path to the Excel file
output_excel_path = "Home_Form_Sponsor_Assignment.xlsx"
```


```python
# Access the 'GoodJustice House Form' feature layer by its item ID
item_id = "649917bf8c434c5cb153a576b9c69742"
feature_layer_item = gis.content.get(item_id)
feature_layer = feature_layer_item.layers[0]
```


```python
# Define the fields to be exported and their corresponding names in the Excel sheet
fields_to_export = ["objectid", "Creator", "Country", "SurveyDate", "FamilyName",
                    "sponsor", "sponsorName", "sponsorEmail", "sponsorPhone", "photoLink"]

field_rename_mapping = {"objectid": "HouseID", "creator": "Collector", "Country": "Country",
                        "SurveyDate": "Form Date", "LastName": "Family Name", "sponsor": "Donor Code",
                        "sponsorName": "Donor Name", "sponsorEmail": "Donor Email",
                        "sponsorPhone": "Donor Phone", "photoLink": "Photo"}
```


```python
# Query the feature layer and retrieve the features where Sponsor is NULL
features = feature_layer.query(where="sponsor IS NULL")
```


```python
# Extract attribute data from features
data = [feature.attributes for feature in features]
```


```python
# Convert data to Pandas DataFrame for easier manipulation
df = pd.DataFrame(data)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>objectid</th>
      <th>globalid</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Accuracy</th>
      <th>SurveyTime</th>
      <th>SurveyDate</th>
      <th>Country</th>
      <th>FamilyName</th>
      <th>FamilySize</th>
      <th>...</th>
      <th>time_date</th>
      <th>int_timezone</th>
      <th>int_device_id</th>
      <th>int_device_model</th>
      <th>int_operating_system</th>
      <th>int_app_version</th>
      <th>int_survey_version</th>
      <th>int_survey_mode</th>
      <th>int_survey_status</th>
      <th>username</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>154</td>
      <td>32c236c6-d2e6-4133-a7af-5a791280f391</td>
      <td>-15.600745</td>
      <td>35.378948</td>
      <td>3.216</td>
      <td>1713270687571</td>
      <td>1713283200000</td>
      <td>Malawi</td>
      <td>Bizweck</td>
      <td>4</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>155</td>
      <td>320692df-dcf3-43f2-883d-e7d3d4105a6d</td>
      <td>-15.607880</td>
      <td>35.384740</td>
      <td>3.216</td>
      <td>1713270646793</td>
      <td>1713283200000</td>
      <td>Malawi</td>
      <td>Goman</td>
      <td>5</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 33 columns</p>
</div>




```python
# Filter DataFrame to include only specified fields
df = df[fields_to_export]
```


```python
# Filter DataFrame to include only specified fields
df = df[fields_to_export].copy()

# Rename fields according to the provided mapping
df.rename(columns=field_rename_mapping, inplace=True)
```


```python
# Create a Pandas Excel writer using XlsxWriter as the engine
with pd.ExcelWriter(output_excel_path, engine='xlsxwriter') as writer:
    # Write the DataFrame to the Excel worksheet named 'Houses Unassigned'
    df.to_excel(writer, sheet_name='Houses Unassigned', index=False)

print(f"Excel file exported with worksheet named 'Houses Unassigned'.")

# Query the feature layer and retrieve the features where Sponsor is NOT NULL
features_assigned = feature_layer.query(where="sponsor IS NOT NULL")

# Extract attribute data from features where Sponsor is NOT NULL
data_assigned = [feature.attributes for feature in features_assigned]

# Convert data to Pandas DataFrame for easier manipulation
df_assigned = pd.DataFrame(data_assigned)

# Filter DataFrame to include only specified fields
df_assigned = df_assigned[fields_to_export]

# Rename fields according to the provided mapping
df_assigned.rename(columns=field_rename_mapping, inplace=True)

# Append the 'Houses Assigned' sheet to the existing Excel file
with pd.ExcelWriter(output_excel_path, engine='openpyxl', mode='a') as writer:
    # Write the DataFrame to the Excel worksheet named 'Houses Assigned'
    df_assigned.to_excel(writer, sheet_name='Houses Assigned', index=False)

print(f"Excel file updated with worksheet named 'Houses Assigned'.")

try:
    # Upload the updated Excel file to the specified folder by ID
    file_item = gis.content.add({}, output_excel_path, folder=folder_id)
    print(f"Excel file uploaded to folder with ID '{folder_id}' in ArcGIS Online Content.")
except Exception as e:
    if "Item 'Home_Form_Sponsor_Assignment.xlsx' already exists." in str(e):
        print("Item already exists. Updating existing item...")
        existing_items = gis.content.search(query=f"title:'Home_Form_Sponsor_Assignment.xlsx'", item_type="Excel")
        if existing_items:
            existing_item = existing_items[0]
            existing_item.update(data=output_excel_path)
            print("Item updated successfully.")
        else:
            print("No existing item found.")
    else:
        raise e
```

    Excel file exported with worksheet named 'Houses Unassigned'.
    Excel file updated with worksheet named 'Houses Assigned'.
    Item already exists. Updating existing item...
    No existing item found.


# Filter Form Sponsor

### Description:

The Filter Form Sponsor Processing section of the notebook automates the retrieval, filtering, processing, and export of feature layer data from the "Filter Form Sponsor" layer in ArcGIS Online. It targets features where the sponsor field is NULL, extracts relevant attribute data, renames fields, exports the data to an Excel worksheet named "Unassigned Filters," and uploads the Excel file to ArcGIS Online, handling updates if the file already exists. Additionally, it retrieves features where the "sponsor" field is NOT NULL, processes them similarly, and appends the data to the same Excel file under the worksheet named "Assigned Filters," before uploading the updated file to ArcGIS Online.


```python
# Define the Folder Name to Upload Excel Files
folder_id = "687c26c73398426cbe5e1d5c6ad12bc3"
```


```python
# Define the path to the Excel file
output_excel_path = "Filter_Form_Sponsor_Assignment.xlsx"
```


```python
# Access the 'GoodJustice Filter Form' feature layer by its item ID
item_id = "8da9de8b78194bbe8187a76052d9e6b9"
feature_layer_item = gis.content.get(item_id)
feature_layer = feature_layer_item.layers[0]
```


```python
# Define the fields to be exported and their corresponding names in the Excel sheet
fields_to_export = ["objectid", "formType", "barcode", "Creator", "Country", "Village",
                    "FormDate", "LastName", "sponsor", "sponsorName", "sponsorEmail", 
                    "sponsorPhone", "photoLink"]

field_rename_mapping = {"objectid": "FilterID", "formType": "Form Type", "barcode": "Barcode",
                        "Creator": "Collector", "Country": "Country", "Village": "Village",
                        "FormDate": "Form Date", "LastName": "Family Name", "sponsor": "Donor Code",
                        "sponsorName": "Donor Name", "sponsorEmail": "Donor Email",
                        "sponsorPhone": "Donor Phone", "photoLink": "Photo"}

```


```python
# Query the feature layer and retrieve the features where Sponsor is NULL
features = feature_layer.query(where="sponsor IS NULL")
```


```python
# Extract attribute data from features
data = [feature.attributes for feature in features]
```


```python
# Convert data to Pandas DataFrame for easier manipulation
df = pd.DataFrame(data)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>objectid</th>
      <th>globalid</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Accuracy</th>
      <th>SurveyTime</th>
      <th>formType</th>
      <th>barcode</th>
      <th>Follow_Up_Num</th>
      <th>Country</th>
      <th>...</th>
      <th>time_date</th>
      <th>int_timezone</th>
      <th>int_device_id</th>
      <th>int_device_model</th>
      <th>int_operating_system</th>
      <th>int_app_version</th>
      <th>int_survey_version</th>
      <th>int_survey_mode</th>
      <th>int_survey_status</th>
      <th>username</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3405</td>
      <td>2debbe9d-c005-4cc1-800c-4cb732ff212e</td>
      <td>14.92286249</td>
      <td>-87.88991646</td>
      <td>3.2160000801086426</td>
      <td>1678412183919</td>
      <td>FollowUp</td>
      <td>SA056862</td>
      <td>8Weeks</td>
      <td>Honduras</td>
      <td>...</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4658</td>
      <td>55e8ed39-e5f6-4d5b-928e-21f3bfd77616</td>
      <td>14.92287519</td>
      <td>-87.88993234</td>
      <td>9.648000717163086</td>
      <td>1684954084907</td>
      <td>FollowUp</td>
      <td>SA060212</td>
      <td>8Weeks</td>
      <td>Honduras</td>
      <td>...</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4662</td>
      <td>76ce57a1-e968-4d43-8c55-24e621f2184b</td>
      <td>15.04598149</td>
      <td>-87.98635785</td>
      <td>9.648000717163086</td>
      <td>1684958330422</td>
      <td>FollowUp</td>
      <td>SA060218</td>
      <td>8Weeks</td>
      <td>Honduras</td>
      <td>...</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4693</td>
      <td>9ac6bb68-b043-46cd-bcdd-365794a6fdf0</td>
      <td>15.04599801</td>
      <td>-87.98636779</td>
      <td>9.648000717163086</td>
      <td>1684962263458</td>
      <td>FollowUp</td>
      <td>SA059571</td>
      <td>8Weeks</td>
      <td>Honduras</td>
      <td>...</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4706</td>
      <td>12c325ac-fd08-4d1a-9fca-c033e3b2fe8a</td>
      <td>15.04594459</td>
      <td>-87.98641601</td>
      <td>3.2160000801086426</td>
      <td>1684963587678</td>
      <td>FollowUp</td>
      <td>SA059557</td>
      <td>8Weeks</td>
      <td>Honduras</td>
      <td>...</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>159</th>
      <td>7944</td>
      <td>eb769645-0e70-4ba5-9ba6-75686e968e79</td>
      <td>20.88200222</td>
      <td>-76.20188784</td>
      <td>3.2160000801086426</td>
      <td>1714661624781</td>
      <td>Distribution</td>
      <td>SA704532</td>
      <td>None</td>
      <td>Cuba</td>
      <td>...</td>
      <td>1.714661e+12</td>
      <td>EDT</td>
      <td>96259c41784f4d56b2276bfc0710232b</td>
      <td>SM-T290</td>
      <td>Android  (11.0)</td>
      <td>3.19.120</td>
      <td>baypark.feb.25.2024</td>
      <td>new</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>160</th>
      <td>7945</td>
      <td>de748dc1-c708-4260-b0ac-bdf983a02bda</td>
      <td>20.88171585</td>
      <td>-76.20084072</td>
      <td>3.2160000801086426</td>
      <td>1714657435669</td>
      <td>Distribution</td>
      <td>SA704522</td>
      <td></td>
      <td>Cuba</td>
      <td>...</td>
      <td>1.714657e+12</td>
      <td>EDT</td>
      <td>96259c41784f4d56b2276bfc0710232b</td>
      <td>SM-T290</td>
      <td>Android  (11.0)</td>
      <td>3.19.120</td>
      <td>baypark.feb.25.2024</td>
      <td>new</td>
      <td>draft</td>
      <td>None</td>
    </tr>
    <tr>
      <th>161</th>
      <td>7946</td>
      <td>6c8167ec-d564-44b5-9dc9-7b3f669c6bd5</td>
      <td>20.8819976</td>
      <td>-76.20187666</td>
      <td>3.2160000801086426</td>
      <td>1714661932068</td>
      <td>Distribution</td>
      <td>SA704531</td>
      <td>None</td>
      <td>Cuba</td>
      <td>...</td>
      <td>1.714662e+12</td>
      <td>EDT</td>
      <td>96259c41784f4d56b2276bfc0710232b</td>
      <td>SM-T290</td>
      <td>Android  (11.0)</td>
      <td>3.19.120</td>
      <td>baypark.feb.25.2024</td>
      <td>new</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>162</th>
      <td>7947</td>
      <td>f4566335-e114-4f7e-adc7-2afec5b7df2a</td>
      <td>20.88204204</td>
      <td>-76.2021945</td>
      <td>3.2160000801086426</td>
      <td>1714663335455</td>
      <td>Distribution</td>
      <td>SA704534</td>
      <td>None</td>
      <td>Cuba</td>
      <td>...</td>
      <td>1.714663e+12</td>
      <td>EDT</td>
      <td>96259c41784f4d56b2276bfc0710232b</td>
      <td>SM-T290</td>
      <td>Android  (11.0)</td>
      <td>3.19.120</td>
      <td>baypark.feb.25.2024</td>
      <td>new</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>163</th>
      <td>7948</td>
      <td>7d219fc9-a78c-418e-a4e7-c01a246bdb09</td>
      <td>20.88228323</td>
      <td>-76.20184585</td>
      <td>9.648000717163086</td>
      <td>1714662633484</td>
      <td>Distribution</td>
      <td>SA704533</td>
      <td>None</td>
      <td>Cuba</td>
      <td>...</td>
      <td>1.714662e+12</td>
      <td>EDT</td>
      <td>96259c41784f4d56b2276bfc0710232b</td>
      <td>SM-T290</td>
      <td>Android  (11.0)</td>
      <td>3.19.120</td>
      <td>baypark.feb.25.2024</td>
      <td>new</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>164 rows × 114 columns</p>
</div>




```python
# Filter DataFrame to include only specified fields
df = df[fields_to_export]
```


```python
# Filter DataFrame to include only specified fields
df = df[fields_to_export].copy()

# Rename fields according to the provided mapping
df.rename(columns=field_rename_mapping, inplace=True)
```


```python
# Create a Pandas Excel writer using XlsxWriter as the engine
with pd.ExcelWriter(output_excel_path, engine='xlsxwriter') as writer:
    # Write the DataFrame to the Excel worksheet named 'Houses Unassigned'
    df.to_excel(writer, sheet_name='Unassigned Filters', index=False)

print(f"Excel file exported with worksheet named 'Unassigned Filters'.")

# Query the feature layer and retrieve the features where Sponsor is NOT NULL
features_assigned = feature_layer.query(where="sponsor IS NOT NULL")

# Extract attribute data from features where Sponsor is NOT NULL
data_assigned = [feature.attributes for feature in features_assigned]

# Convert data to Pandas DataFrame for easier manipulation
df_assigned = pd.DataFrame(data_assigned)

# Filter DataFrame to include only specified fields
df_assigned = df_assigned[fields_to_export]

# Rename fields according to the provided mapping
df_assigned.rename(columns=field_rename_mapping, inplace=True)

# Append the 'Houses Assigned' sheet to the existing Excel file
with pd.ExcelWriter(output_excel_path, engine='openpyxl', mode='a') as writer:
    # Write the DataFrame to the Excel worksheet named 'Houses Assigned'
    df_assigned.to_excel(writer, sheet_name='Assigned Filters', index=False)

print(f"Excel file updated with worksheet named 'Assigned Filters'.")

try:
    # Upload the updated Excel file to the specified folder by ID
    file_item = gis.content.add({}, output_excel_path, folder=folder_id)
    print(f"Excel file uploaded to folder with ID '{folder_id}' in ArcGIS Online Content.")
except Exception as e:
    if "Item 'Filter_Form_Sponsor_Assignment.xlsx' already exists." in str(e):
        print("Item already exists. Updating existing item...")
        existing_items = gis.content.search(query=f"title:'Filter_Form_Sponsor_Assignment.xlsx'", item_type="Excel")
        if existing_items:
            existing_item = existing_items[0]
            existing_item.update(data=output_excel_path)
            print("Item updated successfully.")
        else:
            print("No existing item found.")
    else:
        raise e
```

    Excel file exported with worksheet named 'Unassigned Filters'.
    Excel file updated with worksheet named 'Assigned Filters'.
    Item already exists. Updating existing item...
    No existing item found.


# Automated Upload of Excel Spreadsheets to AWS Bucket

### Description:
This section facilitates the upload of two Excel spreadsheets to an AWS S3 bucket. It utilizes the Boto3 library to interact with AWS services and requires the user's AWS access key ID, secret access key, and the region where the S3 bucket is located. The script defines a function `upload_to_s3` to handle the file upload process. Users specify the S3 bucket name, folder path, and file paths/names for the Excel files to be uploaded. Upon execution, the script uploads the specified Excel files to the designated S3 bucket and folder, providing feedback on the success or failure of each upload operation.


```python
# import modules
import boto3
import pandas as pd
import os
```


```python
# AWS credentials and region
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
region_name = 'us-west-1'
```


```python
# Initialize S3 client
s3 = boto3.client(
    service_name='s3',
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
```


```python
# Define function to upload Excel files to AWS S3 bucket
def upload_to_s3(bucket_name, file_path, file_name):
    try:
        # Upload the Excel file to S3 bucket
        s3.upload_file(file_path, bucket_name, file_name)
        print(f"File '{file_name}' uploaded to S3 bucket '{bucket_name}' successfully.")
    except Exception as e:
        print(f"An error occurred while uploading '{file_name}' to S3 bucket '{bucket_name}': {str(e)}")
```


```python
# Define AWS S3 bucket details
bucket_name = 'YOUR_AWS_BUCKET_NAME'
s3_folder_path = 'YOUR_S3_FOLDER_PATH/'
```


```python
# Define file names for the Excel files in the S3 bucket
excel_file1 = 'Filter_Form_Sponsor_Assignment.xlsx'
excel_file2 = 'Home_Form_Sponsor_Assignment.xlsx'
```


```python
# Upload the first Excel file
upload_to_s3(bucket_name, excel_file1, s3_folder_path + os.path.basename(excel_file1))
```

    File 'GoodJustice/Donor_Info/Filter_Form_Sponsor_Assignment.xlsx' uploaded to S3 bucket 'bayparkbucket' successfully.



```python
# Upload the second Excel file
upload_to_s3(bucket_name, excel_file2, s3_folder_path + os.path.basename(excel_file2))
```

    File 'GoodJustice/Donor_Info/Home_Form_Sponsor_Assignment.xlsx' uploaded to S3 bucket 'bayparkbucket' successfully.

