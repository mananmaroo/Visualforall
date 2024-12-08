#Dynamic Data Visualization Tool #

A versatile Python script that enables users to load a dataset, select columns, and create a variety of visualizations interactively. The tool supports multiple chart types and allows flexible column selection.

#📋 Project Overview

This project simplifies the process of data exploration and visualization:

Automatically adjusts for column data types.
Enables users to interactively choose the dataset and columns.
Offers a wide array of visualization options to analyze relationships and distributions effectively.

#🚀 Features

Dataset Loading:
Supports CSV files as input.
Automatically converts columns to appropriate data types (string or integer).
Interactive Column Selection:
Displays column names with indices.
Allows users to specify columns for visualization based on type constraints.

Visualization Options:


Bar Graph

Count Plot

Pie Chart

Heatmap

Scatter Plot

Line Plot

Histogram

Box Plot

Distribution Plot

Customization:


Automatically adjusts figure size.
Handles rotation of axis labels for better readability.



#🛠️ Technologies Used


Python: Programming language.

Pandas: For data manipulation and preprocessing.

Matplotlib: For static visualizations.

Seaborn: For enhanced and aesthetically pleasing visualizations.



#🧑‍💻 How to Use


Install Required Libraries:

pip install pandas matplotlib seaborn

Run the Script:

python data_visualization_tool.py

Follow the Steps:

Provide the file path to your dataset (CSV format).

Choose the columns for X and Y axes (and optional Z axis for some visualizations).

Select the type of chart you want to generate.


#🗂️ Visualization Types and Use Cases


Bar Graph:

Ideal for visualizing categorical vs. numerical relationships.


Count Plot:

Counts occurrences of categorical data.


Pie Chart:

Displays proportions for categorical data.


Heatmap:

Shows correlations between numerical variables.


Scatter Plot:

Analyzes relationships between two numerical variables.

Line Plot:
Useful for trend analysis over continuous data.

Histogram:
Displays frequency distributions.

Box Plot:
Summarizes data distribution and highlights outliers.

Distribution Plot:
Provides density estimation of numerical variables.


#📈 Sample Workflow
Input Dataset:

plaintext

Enter the file path of your dataset: data.csv

Select Columns:


plaintext

Columns in the dataset:

1] Category (string)


2] Sales (int)

3] Profit (int)

Select columns X and Y from the dataset:

Enter the index of column X (string type): 1

Enter the index of column Y (integer type): 2

Choose Visualization:

plaintext

Select the type of chart:

1] Bar Graph

2] Count Plot

Enter your choice: 1

Output:


The chosen chart is displayed interactively.



#🔄 Future Enhancements

Add support for additional file formats (e.g., Excel, JSON).

Allow customization of color palettes and chart themes.

Implement advanced visualizations like pair plots or multi-dimensional scatter plots.

Would you like further additions, such as examples of charts or troubleshooting tips?






