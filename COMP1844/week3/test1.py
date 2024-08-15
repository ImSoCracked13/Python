import numpy as np

cities = ['C1', 'C2', 'C3']
months = ['Jan', 'Feb', 'Mar']
temperatures = [
    [22, 23, 24],
    [11, 12, 13],
    [17, 18, 19]
]

print("City\tMonth\tTemperature")
for i in range(len(cities)):
    for j in range(len(months)):
        print(f"{cities[i]}\t{months[j]}\t{temperatures[i][j]}")

temperatures_transposed = np.transpose(temperatures)

print("Month\t" + "\t".join(months))
for i in range(len(cities)):
    print(f"{cities[i]}\t" + "\t".join(map(str, temperatures_transposed[i])))