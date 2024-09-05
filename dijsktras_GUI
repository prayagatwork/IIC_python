import tkinter as tk
import heapq

# Dijkstra's algorithm function
def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# GUI Application
class GraphGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Visualization")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.nodes = {}  # stores node coordinates and their names
        self.edges = []  # stores edges between nodes

        self.canvas.bind("<Button-1>", self.add_node)

        self.start_label = tk.Label(root, text="Enter start node:")
        self.start_label.pack(pady=5)

        self.start_entry = tk.Entry(root)
        self.start_entry.pack(pady=5)

        self.calculate_button = tk.Button(root, text="Calculate Shortest Path", command=self.calculate)
        self.calculate_button.pack(pady=5)

    def add_node(self, event):
        node_name = f"N{len(self.nodes) + 1}"
        self.nodes[node_name] = (event.x, event.y)
        self.canvas.create_oval(event.x-10, event.y-10, event.x+10, event.y+10, fill="blue")
        self.canvas.create_text(event.x, event.y-15, text=node_name, fill="black")

        if len(self.nodes) > 1:
            self.connect_nodes()

    def connect_nodes(self):
        if len(self.nodes) < 2:
            return

        nodes_list = list(self.nodes.keys())
        last_node = nodes_list[-1]
        prev_node = nodes_list[-2]

        x1, y1 = self.nodes[prev_node]
        x2, y2 = self.nodes[last_node]

        self.canvas.create_line(x1, y1, x2, y2)
        self.edges.append((prev_node, last_node))

    def calculate(self):
        start_node = self.start_entry.get()
        if start_node not in self.nodes:
            return

        # Convert edges into a graph dictionary
        graph = {node: {} for node in self.nodes}
        for edge in self.edges:
            node1, node2 = edge
            weight = self.calculate_distance(self.nodes[node1], self.nodes[node2])
            graph[node1][node2] = weight
            graph[node2][node1] = weight

        # Run Dijkstra's algorithm
        result = dijkstra(graph, start_node)
        print("Shortest paths:", result)

        # Highlight the shortest paths on the canvas
        self.highlight_paths(result)

    def calculate_distance(self, coord1, coord2):
        return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5

    def highlight_paths(self, result):
        self.canvas.delete("highlight")
        for node in result:
            if result[node] == float('infinity'):
                continue

            x, y = self.nodes[node]
            self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="green", tags="highlight")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    gui = GraphGUI(root)
    root.mainloop()
