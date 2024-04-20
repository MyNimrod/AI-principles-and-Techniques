# Ethiopia Travel State Space Search

## Overview

This project represents a state space graph for the traveling problem in Ethiopia. The code includes classes to define the graph, problem, nodes, and search strategies.

## Structure

- **Graph**: Represents the state space graph with nodes and edges.
- **Problem**: Defines the initial state and goal state.
- **GraphProblem**: Inherits from Problem and uses a graph to define state transitions.
- **Node**: Represents a node in the search tree with state, parent, action, and depth attributes.

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

## Running the Code

To run the code, create a Python script and include the provided classes and graph definition. You can then instantiate a problem and explore the state space using the defined methods.

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
