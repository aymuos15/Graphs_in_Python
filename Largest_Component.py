# Define a function to find the size of the largest component in an undirected graph.
def largest_component(graph):
    # Create a set to keep track of visited nodes.
    visited = set()
    # Initialize a variable to store the size of the largest component.
    longest = 0

    # Iterate through each node in the graph.
    for node in graph:
        # Call the exploreSize function to calculate the size of the connected component
        # starting from the current node.
        size = exploreSize(graph, node, visited)
        # Update the size of the largest component if the current component is larger.
        if size > longest:
            longest = size

    # Return the size of the largest connected component.
    return longest

# Define a recursive function to explore and calculate the size of a connected component.
def exploreSize(graph, node, visited):
    # Check if the current node has been visited before.
    if node in visited:
        return 0
    # Mark the current node as visited.
    visited.add(node)

    # Initialize the size of the component to 1, as the current node is part of it.
    size = 1
    # Recursively explore each neighbor of the current node and add their sizes to the size variable.
    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)

    # Return the total size of the connected component starting from the initial node.
    return size

# Define the graph as a dictionary where each node is associated with its neighboring nodes.
graph = {0: [8, 1, 5],
         1: [0],
         5: [0, 8],
         8: [0, 5],
         2: [3, 4],
         3: [2, 4],
         4: [3, 2]
         }

# Call the largest_component function on the graph to find the size of the largest component.
result = largest_component(graph)
# Print the size of the largest component.
print("Size of the largest component:", result)
