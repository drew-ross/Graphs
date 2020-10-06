class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        visited = set()
        q = []
        q.append(starting_vertex)
        while q:
            v = q.pop(0)
            if v not in visited:
                visited.add(v)
                print(v)
                for n in self.vertices[v]:
                    q.append(n)

    def dft(self, starting_vertex):
        visited = set()
        s = []
        s.append(starting_vertex)
        while s:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for n in self.vertices[v]:
                    s.append(n)

    def dft_recursive(self, starting_vertex, visited=set()):
        visited.add(starting_vertex)
        print(starting_vertex)
        for node in self.vertices[starting_vertex]:
            if node not in visited:
                self.dft_recursive(node, visited)

    def bfs(self, starting_vertex, destination_vertex):
        visited = set()
        q = []
        q.append([starting_vertex])
        while q:
            path = q.pop(0)
            if path[-1] == destination_vertex:
                return path
            if path[-1] not in visited:
                visited.add(path[-1])
                for n in self.vertices[path[-1]]:
                    q.append(path + [n])

    def dfs(self, starting_vertex, destination_vertex):
        visited = set()
        s = []
        s.append([starting_vertex])
        while s:
            path = s.pop()
            if path[-1] == destination_vertex:
                return path
            if path[-1] not in visited:
                visited.add(path[-1])
                for n in self.vertices[path[-1]]:
                    s.append(path + [n])

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set()):
        path = []
        if starting_vertex == destination_vertex:
            return [starting_vertex]
        elif starting_vertex not in visited:
            visited.add(starting_vertex)
            for node in self.vertices[starting_vertex]:
                path = [starting_vertex] + self.dfs_recursive(
                    node, destination_vertex, visited
                )
        return path


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    # graph.bft(1)
    # print('')

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    # graph.dft(1)
    # graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    # print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
