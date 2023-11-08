# Annual Precipitation Heatmap Generator
# This script loads precipitation data, processes it, and generates a heatmap visual saved as a PDF.

```python
# Import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# Define constants
DATA_FILE = "/arcgis/home/bamberger_precip.csv"
OUTPUT_PDF = "Bamberger Precipitation Heatmap.pdf"

# Function to load and prepare data
def load_and_prepare_data(file_path):
    """
    Load precipitation data from a CSV file and backfill missing values.
    
    Parameters:
        file_path (str): The path to the CSV data file.
        
    Returns:
        DataFrame: The processed Pandas DataFrame with backfilled data.
    """
    df = pd.read_csv(file_path)
    df.fillna(method="bfill", inplace=True)
    return df

# Function to create a heatmap and save it as a PDF
def create_heatmap(data, output_file):
    """
    Create a heatmap from the data and save it to a PDF file.
    
    Parameters:
        data (DataFrame): The prepared data for the heatmap.
        output_file (str): The file path for the output PDF.
    """
    with PdfPages(output_file) as pdf:
        plt.figure(figsize=(14, 10))
        cmap = sns.diverging_palette(20, 145, sep=77, as_cmap=True)
        heatmap = sns.heatmap(data.T, cmap=cmap, linecolor='0.8', linewidth=0.1, annot=True,
                              cbar_kws={'shrink': 0.8, 'label': 'Precipitation (mm)'})
        heatmap.set_title('Bamberger Average Annual Precipitation in Millimeters',
                          loc='center', fontsize=26, fontweight="bold")
        heatmap.set_xlabel('Period: 2011 - 2021', fontsize=16)
        heatmap.set_ylabel('Monthly Averages', fontsize=16)
        heatmap.annotate('Precipitation Report (10-Years)\nBamberger: 30.2060, -98.4494\n'
                         '2341 Blue Ridge Dr Johnson City, TX 78636',
                         xy=(0.5, -0.05), xycoords='axes fraction', ha='center', va='top', fontsize=9, color='#636363')
        heatmap.annotate('Creation Date: 07 Jul. 2022\nData Source: https://power.larc.nasa.gov/data-access-viewer/',
                         xy=(0.5, -0.1), xycoords='axes fraction', ha='center', va='top', fontsize=9, color='#636363')
        pdf.savefig(bbox_inches="tight")
        plt.close()

# Main execution
if __name__ == "__main__":
    # Load and prepare data
    precipitation_data = load_and_prepare_data(DATA_FILE)

    # Create a subset of the data with selected variables (if needed)
    selected_columns = ["Year", "Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", 
                        "Jul.", "Aug.", "Sept.", "Oct.", "Nov.", "Dec.", "Annual Avg."]
    monthly_data = precipitation_data[selected_columns]

    # Group the data by 'Year' and calculate mean values
    grouped_data = monthly_data.groupby("Year").mean().round(2)

    # Create and save heatmap
    create_heatmap(grouped_data, OUTPUT_PDF)
```
