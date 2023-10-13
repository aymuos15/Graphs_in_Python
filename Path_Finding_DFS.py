graph = {
    'F' : ['G','I'],
    'G' : ['H'],
    'H' : [],
    'I' : ['G','K'],
    'J' : ['I'],
    'K' : []
}

def is_path_dfs(graph, source, destination):
    if source == destination:
        return True
    for neighbor in graph[source]:
        if is_path_dfs(graph, neighbor, destination):
            return print('Path is there')
    return False

is_path_dfs(graph, 'F', 'K')
