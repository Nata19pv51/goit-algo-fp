import heapq
import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.right = None
        self.left = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
    if node.left:
        graph.add_edge(node.id, node.left.id)
        l = x - 1 / 2 ** layer
        pos[node.left.id] = (l, y - 1)
        l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
        graph.add_edge(node.id, node.right.id)
        r = x + 1 / 2 ** layer
        pos[node.right.id] = (r, y - 1)
        r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if colors is None:
        colors = {}
        
    colors_map = [colors.get(node, "#1296F0") for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors_map)
    plt.show()

def create_tree(arr, index=0):
    if index >= len(arr):
        return None
    
    node = Node(arr[index])
    node.left = create_tree(arr, 2 * index + 1)
    node.right = create_tree(arr, 2 * index + 2)
    
    return node


if __name__ == "__main__":
    arr = [1, 4, 6, 3, 6, 2, 10, 5, 8]
    heapq.heapify(arr)
    root = create_tree(arr)
    
    draw_tree(root)
