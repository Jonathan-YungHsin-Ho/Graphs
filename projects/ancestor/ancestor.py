class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.vertices[v1].add(v2)

    def get_ancestor(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        paths = []
        while queue.size() > 0:
            path_to_current_node = queue.dequeue()
            current_node = path_to_current_node[-1]
            if not self.get_ancestor(current_node):
                paths.append(path_to_current_node)
            if current_node not in visited:
                visited.add(current_node)
                for ancestor in self.get_ancestor(current_node):
                    path_to_ancestor = [*path_to_current_node, ancestor]
                    queue.enqueue(path_to_ancestor)
        return paths


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        graph.add_edge(ancestor[1], ancestor[0])
    paths = graph.bft(starting_node)

    longest_path = []
    for path in paths:
        if len(path) > len(longest_path) or \
                (len(path) == len(longest_path) and path[-1] < longest_path[-1]):
            longest_path = path
    return -1 if len(longest_path) == 1 else longest_path[-1]
