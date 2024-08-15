import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate the dataset
data = np.random.normal(8, 0.75, 2000)

# Convert data to a DataFrame
df = pd.DataFrame(data, columns=['Value'])

# Compute statistics
min_val = df['Value'].min()
max_val = df['Value'].max()
range_val = max_val - min_val
mode_val = df['Value'].mode()[0]
std_dev_val = df['Value'].std()
variance_val = df['Value'].var()

print(f"MIN: {min_val}")
print(f"MAX: {max_val}")
print(f"RANGE: {range_val}")
print(f"MODE: {mode_val}")
print(f"Standard Deviation: {std_dev_val}")
print(f"Variance: {variance_val}")

# Summary of the dataset
summary = df.describe()
print(summary)

# Histogram and KDE using Matplotlib
plt.figure(figsize=(10, 6))
df['Value'].plot(kind='hist', bins=30, density=True, alpha=0.6, color='blue', edgecolor='black', label='Histogram')
df['Value'].plot(kind='kde', color='red', label='KDE')
plt.title('Histogram and KDE of Generated Data')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()

# Probability Density Function (PDF)
x = np.linspace(min_val, max_val, 1000)
pdf = (1 / (0.75 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 8) / 0.75) ** 2)

plt.figure(figsize=(10, 6))
plt.plot(x, pdf, label='PDF', color='red')
df['Value'].plot(kind='hist', bins=30, density=True, alpha=0.6, color='blue', edgecolor='black')
plt.title('Probability Density Function and Histogram')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()  