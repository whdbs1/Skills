import heapq

graph = [[] for _ in range(num_node)]
for _ in range(num_edge):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

def dijkstra(graph, start): 
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)] 
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
