import matplotlib.pyplot as plt
import numpy as np

# Define points for different lines
diagonal_up_x = np.array([0, 10])
diagonal_up_y = np.array([0, 10])

diagonal_down_x = np.array([0, 10])
diagonal_down_y = np.array([10, 0])

vertical_x = np.array([0, 10])
vertical_y = np.array([5, 5])

horizontal_x = np.array([5, 5])
horizontal_y = np.array([0, 10])

# Plot the lines
plt.plot(diagonal_up_x, diagonal_up_y)
plt.plot(diagonal_down_x, diagonal_down_y)
plt.plot(vertical_x, vertical_y)
plt.plot(horizontal_x, horizontal_x)

# Display the plot
plt.show()