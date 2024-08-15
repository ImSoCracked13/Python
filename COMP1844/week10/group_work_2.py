import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the CSV file
file_path = 'World_Population_CountryWise_RAW.csv'
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
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

# Handle missing values (if any)
data_cleaned.fillna(0, inplace=True)

# Calculate summary statistics
mean_population = data_cleaned.mean(numeric_only=True)
median_population = data_cleaned.median(numeric_only=True)
mode_population = data_cleaned.mode().iloc[0]
std_population = data_cleaned.std(numeric_only=True)

# Display the summary statistics in the console
print("Summary Statistics:")
print(data_cleaned.describe())

print("\nMean Population by Year:")
print(mean_population)

print("\nMedian Population by Year:")
print(median_population)

print("\nMode Population by Year:")
print(mode_population)

print("\nStandard Deviation Population by Year:")
print(std_population)

# Plotting population trends over the years
years = mean_population.index.astype(float)

plt.figure(figsize=(14, 7))
plt.plot(years, mean_population, label='Mean', marker='o')
plt.plot(years, median_population, label='Median', marker='o')
plt.plot(years, mode_population[4:], label='Mode', marker='o')  # Skip first four non-year columns
plt.plot(years, std_population, label='Standard Deviation', marker='o')

plt.title('Population Trends (1960-2023)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.tight_layout()
p_trends = os.path.join(__location__, 'population_trends.png')
plt.savefig(p_trends)
plt.show()

# Plotting distribution of population for the year 2023
plt.figure(figsize=(12, 6))
sns.histplot(data_cleaned['2023.0'], kde=True)
plt.title('Population Distribution in 2023')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
p_distr = os.path.join(__location__, 'population_distribution_2023_2.png')
plt.savefig(p_distr)
plt.show()

# Save the preprocessed dataset
f = os.path.join(__location__, 'World_Population_CountryWise_Processed.csv')
data_cleaned.to_csv(f, index=False)
