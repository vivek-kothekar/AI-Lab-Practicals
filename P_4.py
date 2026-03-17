import heapq

def find_optimal_path(adjacency, source, destination, h_values):
    priority_queue = []
    heapq.heappush(priority_queue, (h_values[source], source))

    predecessors = {}
    path_cost = {node: float('inf') for node in adjacency}
    path_cost[source] = 0

    estimated_cost = {node: float('inf') for node in adjacency}
    estimated_cost[source] = h_values[source]

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)

        if current_node == destination:
            route = []
            while current_node:
                route.append(current_node)
                current_node = predecessors.get(current_node)
            return route[::-1]

        for adjacent, edge_weight in adjacency[current_node].items():
            tentative_cost = path_cost[current_node] + edge_weight

            if tentative_cost < path_cost[adjacent]:
                predecessors[adjacent] = current_node
                path_cost[adjacent] = tentative_cost
                estimated_cost[adjacent] = tentative_cost + h_values[adjacent]
                heapq.heappush(priority_queue, (estimated_cost[adjacent], adjacent))

    return None


adjacency = {
    'S': {'A': 1, 'G': 10},
    'A': {'B': 2, 'C': 1},
    'B': {'D': 5},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 2},
    'G': {}
}

h_values = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0
}

source = 'S'
destination = 'G'

optimal_path = find_optimal_path(adjacency, source, destination, h_values)

if optimal_path:
    print("Shortest Path:", optimal_path)
    total_weight = 0
    for idx in range(len(optimal_path) - 1):
        total_weight += adjacency[optimal_path[idx]][optimal_path[idx + 1]]
    print("Total Cost:", total_weight)
else:
    print("No path found")
