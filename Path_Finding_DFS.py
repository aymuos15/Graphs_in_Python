graph = {
    'F' : ['G','I'],
    'G' : ['H'],
    'H' : [],
    'I' : ['G','K'],
    'J' : ['I'],
    'K' : []
}

# Define a function to check if there is a path between two nodes in a graph using DFS.
# Parameters:
# - graph: A dictionary representing the directed graph.
# - source: The current node being checked.
# - destination: The target node to find a path to.

def is_path_dfs(graph, source, destination):
    # Base case: If the current node is the destination, return True indicating a path is found.
    if source == destination:
        return True

    # Recursive case: Check each neighbor of the current node.
    for neighbor in graph[source]:
        # Recursively call the function for each neighbor.
        if is_path_dfs(graph, neighbor, destination):
            return True  # Print a message if a path is found.

    # If the loop completes without finding a path, return False.
    return False

# Call the is_path_dfs function with a sample graph and source-destination nodes.
result = is_path_dfs(graph, 'F', 'K')

# Check the result and print a message.
if result:
    print('Path exists')
else:
    print('Path is not there')
