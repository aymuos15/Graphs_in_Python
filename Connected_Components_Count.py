# This function is used to find the number of connected components in an undirected graph.
def Connected_Components_Count(graph):
    # Initialize an empty set to keep track of visited nodes.
    visited = set()
    # Initialize a variable to keep count of the connected components.
    count = 0

    # Iterate through all nodes in the graph.
    for node in graph:
        # If explore() returns True, it means we've found a new connected component, so we increment the count.
        if explore(graph, node, visited):
            count += 1
    # Return the count of connected components.
    return count

# This is a recursive function that performs depth-first search to explore a connected component.
def explore(graph, current, visited):
    # If the current node has already been visited, return False.
    if current in visited:
        return False
    # Mark the current node as visited by adding it to the 'visited' set.
    visited.add(current)
    # Recursively explore all neighbors of the current node.
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    # Return True to indicate that a connected component has been fully explored.
    return True

# Define the graph as a dictionary where each node is associated with its neighboring nodes.
graph = {0: [8, 1, 5],
         1: [0],
         5: [0, 8],
         8: [0, 5],
         2: [3, 4],
         3: [2, 4],
         4: [3, 2]
         }

# Call the Connected_Components_Count function to find the number of connected components.
count = Connected_Components_Count(graph)
# Print the count to the console.
print(count)
