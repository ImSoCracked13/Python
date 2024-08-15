import numpy as np

# Sample data
cities = ['Denver', 'Toronto', 'Dresden']
months = ['Jan', 'Feb', 'Mar']
temperatures = [
    [10, 15, 20],
    [12, 18, 22],
    [8, 13, 17]
]

# Transpose the data
data = np.transpose([cities, months, *temperatures])

# Print the table
print("City\tMonth\tTemperature")
for row in data:
    print("\t".join(row))