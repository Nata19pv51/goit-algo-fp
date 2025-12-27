import heapq


def dijkstra(graph, start_node):
    # Ініціалізація відстаней: всі нескінченні, стартова - 0
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    
    priority_queue = [(0, start_node)]
    
    while len(priority_queue) > 0:
        # Вибираємо вершину з найменшою поточною відстанню
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        # Розглядаємо всіх сусідів поточної вершини
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

if __name__ == "__main__":
    transport_graph = {
        'Київ': {'Глеваха': 34, 'Васильків': 50, 'Обухів': 47},
        'Глеваха': {'Фастів': 48, 'Біла Церква': 59},
        'Васильків': {'Гребенки': 30, 'Обухів': 35},
        'Обухів': {'Кагарлик': 33},
        'Кагарлик': {'Біла Церква': 58, 'Миронівка': 21},
        'Фастів': {'Біла Церква': 38},
        'Гребенки': {'Біла Церква': 20},
        'Біла Церква': {'Тараща': 46},
        'Миронівка': {},
        'Тараща': {}
    }
    
start = 'Київ'
shortest_paths = dijkstra(transport_graph, start)

print(f"Найкоротші відстані від вершини {start}:")
for node, distance in shortest_paths.items():
    print(f"До {node}: {distance}")
