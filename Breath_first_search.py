# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['C','B'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : [],
    'F' : []
}

def bfs(graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)

bfs(graph, 'A')
