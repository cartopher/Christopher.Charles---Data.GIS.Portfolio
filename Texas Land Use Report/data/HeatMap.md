# Python Script for Data Visualization and Analysis on Historical Precipitation Data

## Main Objective

The main objective of this Python script is to perform data visualization and analysis on historical precipitation data. Specifically, the script:

1. Imports necessary Python modules for data manipulation and visualization.
2. Loads a CSV file containing historical precipitation data into a Pandas DataFrame.
3. Cleans the DataFrame by filling missing values.
4. Selects a subset of variables for further analysis.
5. Groups the data by the “Year” column and calculates mean values.
6. Generates a heatmap using seaborn to visualize these annual average precipitation values.
7. Exports the heatmap to a PDF file for easy sharing and reporting.

The script aims to provide insights into weather patterns over time, with a focus on precipitation.

---

## Importing Libraries

Place all import statements at the top of the file, one per line.

```python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
import numpy as np

