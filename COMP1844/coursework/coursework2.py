import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# Task 2:
# Initialize the graph and define initial stations and positions
G = nx.Graph()
positions = {
    "Hyde Park Corner": (0.5, 1),
    "Green Park": (1.75, 2),
    "Piccadilly Circus": (3, 2), # Connected 1
    "Leicester Square": (4, 2), # Connected 1
    "Covent Garden": (5, 3),
    "Holborn": (6, 4), # Connected 1
    "Bond Street": (1.5, 4),
    "Oxford Circus": (2.5, 4), # Connected 1
    "Tottenham Court Road": (4, 4), # Connected 1
    "Chancery Lane": (6.75, 4), 
    "St. Paul": (8.5, 3.25),
    "Marylebone": (0.5, 7),
    "Baker Street": (1.25, 6),
    "Regent's Park": (2, 5),
    "Charing Cross": (4, 0.25), # Connected 1
    "Euston": (4.75, 8.25),
    "Warren Street": (4, 6.75),
    "Goodge Street": (4, 5)
}

# Function to add line with specified distances
def add_line(G, distances, line_name):
    for u, v, dist in distances:
        G.add_edge(u, v, distance=dist, line=line_name)

# Add Piccadilly line edges
piccadilly_distances = [
    ("Hyde Park Corner", "Green Park", 0.88),
    ("Green Park", "Piccadilly Circus", 0.66),
    ("Piccadilly Circus", "Leicester Square", 0.29),
    ("Leicester Square", "Covent Garden", 0.44),
    ("Covent Garden", "Holborn", 0.71)
]
add_line(G, piccadilly_distances, "Piccadilly")

# Add Central line edges
central_distances = [
    ("Bond Street", "Oxford Circus", 0.57),
    ("Oxford Circus", "Tottenham Court Road", 0.59),
    ("Tottenham Court Road", "Holborn", 0.89),
    ("Holborn", "Chancery Lane", 0.58),
    ("Chancery Lane", "St. Paul", 1.07)
]
add_line(G, central_distances, "Central")

# Add Northern line edges
northern_distances = [
    ("Euston", "Warren Street", 0.62),
    ("Warren Street", "Goodge Street", 0.52),
    ("Goodge Street", "Tottenham Court Road", 0.57),
    ("Tottenham Court Road", "Leicester Square", 0.55),
    ("Leicester Square", "Charing Cross", 0.44)
]
add_line(G, northern_distances, "Northern")

# Add Bakerloo line edges
bakerloo_distances = [
    ("Marylebone", "Baker Street", 0.48),
    ("Baker Street", "Regent's Park", 0.71),
    ("Regent's Park", "Oxford Circus", 0.84),
    ("Oxford Circus", "Piccadilly Circus", 0.82),
    ("Piccadilly Circus", "Charing Cross", 0.85)
]
add_line(G, bakerloo_distances, "Bakerloo")

# Set edge colors based on lines
line_colors = {
    "Piccadilly": "blue",
    "Central": "red",
    "Northern": "black",
    "Bakerloo": "brown"
}
line_edges = {
    "Piccadilly": piccadilly_distances,
    "Central": central_distances,
    "Northern": northern_distances,
    "Bakerloo": bakerloo_distances
}

# Assign node colors based on the line they belong to
node_colors = {}
for line, edges in line_edges.items():
    color = line_colors[line]
    for u, v, _ in edges:
        node_colors[u] = color
        node_colors[v] = color

# Plot the graph
plt.figure(figsize=(12, 8))
nx.draw(G, pos=positions, with_labels=True, node_size=500, node_color=[node_colors[node] for node in G.nodes()], 
        font_size=10, font_color='grey', font_weight='bold')

# Draw edges with respective colors
for line, edges in line_edges.items():
    nx.draw_networkx_edges(G, pos=positions, edgelist=edges, edge_color=line_colors[line], width=2)

# Add edge labels
edge_labels = {(u, v): f"{d['distance']:.2f} km" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edge_labels, font_color='black')

# Draw the key with black text
for i, (line, color) in enumerate(line_colors.items()):
    plt.text(8, 2.5 - 0.2 * i, f"{line} Line", fontsize=12, bbox=dict(facecolor=color, alpha=0.5), color='black')

plt.title('Transport Network Map')
plt.show()


# Task 3: 
# Calculate and print the required metrics using pandas
data = [(u, v, d['distance']) for u, v, d in G.edges(data=True)]
df = pd.DataFrame(data, columns=['Station 1', 'Station 2', 'Distance'])

total_length = df['Distance'].sum()
average_distance = df['Distance'].mean()
std_dev_distance = df['Distance'].std()

print(f"Total length: {total_length:.2f} km")
print(f"Average distance: {average_distance:.2f} km")
print(f"Standard deviation: {std_dev_distance:.2f} km")
