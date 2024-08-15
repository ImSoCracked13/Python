import pandas as pd
import os

file_path = 'World_Population_CountryWise_RAW.csv'
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = os.path.join(__location__, file_path)

if os.path.exists(f):
    data = pd.read_csv(f)

# Preprocess the dataset
data_cleaned = data.iloc[3:].reset_index(drop=True)
data_cleaned.columns = data_cleaned.iloc[0]
data_cleaned = data_cleaned.drop(0).reset_index(drop=True)

# Convert columns to appropriate data types
data_cleaned.columns = [str(col) for col in data_cleaned.columns]
for col in data_cleaned.columns[4:]:
    data_cleaned[col] = pd.to_numeric(data_cleaned[col], errors='coerce')
data_cleaned.fillna(0, inplace=True)

# Calculate summary statistics
mean_population = data_cleaned.mean(numeric_only=True)
median_population = data_cleaned.median(numeric_only=True)
mode_population = data_cleaned.mode().iloc[0]
std_population = data_cleaned.std(numeric_only=True)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.lineplot(data=data_cleaned.loc[:, '1960.0':'2023.0'].mean(), marker='o')
plt.title('Average Population Trends (1960-2023)')
plt.xlabel('Year')
plt.ylabel('Average Population')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(__location__, 'average_population_trends.png'))
plt.show()

years = mean_population.index.astype(float)

plt.figure(figsize=(14, 7))
plt.plot(years, mean_population, label='Mean', marker='o')
plt.plot(years, median_population, label='Median', marker='o')
plt.plot(years, mode_population[4:], label='Mode', marker='o')
plt.plot(years, std_population, label='Standard Deviation', marker='o')

plt.title('Population Trends (1960-2023)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(__location__, 'population_trends.png'))
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(data_cleaned['2023.0'], kde=True)
plt.title('Population Distribution in 2023')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(__location__, 'population_distribution_2023.png'))
plt.show()

# Save the preprocessed dataset
f = os.path.join(__location__, 'World_Population_CountryWise_Processed.csv')
data_cleaned.to_csv(f, index=False)