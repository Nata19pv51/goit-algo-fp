import networkx as nx


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distance_between_cities = {vertex: float('infinity') for vertex in graph}
    distance_between_cities[start] = 0
    unvisited = set(graph.nodes())
    
    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distance_between_cities[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distance_between_cities[current_vertex] == float('infinity'):
            break
        
        for neighbor, attributes in graph.adj[current_vertex].items():
            if "distance" not in attributes:
                continue
                
            weight = attributes["distance"]
            new_distance = distance_between_cities[current_vertex] + weight 

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if new_distance < distance_between_cities[neighbor]:
                distance_between_cities[neighbor] = new_distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distance_between_cities

G = nx.Graph()
edges = [
    ('A', 'B', 5), ('A', 'C', 10),
    ('B', 'D', 3), ('B', 'E', 8),
    ('C', 'E', 2), ('D', 'E', 1),
    ('E', 'F', 6), ('D', 'F', 12)
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)