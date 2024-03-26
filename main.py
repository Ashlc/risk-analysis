import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/credit_risk_dataset.csv")

df = df.dropna()

# Handle outliers

# Get numerical columns
num_cols = df.select_dtypes(include=[np.number]).columns

print("Before handling outliers")
print(df[num_cols].describe())

# Plotting numerical columns
for column in df[num_cols]:
    plt.figure(figsize=(8, 6))  # Set figure size for better visibility
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.xlabel(column)
    plt.ylabel("Values")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
    plt.tight_layout()  # Adjust plot to prevent clipping of labels
    plt.savefig(f"plots/{column}.png")  # Save plot to file

# Handle outliers

Q1 = df[num_cols].quantile(0.25)  # Calculate the first quartile
Q3 = df[num_cols].quantile(0.75)  # Calculate the third quartile
iqr = Q3 - Q1  # Calculate the interquartile range
upper_bound = Q3 + 1.5 * iqr  # Calculate the upper bound

# Remove outliers (numerical columns)
df[num_cols] = np.where(df[num_cols] > upper_bound, df[num_cols].median(), df[num_cols])

print("After handling outliers")
print(df[num_cols].describe())

# Plot the cleaned data

for column in df[num_cols]:
    plt.figure(figsize=(8, 6))  # Set figure size for better visibility
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}, cleaned")
    plt.xlabel(column)
    plt.ylabel("Values")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
    plt.tight_layout()  # Adjust plot to prevent clipping of labels
    plt.savefig(f"plots/{column}_cleaned.png")  # Save plot to file
