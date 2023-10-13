graph = {
    'F' : ['G','I'],
    'G' : ['H'],
    'H' : [],
    'I' : ['G','K'],
    'J' : ['I'],
    'K' : []
}

# Define a function to check if there is a path between two nodes in a graph using BFS.
# Parameters:
# - graph: A dictionary representing the directed graph.
# - source: The starting node for the search.
# - destination: The target node to find a path to.

def is_path_bfs(graph, source, destination):
    # Create a queue to perform BFS.
    queue = [source]
    
    # Start BFS loop.
    while len(queue) > 0:
        # Get the current node from the queue.
        current = queue.pop(0)
        
        # Check if the current node is the destination node.
        if current == destination:
            return True  # A path from source to destination exists.
        
        # If not, add the neighbors of the current node to the queue for further exploration.
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    # If the loop completes without finding the destination, return False.
    return False

# Call the is_path_bfs function with a sample graph and source-destination nodes.
result = is_path_bfs(graph, 'H', 'K')

# Check the result and print a message.
if result:
    print('Path exists')
else:
    print('Path is not there')
