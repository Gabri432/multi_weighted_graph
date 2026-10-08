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