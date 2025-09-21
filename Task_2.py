import pandas as pd

# 1 Explore the dataset from PC
url = "C:\\Users\\DELL\\PythonProjects\\Week 2\\user_profiles.csv"
data = pd.read_csv(url)

# Show first 5 rows
print(data.head(5))

# Check data types and null values
print("\nData Info:")
print(data.info())

# Get summary statistics
print("\nSummary Statistics:")
print(data.describe())

# 2 Calculating basic statitics
import numpy as np

# Mean
print("\nMean:\n", data.mean(numeric_only=True))

# Median
print("\nMedian:\n", data.median(numeric_only=True))

# Mode
print("\nMode:\n", data.mode().iloc[0])

# Standard Deviation
print("\nStandard Deviation:\n", data.std(numeric_only=True))

# Calculating the Correlation between different features
print("\nCorrelation Matrix:")
print(data.corr(numeric_only=True))

import matplotlib.pyplot as plt
import seaborn as sns

# Decided to add the Heatmap of correlation
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()


