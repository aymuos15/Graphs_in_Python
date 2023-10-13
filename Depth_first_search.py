# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['C','B'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : [],
    'F' : []
}

'''
In Python, a stack is implemented using a list object.

To push an item in the stack, use the list function append list.append(item)
To pop an item in the stack, use the list function pop list.pop()
To get the top most item in the stack, write list[-1]
'''

def iterative_dfs(graph, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

def recursive_dfs(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursive_dfs(graph, neighbor)

# iterative_dfs(graph, 'A')
# recursive_dfs(graph, 'A')

# Reference: https://www.youtube.com/watch?v=tWVWeAqZ0WU (freeCodeCamp)
