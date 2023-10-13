def Undirected_Path_finding_dfs(edges, start, end):
    # Create the graph from the list of edges
    graph = edge2graph(edges)
    
    # Call the path_check function to find the path
    path = path_check(graph, start, end, visited=set())
    
    if path:
        print("Path is there from", start, "to", end)
    else:
        print("No path from", start, "to", end)

def path_check(graph, start, end, visited=set()):
    # If the start and end nodes are the same, a path exists
    if start == end:
        return True
    
    # If the start node is already in the visited set, there's no path
    if start in visited:
        return False
    
    # Mark the current node as visited
    visited.add(start)
    
    # Check all neighbors of the current node recursively
    for neighbor in graph[start]:
        if path_check(graph, neighbor, end, visited):
            return True
    
    # If no path is found, return False
    return False

def edge2graph(edges):
    # Create an empty dictionary to represent the graph
    graph = {}
    
    # Create the graph by iterating through the list of edges
    for edge in edges:
        [a, b] = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        # Add both nodes as neighbors of each other
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

edges = [['i', 'j'],
         ['k', 'i'],
         ['m', 'k'],
         ['k', 'l'],
         ['o', 'n']]

start_node = 'o'
end_node = 'm'
Undirected_Path_finding_dfs(edges, start_node, end_node)
