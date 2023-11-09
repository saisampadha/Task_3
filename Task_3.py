import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your given dataset
df = pd.read_csv("D:/data/Task_3.csv")

# Create a histogram for given dataset
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Species', bins=20, kde=True)  # Replace 'Numeric_Column' with your numerical column
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Numeric Data Distribution for given dataset:')
plt.grid(True)

# Create a bar chart for the given dataset
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Species')  # Replace 'Species' with your categorical column
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Bar Chart of Categorical Data Distribution')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility if needed


# Show the bar chart for the given data
plt.tight_layout()
# Show the histogram for the given data
plt.show()