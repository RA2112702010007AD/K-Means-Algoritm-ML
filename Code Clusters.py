import numpy as np

# Define the number of clusters
k = 4

# Define the 15 data points
data = np.array([(1, 1), (1, 2), (2, 1), (2, 3), (3, 2), (3, 3), (4, 2), (5, 3), (6, 3), (7, 2), (7, 3), (8, 2), (8, 4), (9, 3), (9, 4)])

# Initialize the centroids randomly
centroids = data[np.random.choice(data.shape[0], k, replace=False)]

# Initialize old_centroids
old_centroids = np.zeros_like(centroids)

# Repeat until convergence or a maximum number of iterations is reached
for i in range(100):
    # Assign each point to the closest centroid
    distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))
    labels = np.argmin(distances, axis=0)

    # Update the centroids
    for j in range(k):
        centroids[j] = data[labels == j].mean(axis=0)

    # Check for convergence
    if np.allclose(centroids, old_centroids):
        break

    old_centroids = centroids.copy()

# Print the resulting clusters
for j in range(k):
    print(f"Cluster {j+1}: {data[labels == j]}")
