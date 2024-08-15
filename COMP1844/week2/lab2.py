import numpy as np

# Define number of elements
NumberOfElements = 50

# Allocate memory
MyArray1 = np.empty(shape=NumberOfElements, dtype=int)

# Initialise an array with 10 random (pseudo-random) integer values
# The values will be within the interval [-5..5]
MyArray2 = np.random.randint(-5, 6, 10, dtype=int)

# Visualize elements alongside their indices using a FOR loop
print("Visualizing elements using FOR loop:")
for i in range(10):
    print(i, MyArray2[i])

# Visualize elements alongside their indices using a WHILE loop
print("\nVisualizing elements using WHILE loop:")
i = 0
while i < 10:
    print(i, MyArray2[i])
    i += 1