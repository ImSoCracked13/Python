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

# Summary statistics calculations
summary_statistics = data_cleaned.describe()

# Mean population by year
mean_population = data_cleaned.mean(numeric_only=True)

# Median population by year
median_population = data_cleaned.median(numeric_only=True)

# Mode population by year (mode can be multiple values, handle accordingly)
mode_population = data_cleaned.mode().iloc[0]

# Standard deviation population by year
std_population = data_cleaned.std(numeric_only=True)

# Visualizations

# Population trends over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=data_cleaned.loc[:, '1960.0':'2023.0'].mean(), marker='o')
plt.title('Average Population Trends (1960-2023)')
plt.xlabel('Year')
plt.ylabel('Average Population')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
avg_p_trends = os.path.join(__location__, 'average_population_trends.png')
plt.savefig(avg_p_trends)
plt.show()

# Distribution of population for the year 2023
plt.figure(figsize=(12, 6))
sns.histplot(data_cleaned['2023.0'], kde=True)
plt.title('Population Distribution in 2023')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
p_distr = os.path.join(__location__, 'population_distribution_2023.png')
plt.savefig(p_distr)
plt.show()


