import networkx as nx
import matplotlib.pyplot as plt
import random

def create_graph():
    G = nx.Graph()
    nodes = [(i,j) for i in range(4) for j in range(4)]
    G.add_nodes_from(nodes)

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if j != k:
                    G.add_edge((i,j), (i,k), weight=random.randint(1,10))

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i != k:
                    G.add_edge((i,j), (k,j), weight=random.randint(1,10))

    return G

def draw_graph(G):
    pos = dict()
    for i in range(4):
        for j in range(4):
            pos[(i,j)] = (i,j)
            
    nx.draw(G, pos, node_color='k', edge_color='k')
    
    edge_labels = dict([((u,v,), d['weight']) for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

def walk(G, steps, start_node):
    node = start_node
    visited = [node]
    node_colors = ['C0'] 
    edge_colors = []

    for i in range(steps):
        neighbords = list(G.neighbors(node))
        next_node = random.choice(neighbords)
        edge = (node, next_node)

        node_colors.append(f'C{i+1}')
        edge_colors.append(edge)

        node = next_node
        visited.append(node)

    return visited, node_colors, edge_colors

def draw_walk(G, visited, node_colors, edge_colors):
    pos = dict()
    for i in range(4):
        for j in range(4):
            pos[(i,j)] = (i,j)

    for i, edge in enumerate(edge_colors):
        nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color=f'C{i}', width=6.0)

    for i, n in enumerate(visited):
        nx.draw_networkx_nodes(G, pos, nodelist=[n], node_color=node_colors[i])

    edge_labels = dict([((u,v,), d['weight']) for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    nx.draw_networkx_labels(G, pos)
    plt.axis('off')
    plt.show()


G = create_graph()
draw_graph(G)

visited, node_colors, edge_colors = walk(G, 2, (2,2))
draw_walk(G, visited, node_colors, edge_colors)
