# Automated User Management and CSV Update for ArcGIS Hub

### Description

This Python notebook automates the process of adding new members to a specific group in ArcGIS Hub from a list provided in a CSV file hosted on AWS S3. After successfully adding each member, the script clears the data from the CSV, preserving only the column headers. The notebook handles authentication with ArcGIS, reads and writes to an S3 bucket, and maintains accurate user management within the ArcGIS platform. The process includes robust error handling to ensure each step is completed successfully before proceeding to the next, ensuring the integrity of user data and the reliability of the group management process.


```python
import boto3
import pandas as pd
from arcgis.gis import GIS
from io import StringIO
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
# Bucket and file path details
bucket_name = 'YOUR_AWS_BUCKET_NAME'
file_key = 'YOUR_S3_FILE_KEY/'  # Correct key based on your provided full path
```


```python
# Function to read CSV from S3
def read_csv_from_s3(bucket_name, file_key):
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    data = response['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(data))
    return df
```


```python
# Authenticate with ArcGIS Online using specific credentials
gis = GIS("https://www.arcgis.com", "USERNAME", "PASSWORD")
```


```python
# Function to add user and assign to a group
def add_user_to_group(user_details, group_id):
    try:
        user = gis.users.create(
            username=user_details['username'],
            password=user_details['password'],
            firstname=user_details['firstname'],
            lastname=user_details['lastname'],
            email=user_details['email'],
            user_type=user_details['user type'],
            role=user_details['role'],
            level=user_details['credit allocation']
        )
        # Get the group and add user
        group = gis.groups.get(group_id)
        if group is not None:
            group.add_users([user.username])
            print(f"User {user.username} added to group {group.title}.")
            return True
        else:
            print("Group not found.")
            return False
    except Exception as e:
        print(f"Error processing user {user_details['username']}: {e}")
        return False
```


```python
# Function to clear the CSV data in S3 while preserving headers
def clear_csv_data_on_s3(bucket_name, file_key):
    # Fetch the current CSV to retain the headers
    df = read_csv_from_s3(bucket_name, file_key)
    # Create a new empty DataFrame with the same columns
    empty_df = pd.DataFrame(columns=df.columns)
    # Convert the empty DataFrame to CSV format, excluding the row index
    csv_buffer = StringIO()
    empty_df.to_csv(csv_buffer, index=False)
    # Upload the empty CSV with headers to S3
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=csv_buffer.getvalue())
    print("CSV data cleared, headers preserved.")
```


```python
# Process the users from CSV
def process_users():
    df = read_csv_from_s3(bucket_name, file_key)
    group_id = 'bbfe2d6d05a944d8acbad023405fa5ac'  # Network group ID
    success = True

    for index, row in df.iterrows():
        if not add_user_to_group(row, group_id):
            success = False

    if success:
        clear_csv_data_on_s3(bucket_name, file_key)
        # Re-read the CSV to show it's empty with headers
        empty_df = read_csv_from_s3(bucket_name, file_key)
        print("CSV content after clearing:")
        print(empty_df)

# Call the process
process_users()
```
