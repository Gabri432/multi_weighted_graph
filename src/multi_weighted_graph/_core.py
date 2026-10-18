class MultiWeightedGraph:
    '''An instance of class MultiWeightedGraph represents a graph in which each edge is associated to one or more weights.'''
    class GraphEdge:
        def __init__(self, vertex_a: str, vertex_b: str, weights: list[float]) -> None:
            self.vertex_a = vertex_a
            self.vertex_b = vertex_b
            self.weights = weights
    
        def __str__(self) -> str:
            return "(" + self.vertex_a + ")- "+ str(self.weights) + " -(" + self.vertex_b +")"
            
        def __repr__(self) -> str:
            return f"GraphEdge({self.vertex_a!r}, {self.vertex_b!r}, {self.weights!r})"

    class __Partition__:
        def __init__(self, name: str) -> None:
            self.name = name
            self.elements = set(name)

        def __find__(self, name: str) -> bool:
            return self.elements.__contains__(name)

        def __str__(self) -> str:
            return "{"+ self.elements.__str__() +"}"
                    
        def __repr__(self) -> str:
            return f"Partition(name={self.name}, elements={self.elements})"

        def __union__(self, elements: set[str], new_name: str) -> None:
            self.elements = self.elements.union(elements)
            self.name = new_name

        def __eq__(self, value: object) -> bool:
            if not isinstance(value, MultiWeightedGraph.__Partition__):
                return False

            return value.name == self.name

        def __hash__(self) -> int:
            return hash(self.name)

    class __Vertex__:
        def __init__(self, vertex: str, distance_from_source: float) -> None:
            self.vertex = vertex
            self.distance_from_source = distance_from_source

        def __str__(self) -> str:
            return "{"+ self.vertex +" : " + str(self.distance_from_source)+"}"
                    
        def __repr__(self) -> str:
            return f"Vertex(name={self.vertex}, distance_from_source={self.distance_from_source})"

    class __VertexNeighbours__:
        def __init__(self, vertex: str, neighbours: list[MultiWeightedGraph.__Vertex__]):
            self.vertex = vertex
            self.neighbourhood = neighbours

        def __str__(self) -> str:
            return "{"+ self.vertex +" : " + str(self.neighbourhood)+"}"
                    
        def __repr__(self) -> str:
            return f"Vertex(name={self.vertex}, neighbours={self.neighbourhood})"
    
    def __init__(self, name: str = "My new multi-weighted graph", number_of_weights_per_edge: int = 1) -> None:
        self.name = name
        self.weights_per_edge = number_of_weights_per_edge
        self.edges: list[MultiWeightedGraph.GraphEdge] = []
        self.vertices: list[str] = []
        self.__alphabetical_order__ = True

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"MultiWeightedGraph({self.name!r}, {self.weights_per_edge})"

    def add_edge(self, first_vertex_name: str, second_vertex_name: str, weights: list[float]) -> None:
        '''Adds an edge to the graph by specifying the name of the vertices, as well as a list of weights to associate to such edge.
        \n\n It also creates the two vertices if they were not specified before.'''
        edge = self.GraphEdge(first_vertex_name, second_vertex_name, weights)
        self.edges.append(edge)
        if (self.vertices.__contains__(first_vertex_name) == False): 
            self.vertices.append(first_vertex_name)
        if (self.vertices.__contains__(second_vertex_name) == False):
            self.vertices.append(second_vertex_name)
        self.order_vertices(self.__alphabetical_order__)

    def remove_edge(self, first_vertex_name: str, second_vertex_name: str) -> None:
        '''Removes an edge from the graph by specifying its two vertices.
        \n\n Removing an edge does not eliminate the vertices associated with.'''
        for edge in self.edges:
            condition1 = edge.vertex_a == first_vertex_name and edge.vertex_b == second_vertex_name
            condition2 = edge.vertex_a == second_vertex_name and edge.vertex_b == first_vertex_name
            if condition1:
                self.edges.remove(edge)
            elif condition2:
                self.edges.remove(edge)

    def add_vertex(self, name: str) -> None:
        '''Adds a new vertex to the graph.'''
        if (self.vertices.__contains__(name) == False): 
            self.vertices.append(name)
            self.order_vertices(self.__alphabetical_order__)

    def remove_vertex(self, name: str) -> None:
        '''Removes a vertex from the graph, as well as <b>ALL</b> its associated edges. 
        \n\n For example, once vertex A is removed, then edges of type (A, x) and (x, A) will also be removed from the graph.'''
        if self.vertices.__contains__(name): 
            for edge in self.edges:
                if edge.vertex_a == name or edge.vertex_b == name:
                    self.edges.remove(edge)
            self.vertices.remove(name)
            self.order_vertices(self.__alphabetical_order__)

    def order_vertices(self, alphabetical_order: bool = True) -> None:
        '''Order the vertices alphabetically by default when True. When False it applies the reverse alphabetical order.'''
        self.vertices = sorted(self.vertices)
        if alphabetical_order == False:
            self.vertices = sorted(self.vertices, reverse=True)
        self.__alphabetical_order__ = alphabetical_order

    def minimal_spanning_tree(self, weights_to_select: int) -> list[MultiWeightedGraph.GraphEdge]:
        '''Calculate the minimal spanning tree based on the weight selected for each edge.'''
        ordered_edges = sorted(self.edges, key=lambda edge:(edge.weights[weights_to_select]))
        current_tree: list[MultiWeightedGraph.GraphEdge] = []
        partition: list[MultiWeightedGraph.__Partition__] = []
        for edge in ordered_edges:
            part_a = self.__Partition__(edge.vertex_a)
            part_b = self.__Partition__(edge.vertex_b)
            if partition.__contains__(part_a) == False:
                partition.append(part_a)
            if partition.__contains__(part_b) == False:
                partition.append(part_b)
            if not self.__same_partition__(partition, edge.vertex_a, edge.vertex_b):
                partition_of_a = self.__find_partition__(partition, edge.vertex_a)
                partition_of_b = self.__find_partition__(partition, edge.vertex_b)
                partition.remove(partition_of_a)
                partition.remove(partition_of_b)
                partition_of_a.__union__(partition_of_b.elements, part_a.name)
                partition.append(partition_of_a)
                current_tree.append(edge)
        return current_tree

    def __same_partition__(self, partition: list[MultiWeightedGraph.__Partition__], vertex_a: str, vertex_b) -> bool:
        for sub_partition in partition:
            if sub_partition.__find__(vertex_a) and sub_partition.__find__(vertex_b):
                return True
        return False

    def __find_partition__(self, partition: list[MultiWeightedGraph.__Partition__], name: str) -> MultiWeightedGraph.__Partition__:
        for sub_partition in partition:
            if sub_partition.name == name or sub_partition.elements.__contains__(name):
                return sub_partition
        return MultiWeightedGraph.__Partition__("")

    def matrix_of_distances(self, weight_to_select: int = 0) -> list[list[float]]:
        '''Calculates the matrix of distances between vertices based on the weight selected for each edge.'''
        n = len(self.vertices)
        v_to_idx = {v: i for i, v in enumerate(self.vertices)}
        inf = float("inf")
        dist = [[inf] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for edge in self.edges:
            dist[v_to_idx[edge.vertex_a]][v_to_idx[edge.vertex_b]] = edge.weights[weight_to_select]
            dist[v_to_idx[edge.vertex_b]][v_to_idx[edge.vertex_a]] = edge.weights[weight_to_select]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist

    def matrix_of_distances_from_source(self, source: str, weight_to_select: int = 0) -> list[float]:
        '''Calculates the matrix of distances between vertices from a specific vertex (source) based on the weight selected for each edge.'''
        graph = self.__create_adjacency_lists__(weight_to_select)
        n = len(self.vertices)
        explored = [False for _ in range(n)]
        dist_from_source = self.__initialize_distance_vector__(source, weight_to_select)
        v_to_idx = {v: i for i, v in enumerate(self.vertices)}
        idx_to_v = {i: v for i, v in enumerate(self.vertices)}
        a = (v_to_idx.get(source))
        if a != None:
            explored[a] = True
        for _, v in enumerate(self.vertices):
            if v != source:
                index_min = self.__get_min_distance_vertex_index__(explored, dist_from_source)
                adjacent_list: list[MultiWeightedGraph.__Vertex__] = []
                vertex_of_min_distance = idx_to_v.get(index_min)
                if vertex_of_min_distance != None:
                    adjacent_list = self.__get_specific_adjacent_list__(vertex_of_min_distance, graph)
                for vert in adjacent_list:
                    index_of_adj_vertex = v_to_idx.get(vert.vertex)
                    if index_of_adj_vertex != None and explored[index_of_adj_vertex]:
                        continue
                    if index_of_adj_vertex != None and dist_from_source[index_of_adj_vertex] > dist_from_source[index_min] + vert.distance_from_source:
                        dist_from_source[index_of_adj_vertex] = dist_from_source[index_min] + vert.distance_from_source
                explored[index_min] = True
        return dist_from_source

    def __create_adjacency_lists__(self, weight_to_select: int = 0) -> list[MultiWeightedGraph.__VertexNeighbours__]:
        main_list: list[MultiWeightedGraph.__VertexNeighbours__] = []
        for vertex in self.vertices:
            adj: list[MultiWeightedGraph.__Vertex__] = []
            for edge in self.edges:
                if edge.vertex_a == vertex:
                    new_vertex = MultiWeightedGraph.__Vertex__(edge.vertex_b, edge.weights[weight_to_select])
                    adj.append(new_vertex)
                elif edge.vertex_b == vertex:
                    new_vertex = MultiWeightedGraph.__Vertex__(edge.vertex_a, edge.weights[weight_to_select])
                    adj.append(new_vertex)
            vertex_neighbourhood = MultiWeightedGraph.__VertexNeighbours__(vertex, adj)
            main_list.append(vertex_neighbourhood)
        return main_list
    
    def __get_specific_adjacent_list__(self, vertex: str, graph: list[MultiWeightedGraph.__VertexNeighbours__]) -> list[MultiWeightedGraph.__Vertex__]:
        for v_ne in graph:
            if v_ne.vertex == vertex:
                return v_ne.neighbourhood
        return []

    def __initialize_distance_vector__(self, vertex: str, weight_to_select: int = 0) -> list[float]:
        n = len(self.vertices)
        v_to_idx = {v: i for i, v in enumerate(self.vertices)}
        inf = float("inf")
        dist_from_source = [inf * n for _ in range(n)]
        for i in range(n):
            if i == v_to_idx.get(vertex):
                dist_from_source[i] = 0
            else:
                dist_from_source[i] = inf
        for edge in self.edges:
            a = v_to_idx.get(edge.vertex_a)
            b = v_to_idx.get(edge.vertex_b)
            if edge.vertex_a == vertex and b != None:
                dist_from_source[b] = edge.weights[weight_to_select]
            elif edge.vertex_b == vertex and a != None:
                dist_from_source[a] = edge.weights[weight_to_select]
        return dist_from_source

    def __get_min_distance_vertex_index__(self, explored_vertices: list, distances_from_source: list[float]) -> int:
        min_dist = float("inf")
        index = 0
        for i, dist in enumerate(distances_from_source):
            if dist < min_dist and explored_vertices[i] == False:
                min_dist = dist
                index = i
        return index