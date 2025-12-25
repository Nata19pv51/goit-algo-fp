from collections import deque
import heapq
import networkx as nx
from matplotlib import pyplot as plt

from task_4 import create_tree, draw_tree


def generate_colors(n):
    colors = []
    for i in range(n):
        level = int(255 * (i / n))
        colors.append(f'#00{level:02x}A0') # Відтінки синього/зеленого
    return colors

def dfs_iterative(root):
    if not root:
        return []
    
    visited_order = [] 
    visited_set = set()
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        if node.id not in visited_set:
            visited_set.add(node.id)
            visited_order.append(node.id)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
    generated_colors = generate_colors(len(visited_order))
    colors_map = {node_id: color for node_id, color in zip(visited_order, generated_colors)}
    draw_tree(root, colors_map) 

def bfs_iterative(root):
    if not root:
        return
    
    queue = deque([root])
    visited = []
    
    while queue:
        node = queue.popleft()
        visited.append(node.id)
        if node.right:
            queue.append(node.right)   
        if node.left:
            queue.append(node.left)

    colors_map = {node_id: color for node_id, color in zip(visited, generate_colors(len(visited)))}
    draw_tree(root, colors_map) 

if __name__ == "__main__":
    arr = [1, 4, 6, 3, 6, 2, 10, 5, 8]
    heapq.heapify(arr)
    root = create_tree(arr)

    dfs_iterative(root)
    bfs_iterative(root)