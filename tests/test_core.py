from multi_weighted_graph import MultiWeightedGraph


def test_add_edges():
    my_graph = MultiWeightedGraph()
    my_graph.add_edge("a", "b", [2])
    assert len(my_graph.edges) == 1

def test_remove_edges():
    my_graph = MultiWeightedGraph()
    my_graph.add_edge("a", "b", [2])
    my_graph.add_edge("c", "d", [2])
    my_graph.remove_edge("a", "b")
    assert len(my_graph.edges) == 1

def test_minimal_spanning_tree_1():
    my_graph = MultiWeightedGraph()
    my_graph.add_edge("a", "b", [2])
    my_graph.add_edge("c", "d", [2])
    my_graph.add_edge("a", "d", [2])
    my_graph.add_edge("a", "c", [3])
    spanning_tree = my_graph.minimal_spanning_tree(0)
    total_weight = 0
    for edge in spanning_tree:
        total_weight += edge.weights[0]
    assert total_weight == 6

def test_minimal_spanning_tree_2():
    my_graph = MultiWeightedGraph("", 2)
    my_graph.add_edge("a", "b", [4, 2])
    my_graph.add_edge("b", "c", [3, 2])
    my_graph.add_edge("c", "d", [2, 2])
    my_graph.add_edge("a", "d", [1, 2])
    spanning_tree_first_weight = my_graph.minimal_spanning_tree(0)
    spanning_tree_second_weight = my_graph.minimal_spanning_tree(1)
    total_weight_1 = 0
    total_weight_2 = 0
    for edge in spanning_tree_first_weight:
        total_weight_1 += edge.weights[0]
    for edge in spanning_tree_second_weight:
            total_weight_2 += edge.weights[1]
    assert total_weight_1 == total_weight_2

def test_matrix_of_distances():
    my_graph = MultiWeightedGraph("", 2)
    my_graph.add_edge("a", "b", [4, 2])
    my_graph.add_edge("b", "c", [3, 2])
    my_graph.add_edge("c", "d", [2, 2])
    my_graph.add_edge("a", "d", [1, 2])
    v_to_idx = {v: i for i, v in enumerate(my_graph.vertices)}
    matrix_0 = my_graph.matrix_of_distances(0)
    matrix_1 = my_graph.matrix_of_distances(1)
    b = v_to_idx.get("b")
    d = v_to_idx.get("d")
    if b != None and d != None:
        assert matrix_0[b][d] == 5
        assert matrix_1[d][b] == 4

def test_matrix_of_distances_from_source():
    my_graph = MultiWeightedGraph("", 2)
    my_graph.add_edge("a", "b", [4, 2])
    my_graph.add_edge("b", "c", [3, 2])
    my_graph.add_edge("c", "d", [2, 2])
    my_graph.add_edge("a", "d", [1, 2])
    v_to_idx = {v: i for i, v in enumerate(my_graph.vertices)}
    vector_a = my_graph.matrix_of_distances_from_source("a", 0)
    vector_c = my_graph.matrix_of_distances_from_source("c", 1)
    vector_b = my_graph.matrix_of_distances_from_source("b", 0)
    vector_d = my_graph.matrix_of_distances_from_source("d", 0)
    a = v_to_idx.get("a")
    b = v_to_idx.get("b")
    c = v_to_idx.get("c")
    d = v_to_idx.get("d")
    print(v_to_idx)
    if a != None and c != None and b != None and d != None:
        assert vector_a[c] == 3
        assert vector_c[a] == 4
        assert vector_b[d] == 5
        assert vector_d[b] == 5

def test_add_vertices():
    my_graph = MultiWeightedGraph("", 1)
    my_graph.add_vertex("B")
    my_graph.add_vertex("F")
    my_graph.add_vertex("Z")
    my_graph.add_vertex("A")
    my_graph.add_vertex("A")
    vertices = my_graph.vertices
    assert vertices == ["A", "B", "F", "Z"]

def test_remove_vertices_1():
    my_graph = MultiWeightedGraph("", 1)
    my_graph.add_vertex("B")
    my_graph.add_vertex("F")
    my_graph.add_vertex("Z")
    my_graph.add_vertex("A")
    my_graph.remove_vertex("B")
    vertices = my_graph.vertices
    assert vertices == ["A", "F", "Z"]

def test_remove_vertices_2():
    my_graph = MultiWeightedGraph("", 1)
    my_graph.add_edge("A", "B", [1])
    my_graph.add_edge("C", "B", [1])
    my_graph.add_edge("A", "F", [1])
    my_graph.add_edge("C", "D", [1])
    my_graph.add_edge("E", "F", [1])
    my_graph.remove_vertex("B")
    vertices = my_graph.vertices
    edges = my_graph.edges
    assert vertices == ["A", "C", "D", "E", "F"]
    assert edges.__len__() == 4

def test_order_vertices():
    my_graph = MultiWeightedGraph("", 1)
    my_graph.add_edge("A", "B", [1])
    my_graph.add_edge("C", "B", [1])
    my_graph.add_edge("A", "F", [1])
    my_graph.add_edge("C", "D", [1])
    my_graph.add_edge("E", "F", [1])
    vertices = my_graph.vertices
    assert vertices == ["A", "B", "C", "D", "E", "F"]
    my_graph.order_vertices(False)
    vertices = my_graph.vertices
    assert vertices == ["F", "E", "D", "C", "B", "A"]