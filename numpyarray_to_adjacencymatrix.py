import numpy as np

def slow_adjacency_matrix(grid):
    """
    Generates an adjacency matrix for a 2D grid where each cell is connected to its neighboring cells.

    Parameters:
    - grid (numpy.ndarray): 2D array representing the grid.

    Returns:
    - numpy.ndarray: Adjacency matrix representing the connections between cells.
    """

    # Get the dimensions of the grid
    N, M = grid.shape

    # Initialize an empty adjacency matrix
    adj = np.zeros((N * M, N * M))

    # Iterate through each cell in the grid
    for i in range(N):
        for j in range(M):
            # Convert 2D indices to a flattened index
            k = np.ravel_multi_index((i, j), (N, M))

            # Check and connect with the cell above
            if i > 0:
                ii, jj = i - 1, j
                adj[k, np.ravel_multi_index((ii, jj), (N, M))] = 1

            # Check and connect with the cell below
            if i < N - 1:
                ii, jj = i + 1, j
                adj[k, np.ravel_multi_index((ii, jj), (N, M))] = 1

            # Check and connect with the cell to the left
            if j > 0:
                ii, jj = i, j - 1
                adj[k, np.ravel_multi_index((ii, jj), (N, M))] = 1

            # Check and connect with the cell to the right
            if j < M - 1:
                ii, jj = i, j + 1
                adj[k, np.ravel_multi_index((ii, jj), (N, M))] = 1

    return adj
