# MultiWeightedGraph

- A class representing graphs having multiple weights associated to each edge.

## Project structure
```
- multi_weighted_graph (root)
    - license
    - README.md
    - .gitignore
    - pyproject.toml
    - src/multi_weighted_graph (folder)
        - __init__.py
        - _core.py
        - _utils.py
        - py.typed
    - tests (folder)
        - test_core.py
```

## Tech stack

- Python 3.14.3
- pytest 9.1.1

## How to use it
- To run tests run the command:
```
pytest
```

- Import the class and start using it:
```py
from multi_weighted_graph import MultiWeightedGraph

my_graph = MultiWeightedGraph("My New Graph", 2)
my_graph.add_edge("a", "b", [4, 2])
my_graph.add_edge("b", "c", [3, 2])
my_graph.add_edge("c", "d", [2, 2])
my_graph.add_edge("a", "d", [1, 3])
my_graph.add_edge("e", "f", [3, 5])
my_graph.remove_edge("e", "f")

print(my_graph.minimal_spanning_tree())
print(my_graph.matrix_of_distances())
print(my_graph.matrix_of_distances_from_source("a"))
```

- Calculate the minimal spanning tree:
```py
>>> print(my_graph.minimal_spanning_tree()) 
[GraphEdge('a', 'd', [1, 2]), GraphEdge('c', 'd', [2, 2]), GraphEdge('b', 'c', [3, 2])]

>>> print(my_graph.minimal_spanning_tree(1)) # building the minimal spanning tree using the second weight associated to edges
[GraphEdge('a', 'b', [4, 2]), GraphEdge('b', 'c', [3, 2]), GraphEdge('c', 'd', [2, 2])]

```

- Calculate the matrix of distances between each vertex:
```py
>>> print(my_graph.matrix_of_distances())
[[0, 4, 3, 1], [4, 0, 3, 5], [3, 3, 0, 2], [1, 5, 2, 0]]
```

- Calculate the matrix of distances from a vertex to all the others
```py
>>> print(my_graph.matrix_of_distances_from_source("a", 0)) # distance from vertex "a" to all the others, using first weight associated to edges
[0, 4, 3, 1]
```


## Notes

- The intended use of this project is for personal and/or educational purposes.
- The project is under the Apache License, that you can see from [here](https://github.com/Gabri432/multi_weighted_graph/blob/main/license)

