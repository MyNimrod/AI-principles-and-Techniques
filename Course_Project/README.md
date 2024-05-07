# Ethiopia Travel State Space Search

## Overview

This project represents a state space graph for the traveling problem in Ethiopia. The code includes classes to define the graph, problem, nodes, and search strategies.

## Structure

- **Graph**: Represents the state space graph with nodes and edges.
- **Problem**: Defines the initial state and goal state.
- **GraphProblem**: Inherits from Problem and uses a graph to define state transitions.
- **Node**: Represents a node in the search tree with state, parent, action, and depth attributes.
- **SearchSolver**: A class to solve the problem using a specified search strategy (BFS or DFS).

## Usage

1. **Graph Class**: Initializes a graph with nodes and edges.
    ```python
    visit_ethiopia = Graph(
        dict({
            'Addis Ababa': {'Adama', 'Ambo', 'Debre Berhan'},
            ...
            'Humera': {'Shire', 'Gondar'}
        }),
        directed=False
    )
    ```

2. **GraphProblem Class**: Defines a problem on the graph.
    ```python
    problem = GraphProblem('Addis Ababa', 'Gondar', visit_ethiopia)
    ```

3. **Node Class**: Represents a node in the search tree.
    ```python
    node = Node('Addis Ababa')
    ```

4. **SearchSolver Class**: Solves the problem using the specified search strategy.
    ```python
    solver = SearchSolver(visit_ethiopia, 'Addis Ababa', 'Shire', strategy='bfs')
    final_node = solver.solve()
    if final_node is not None:
        print("Breadth First Search Solution:", final_node.solution())
    else:
        print("Path does not exist")

    solver = SearchSolver(visit_ethiopia, 'Addis Ababa', 'Shire', strategy='dfs')
    final_node = solver.solve()
    if final_node is not None:
        print("Depth First Search Solution:", final_node.solution())
    else:
        print("Path does not exist")
    ```

## Running the Code

To run the code, create a Python script and include the provided classes and graph definition. You can then instantiate a problem and explore the state space using the defined methods and strategies.

## Example

```python
from collections import deque

# Include the provided code here

# Define the problem
problem = GraphProblem('Addis Ababa', 'Gondar', visit_ethiopia)

# Create the root node
root_node = Node(problem.initial)

# Expand the root node
children = root_node.expand(problem)
for child in children:
    print(child)

# Solve using breadth-first search
solver = SearchSolver(visit_ethiopia, 'Addis Ababa', 'Shire', strategy='bfs')
final_node = solver.solve()
if final_node is not None:
    print("Breadth First Search Solution:", final_node.solution())
else:
    print("Path does not exist")

# Solve using depth-first search
solver = SearchSolver(visit_ethiopia, 'Addis Ababa', 'Shire', strategy='dfs')
final_node = solver.solve()
if final_node is not None:
    print("Depth First Search Solution:", final_node.solution())
else:
    print("Path does not exist")

