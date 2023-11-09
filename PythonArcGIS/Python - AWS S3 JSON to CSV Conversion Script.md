# AWS S3 JSON to CSV Conversion Script

This script is designed to automate the process of extracting JSON data from multiple files in an S3 bucket, combine them into a single DataFrame, and then output the combined data to a CSV file, thereby facilitating easier data analysis and manipulation.

This script performs the following functions:

1. **Secure Credential Management**: It securely retrieves AWS S3 access keys from environment variables to ensure the security of AWS credentials.

2. **S3 Resource Initialization**: It initializes an S3 resource client using `boto3` which is configured with the provided AWS credentials and region information. 

3. **JSON Content Retrieval**: The script defines a function `get_json_content`, which attempts to read and decode JSON data from a specified S3 object (file within a bucket). If an error occurs, it will catch the exception and print an error message.

4. **Data Processing Workflow**:
   - It first fetches the content of the initial page (`Hospice_Testing_GetAll_page_1.txt`) to determine the total number of pages (`totalPages`) available to process.
   - If it successfully fetches the first page, it initializes an empty pandas DataFrame to combine data from all pages.
   - It then enters a loop to process each page, from the first page to the last (`totalPages`), fetching and decoding the JSON content of each.
   - For each page, it converts the JSON payload to a pandas DataFrame and concatenates it to the `combined_df` DataFrame.

5. **CSV Export**:
   - After processing all pages and combining the data, the script checks if the `combined_df` DataFrame contains any data.
   - If it does, it exports the DataFrame to a CSV file named `Hospice_Testing_All_Data.csv` and informs the user of successful exportation.
   - If there is no data to export, it prints a message stating so.

6. **Error Handling**: If the first page's content cannot be retrieved, it prints a message indicating the failure to proceed with the processing.

```python
import boto3
import pandas as pd
import json
import os

# AWS S3 credentials should be managed securely, e.g., using environment variables
# It is assumed that AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are set as environment variables
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
region_name = 'us-west-1'

bucket_name = "bayparkbucket"
file_path_template = "MCH_Data/Hospice/Hospice_Testing_GetAll_page_{}.txt"

# Initialize the boto3 S3 resource
s3_client = boto3.resource(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

def get_json_content(bucket, file_path):
    try:
        content_object = s3_client.Object(bucket, file_path)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        return json.loads(file_content)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Fetch the first page to figure out how many pages there are
first_page_content = get_json_content(bucket_name, file_path_template.format(1))
if first_page_content:
    total_pages = first_page_content['pagination']['totalPages']
    print(f"There are a total of {total_pages} pages to process.")

    # Initialize an empty DataFrame to hold all combined data
    combined_df = pd.DataFrame()

    # Loop through all pages and fetch the content
    for i in range(1, total_pages + 1):
        print(f"Processing page {i}...")
        page_content = get_json_content(bucket_name, file_path_template.format(i))
        if page_content:
            new_df = pd.DataFrame(page_content['payload'])
            combined_df = pd.concat([combined_df, new_df], ignore_index=True)

    # Export to CSV if there is any data
    if not combined_df.empty:
        combined_df.to_csv('Hospice_Testing_All_Data.csv', index=False)
        print('Successfully exported to CSV file.')
    else:
        print('No data to export.')
else:
    print("Could not retrieve the first page content.")
```
