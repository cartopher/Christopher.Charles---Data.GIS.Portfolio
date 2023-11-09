# Paginated JSON Data Aggregator

This script is useful for aggregating JSON data from multiple paginated sources into a single CSV file, especially when dealing with large datasets split across multiple pages on a web server. The improved version with error handling, dynamic fetching, and checks for data integrity makes it robust for practical use in data processing workflows.

The code performs the following tasks:

1. **Data Aggregation**: It initializes an empty DataFrame (`combined_df`) to hold data from multiple JSON payloads.

2. **Data Retrieval and Conversion**:
   - Defines a `fetch_data` function that takes a `page_number` as an argument, constructs a URL for the JSON data located on an S3 bucket, and attempts to fetch the data.
   - The JSON response is checked for successful retrieval (`response.raise_for_status()`), and if successful, it is converted into a pandas DataFrame.
   - If any HTTP errors or general exceptions occur during the request, they are caught, and `None` is returned, indicating a failure to retrieve data.

3. **Iterative Data Fetching**:
   - Starts a loop from `page_number = 1` and incrementally fetches data by calling the `fetch_data` function. 
   - After each successful fetch, the data is appended to the `combined_df` DataFrame.
   - The loop continues until `fetch_data` returns `None` or an empty DataFrame, which signifies that there is no more data to fetch or an error has occurred.

4. **Data Persistence**:
   - Once all pages have been fetched and combined into `combined_df`, it checks whether the DataFrame is empty.
   - If it's not empty, the DataFrame is saved to a CSV file named `OutPatient_update_march.csv` in the specified `data_directory`. The CSV file is saved without the DataFrame index (`index=False`).
   - It prints the path to the saved CSV file or a message stating that no CSV file was created if the DataFrame is empty.

```python
from arcgis.gis import GIS
import pandas as pd
import requests
import os

# Establish a connection to GIS
gis = GIS("home")

# Initialize an empty DataFrame for all data
combined_df = pd.DataFrame()

# Base URL for the JSON data
base_url = 'https://bayparkbucket.s3.us-west-1.amazonaws.com/MCH_Data/CancerCenters/OutPatient_update_page{}.txt'

# Specify the directory to save the CSV file
data_directory = "/arcgis/home/"
filename = 'OutPatient_update_march.csv'

# Function to fetch and return data as a DataFrame
def fetch_data(page_number):
    try:
        # Construct the full URL for the current page
        url = base_url.format(page_number)
        response = requests.get(url)
        # Check if the response was successful
        response.raise_for_status()
        # Convert JSON payload into a DataFrame
        return pd.DataFrame(response.json()['payload'])
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Python 3.6
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

# Start from page 1 and try to fetch data until an empty DataFrame is returned
page_number = 1
while True:
    print(f"Fetching data for page {page_number}...")
    new_df = fetch_data(page_number)
    # If no data is returned or an empty DataFrame, stop the loop
    if new_df is None or new_df.empty:
        print("No more data to fetch.")
        break
    # Concatenate the new data
    combined_df = pd.concat([combined_df, new_df], ignore_index=True)
    page_number += 1

# Check if the DataFrame is not empty before saving
if not combined_df.empty:
    # Save the combined DataFrame to a CSV file
    csv_file_path = os.path.join(data_directory, filename)
    combined_df.to_csv(csv_file_path, index=False)
    print(f'CSV file saved at {csv_file_path}')
else:
    print("The DataFrame is empty. No CSV file was created.")
```
