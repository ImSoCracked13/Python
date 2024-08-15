import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\PC\Desktop\Work\Studies\Coding\Python\COMP1844\winequality-red.csv'
df = pd.read_csv(file_path, delimiter=';')

# 1. Dimensions of the dataset
dimensions = df.shape
print("Dimensions of the dataset:", dimensions)

# 2. Statistical questions
std_volatile_acidity = df['volatile acidity'].std()
mean_chlorides = df['chlorides'].mean()
max_pH = df['pH'].max()
min_sulphates = df['sulphates'].min()
median_density = df['density'].median()

print("Standard deviation of volatile acidity:", std_volatile_acidity)
print("Mean of chlorides:", mean_chlorides)
print("Maximum pH:", max_pH)
print("Minimum sulphates:", min_sulphates)
print("50% (median) of density:", median_density)

# 3. Number of wines with more than 10% alcohol
high_alcohol_wines = df[df['alcohol'] > 10].shape[0]
print("Number of wines with more than 10% alcohol:", high_alcohol_wines)

# 4. Best and lowest quality wines
best_quality = df['quality'].max()
lowest_quality_count = df[df['quality'] == df['quality'].min()].shape[0]
print("Best quality of wine:", best_quality)
print("Number of wines with the lowest quality:", lowest_quality_count)

# 5. Highest density and its count
highest_density = df['density'].max()
highest_density_count = df[df['density'] == highest_density].shape[0]
print("Highest density of wine:", highest_density)
print("Number of wines with the highest density:", highest_density_count)

# 6. Wines with less than 2.5 residual sugar
low_residual_sugar_count = df[df['residual sugar'] < 2.5].shape[0]
print("Number of wines with less than 2.5 residual sugar:", low_residual_sugar_count)

# 7. Extract 'quality' column into a NumPy array and visualize
quality_array = df['quality'].to_numpy()

# Line Chart
plt.figure(figsize=(12, 6))
plt.plot(quality_array, label='Quality')
plt.title('Line Chart of Wine Quality')
plt.xlabel('Sample Index')
plt.ylabel('Quality')
plt.legend()
plt.show()

# Box Plot
plt.figure(figsize=(12, 6))
plt.boxplot(quality_array, vert=False)
plt.title('Box Plot of Wine Quality')
plt.xlabel('Quality')
plt.show()

# Bar Chart
plt.figure(figsize=(12, 6))
plt.hist(quality_array, bins=range(2, 10), edgecolor='black', align='left')
plt.title('Bar Chart of Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Frequency')
plt.show()