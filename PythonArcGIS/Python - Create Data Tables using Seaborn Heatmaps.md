# **Creating Data Tables using Seaborn Heat Maps**

The script is designed to produce a visual representation, specifically a heatmap in standard table form, of soil health data collected from the Bamberger Wildlife Preserve. The table is saved as a PDF document. Key steps in the process include:

1. **Environment Setup:**
   - Imports necessary libraries for file operations, data manipulation, visualization, and PDF output.
   - Checks if a specified directory (`transects_dir`) exists for storing output and creates it if it does not.

2. **Data Preparation:**
   - Sets the file paths for input CSV data and output PDF.
   - Attempts to load a CSV file containing soil data into a pandas DataFrame. If an error occurs during loading, it is printed out and the error is raised, potentially stopping the script.

3. **Visualization Configuration:**
   - Defines the dimensions and resolution for the figure to be created.
   - Sets up custom labels for the x-axis (dates of tests) and y-axis (different soil health indicators).
   - Specifies a dictionary for replacing certain text values in the heatmap, likely to improve readability or cater to specific visualization requirements.

4. **Plotting:**
   - Initiates a PDF file using `PdfPages` which will store the resulting heatmap.
   - Creates a matplotlib figure with the predefined dimensions and resolution.
   - Generates a heatmap from the DataFrame using seaborn's `heatmap` function, with several aesthetic parameters such as the colormap, line widths, annotation settings, etc.
   - Replaces text in the heatmap annotations based on the earlier defined dictionary.

5. **Customization and Saving:**
   - Customizes the plot with titles, axis labels, font sizes, and styles.
   - Adjusts grid lines to enhance the visual appeal, matching the shape and dimensions of the heatmap.
   - Saves the generated heatmap into the PDF file while ensuring the layout is tight (without unnecessary white space).
   - Closes the plot to free up resources.

This automated visualization script helps in efficiently analyzing and reporting soil condition trends and changes over time, providing a clear and accessible way to present complex data.

```python
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages

# Create the directory if it doesn't exist
transects_dir = "/arcgis/home/transects"
if not os.path.exists(transects_dir):
    os.makedirs(transects_dir)

# Define file paths
csv_file = os.path.join(transects_dir, 'bamberger_wildlifepreserve.csv')
output_pdf = os.path.join(transects_dir, 'Bamberger-Wildlife Preserve Soil Results.pdf')

# Load the dataset
try:
    df = pd.read_csv(csv_file, index_col=0)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    # Handle the exception or exit if the file is crucial for further operations
    raise

# Define plot parameters
fig_width, fig_height, fig_dpi = 30, 40, 100
x_axis_labels = ['Nov-2017', 'May-2019', 'Oct-2021']
y_axis_labels = [
    'Soil pH', 'Soil Organic Matter', 'Soil Respiration', 'Water Extractable Organic Carbon', 'Water Extractable Organic Nitrogen',
    'Microbially Active Carbon', 'Organic C to Organic N Ratio', 'Organic N to Inorganic N Ratio', 'Organic Nitrogen Release',
    'Organic Nitrogen Reserve', 'Organic Phosphorus', 'Organic Phosphorus Release', 'Organic Phosphorus Reserve', 'Soil Health Score',
    'Total Living Biomass', 'Fung: Bacteria', 'Protozoa Bacterial', 'Microaggregate', 'Macroaggregates',
    'β-glucosidase enzyme - carbon enzyme', 'Permanganate Oxidizable Carbon - labile carbon', 'Water Holding Capacity, inch H2O inch soil¯¹'
]

# Define a dictionary for custom text replacements
text_replacements = {
    '0': '',  # Assuming you want to hide zeros
    '1': 'All Prey',
    '2': 'All Bact',
    '0.1': 'n/a'
}

# Start plotting and saving the heatmap
with PdfPages(output_pdf) as pdf:
    plt.figure(figsize=(fig_width, fig_height), dpi=fig_dpi)

    # Create the heatmap
    heatmap = sns.heatmap(
        df,
        cbar=False,
        xticklabels=x_axis_labels,
        yticklabels=y_axis_labels,
        annot=True,
        fmt="g",
        cmap=ListedColormap(['ivory']),
        linewidths=6,
        linecolor='0.8',
        square=False,
        center=0,
        annot_kws={"size": 45, "color": 'black'}
    )

    # Apply text replacements
    for text in heatmap.texts:
        text.set_text(text_replacements.get(text.get_text(), text.get_text()))

    # Set title and axis labels with custom settings
    plt.title('Wildlife Preserve\n', loc='center', fontsize=80, fontweight="bold")
    plt.title('Transect Soil Health Results', loc='left', fontsize=65, fontweight="bold")
    plt.xlabel('\nTest Dates', fontsize=75, fontweight="bold")
    plt.ylabel('Bamberger\nAnalytes', fontsize=75, fontweight="bold")
    plt.xticks(rotation=0, fontsize=65)
    plt.yticks(fontsize=45, style='italic')

    # Customize the grid lines
    heatmap.axhline(y=0, color='darkblue', linewidth=10)
    heatmap.axhline(y=df.shape[0], color='darkblue', linewidth=10)  # Adjusted to dataset size
    heatmap.axvline(x=df.shape[1], color='darkblue', linewidth=10)
    heatmap.axvline(x=0, color='darkblue', linewidth=10)

    # Save and close the plot
    pdf.savefig(bbox_inches='tight')
    plt.close()

```
![Soil Data Table](https://github.com/cartopher/Christopher.J.Charles...Portfolio/blob/main/Projects/Past%20Works/Output/Images/SoilDataTable.png?r "Soil Data Table Example")
