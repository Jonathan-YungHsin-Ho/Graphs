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
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
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
        # print(paths)
        return paths


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        graph.add_edge(ancestor[1], ancestor[0])
    # print(graph.vertices)
    paths = graph.bft(starting_node)
    longest_path = []
    for path in paths:
        if len(path) > len(longest_path):
            longest_path = path
        elif len(path) == len(longest_path):
            if path[-1] < longest_path[-1]:
                longest_path = path
    # print(longest_path)
    if len(longest_path) == 1:
        return -1
    else:
        return longest_path[-1]


# We want to create a graph where each node can have two parents and two children
# directed, acyclic graph

# Loop through each tuple in array to build graph
# # create node for 1st tuple, create node for 2nd tuple
# # build edge from child to ancestor

# Once the graph is built, traverse to find all paths
# Once paths are found, find longest path, return the value at end of path

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 3))
print(earliest_ancestor(test_ancestors, 4))
print(earliest_ancestor(test_ancestors, 5))
print(earliest_ancestor(test_ancestors, 6))
print(earliest_ancestor(test_ancestors, 7))
print(earliest_ancestor(test_ancestors, 8))
print(earliest_ancestor(test_ancestors, 9))
print(earliest_ancestor(test_ancestors, 10))
print(earliest_ancestor(test_ancestors, 11))
