import networkx as nx
import matplotlib.pyplot as plt

# Task 1:
# Create the graph
G = nx.Graph()

# Add nodes with positions
positions = {
    "Hyde Park Corner": (0.5, 1),
    "Green Park": (1.75, 2),
    "Piccadilly Circus": (3, 2),
    "Leicester Square": (4, 2),
    "Covent Garden": (5, 3),
    "Holborn": (6, 4)
}

# Add edges with distances (in kilometers)
distances = {
    ("Hyde Park Corner", "Green Park"): 0.88,
    ("Green Park", "Piccadilly Circus"): 0.66,
    ("Piccadilly Circus", "Leicester Square"): 0.29,
    ("Leicester Square", "Covent Garden"): 0.44,
    ("Covent Garden", "Holborn"): 0.71
}

for edge, distance in distances.items():
    G.add_edge(edge[0], edge[1], distance=distance)

# Draw the graph
plt.figure(figsize=(10, 5))
nx.draw(G, positions, with_labels=True, node_size=500, node_color='blue', font_size=10, font_color='grey', font_weight='bold', edge_color='blue')

# Draw edge labels
edge_labels = {(u, v): f"{d['distance']:.2f} km" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels)

plt.title('Piccadilly Line')
plt.show()
