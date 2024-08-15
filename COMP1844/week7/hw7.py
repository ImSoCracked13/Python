import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from pandas.plotting import parallel_coordinates

# Load the Iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

# Convert target to species names
df['target'] = df['target'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

# Plot parallel coordinates
plt.figure(figsize=(10, 8))
parallel_coordinates(df, 'target', color=['r', 'g', 'b'], alpha=0.5)
plt.title('IRIS Flower description and categories')
plt.xlabel('IRIS Features')
plt.ylabel('Feature Values')
plt.grid(True)

# Customizing the plot to match the provided image
max_values = df.max()
for i, feature in enumerate(iris['feature_names']):
    plt.vlines(i, 0, max_values[feature], color='black', linestyle='dotted')

plt.xticks(range(len(iris['feature_names'])), iris['feature_names'], fontsize=10)
plt.yticks(fontsize=10)

# Label positions
plt.text(3.5, max_values['sepal length (cm)'], s='7.9', ha='center', fontsize=10)
plt.text(3.5, max_values['sepal width (cm)'], s='4.4', ha='center', fontsize=10)
plt.text(3.5, max_values['petal length (cm)'], s='6.9', ha='center', fontsize=10)
plt.text(3.5, max_values['petal width (cm)'], s='2.5', ha='center', fontsize=10)

# Specifying species names at the end
plt.text(len(iris['feature_names']) + 0.1, max_values['sepal length (cm)'], s='Setosa', ha='left', color='r')
plt.text(len(iris['feature_names']) + 0.1, max_values['sepal width (cm)'], s='Versicolor', ha='left', color='g')
plt.text(len(iris['feature_names']) + 0.1, max_values['petal length (cm)'], s='Virginica', ha='left', color='b')

plt.show()