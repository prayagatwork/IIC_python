def calculate_time(distance, load):
    # Assuming an average speed of 60 km/h
    # Speed reduces by 10% for every ton over a baseline of 5 tons
    base_speed = 60  # 60 km/h
    speed_reduction = (load - 5) * 0.1 * base_speed if load > 5 else 0
    speed = max(base_speed - speed_reduction, 20)  # Minimum speed capped at 20 km/h
    
    time = distance / speed
    return time

# Assume this function is called when calculating the shortest path
def calculate(self):
    start_node = self.start_entry.get()
    if start_node not in self.nodes:
        return

    graph = {node: {} for node in self.nodes}
    for edge in self.edges:
        node1, node2 = edge
        distance = self.calculate_distance(self.nodes[node1], self.nodes[node2])
        # Calculate time based on distance and a truck load of 10 tons
        time = calculate_time(distance, 10)
        graph[node1][node2] = time
        graph[node2][node1] = time

    result = dijkstra(graph, start_node)
    print("Shortest times:", result)
    self.highlight_paths(result)
