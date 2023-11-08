# **Creating Data Tables using Seaborn HeatMaps**
Create automated data tables using seaborn heatmaps. This is useful for generating consistent reports with a standard format that stakeholders can easily interpret.

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
![Soil Data Table](https://github.com/cartopher/Christopher.Charles---Data.GIS.Portfolio/blob/1a0a240a84774b9a2ce72106d737ad9acfb3d47d/output/images/SoilDataTable.png?raw=true "Soil Data Table Example")


### **Conclusion**
This process efficiently creates a series of data tables in a visual heatmap format, suitable for periodic environmental data reporting. This visual format makes it easier to spot trends and outliers in the dataset across different variables and time points.
