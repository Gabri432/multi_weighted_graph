class MultiWeightedGraph:
    '''An instance of class MultiWeightedGraph represents a graph in which each edge is associated to one or more weights.'''
    class _GraphEdge:
        def __init__(self, vertex_a: str, vertex_b: str, weights: list[float]) -> None:
            self.vertex_a = vertex_a
            self.vertex_b = vertex_b
            self.weights = weights
    
        def __str__(self) -> str:
            return "(" + self.vertex_a + ")- "+ str(self.weights) + " -(" + self.vertex_b +")"
            
        def __repr__(self) -> str:
            return f"GraphEdge({self.vertex_a!r}, {self.vertex_b!r}, {self.weights!r})"

    class _Partition:
        def __init__(self, name: str) -> None:
            self.name = name
            self.elements = set(name)

        def __find__(self, name: str) -> bool:
            return self.elements.__contains__(name)

        def __union__(self, elements: set[str], new_name: str) -> None:
            self.elements.union(elements)
            self.name = new_name

        def __eq__(self, value: object) -> bool:
            if not isinstance(value, MultiWeightedGraph._Partition):
                return False

            return value.name == self.name

        def __hash__(self) -> int:
            return hash(self.name)
    
    def __init__(self, name: str = "My new multi-weighted graph", number_of_weights_per_edge: int = 1) -> None:
        self.name = name
        self.weights_per_edge = number_of_weights_per_edge
        self.edges: list[MultiWeightedGraph._GraphEdge] = []

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"MultiWeightedGraph({self.name!r}, {self.weights_per_edge})"

    def add_edge(self, first_vertice_name: str, second_vertice_name: str, weights: list[float]) -> None:
        edge = self._GraphEdge(first_vertice_name, second_vertice_name, weights)
        self.edges.append(edge)

    def remove_edge(self, first_vertice_name: str, second_vertice_name: str) -> None:
        for edge in self.edges:
            condition1 = edge.vertex_a == first_vertice_name and edge.vertex_b == second_vertice_name
            condition2 = edge.vertex_a == second_vertice_name and edge.vertex_b == first_vertice_name
            if condition1:
                self.edges.remove(edge)
            elif condition2:
                self.edges.remove(edge)

    def minimal_spanning_tree(self, weights_to_select: int) -> list[MultiWeightedGraph._GraphEdge]:
        ordered_edges = sorted(self.edges, key=lambda edge:(edge.weights[weights_to_select]))
        current_tree: list[MultiWeightedGraph._GraphEdge] = []
        partition: list[MultiWeightedGraph._Partition] = []
        for edge in ordered_edges:
            part_a = self._Partition(edge.vertex_a)
            part_b = self._Partition(edge.vertex_b)
            if partition.__contains__(part_a) == False:
                partition.append(part_a)
            if partition.__contains__(part_b) == False:
                partition.append(part_b)
            if not (part_a.__find__(part_b.name) or part_b.__find__(part_a.name)):
                part_a.__union__(part_b.elements, part_a.name)
                partition.remove(part_b)
                current_tree.append(edge)
        return current_tree