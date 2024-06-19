# Importing necessary libraries
import numpy as np  # NumPy for numerical operations, especially useful for handling distance matrices
from collections import deque  # deque for efficient double-ended queue operations, useful for BFS
import heapq  # heapq for priority queue operations, essential for the A* search algorithm


# Function to reconstruct the path from the start node to the goal node
# 'previous' is a dictionary mapping each node to its predecessor in the path
# 's' is the current node
def path(previous, s):
    if s is None:
        return []  # Base case: if there's no predecessor, return an empty list
    else:
        return path(previous, previous[s]) + [s]  # Recursively build the path by adding the current node

# Function to calculate the total cost of a given path
# 'path' is a list of nodes representing the path
# 'step_costs' is a 2D array where step_costs[i][j] is the cost of moving from node i to node j
def pathcost(path, step_costs):
    cost = 0
    # Iterate through each pair of consecutive nodes in the path
    for s in range(len(path) - 1):
        cost += step_costs[path[s]][path[s + 1]]  # Add the cost of moving from path[s] to path[s + 1]
    return cost  # Return the total cost of the path


# Defining a dictionary to represent the map of Ethiopia
# The keys are city names and the values are dictionaries that map neighboring cities to their respective distances
map_distances = {
    'Addis Ababa': {'Adama': 3, 'Ambo': 5, 'Debre Berhan': 5, 'Debre Markos': 13},
    'Adama': {'Matahara': 3, 'Asella': 4, 'Batu': 4, 'Addis Ababa': 3},
    'Ambo': {'Wolkite': 6, 'Addis Ababa': 5, 'Nekemte': 8},
    'Debre Berhan': {'Addis Ababa': 5, 'Debre Sina': 2},
    'Debre Markos': {'Addis Ababa': 13, 'Debre Sina': 17, 'Finote Selam': 3},
    'Matahara': {'Adama': 3, 'Awash': 1},
    'Asella': {'Adama': 4, 'Assasa': 4},
    'Batu': {'Adama': 4, 'Buta Jirra': 2, 'Shashamene': 3},
    'Wolkite': {'Ambo': 6, 'Worabe': 5, 'Jimma': 8, 'Hossana': 5, 'Buta Jirra': 4},
    'Nekemte': {'Ambo': 9, 'Bedelle': 5, 'Gimbi': 4},
    'Debre Sina': {'Debre Berhan': 2, 'Kemise': 7, 'Debre Markos': 17},
    'Finote Selam': {'Debre Markos': 3, 'Bahirdar': 6, 'Injibara': 2},
    'Awash': {'Chiro': 4, 'Gobi Rasu': 5, 'Matahara': 1},
    'Assasa': {'Asella': 4, 'Dodolla': 1},
    'Buta Jirra': {'Batu': 2, 'Wolkite': 4, 'Worabe': 2},
    'Shashamene': {'Batu': 3, 'Dodolla': 3, 'Hawassa': 1, 'Hossana': 7, 'Worabe': 6},
    'Worabe': {'Wolkite': 5, 'Hossana': 2, 'Shashamene': 6, 'Buta Jirra': 2},
    'Jimma': {'Wolkite': 8, 'Bonga': 4, 'Bedelle': 7},
    'Hossana': {'Shashamene': 7, 'Worabe': 2, 'Wolkite': 5, 'Wolaita Sodo': 4},
    'Bedelle': {'Nekemte': 5, 'Gore': 6, 'Jimma': 7},
    'Gimbi': {'Nekemte': 4, 'Dambidollo': 6, 'Assosa': 8},
    'Kemise': {'Debre Sina': 6, 'Dessie': 4},
    'Bahirdar': {'Finote Selam': 6, 'Injibara': 4, 'Metekel': 11, 'Azezo': 7, 'Debre Tabor': 4},
    'Injibara': {'Bahirdar': 4, 'Finote Selam': 2},
    'Chiro': {'Awash': 4, 'Dire Dawa': 8},
    'Gobi Rasu': {'Awash': 5, 'Samara': 10},
    'Dodolla': {'Assasa': 1, 'Shashamene': 3, 'Robe': 13},
    'Hawassa': {'Shashamene': 1, 'Dilla': 3},
    'Bonga': {'Jimma': 4, 'Dawro': 10, 'Tepi': 8, 'Mizan Teferi': 4},
    'Wolaita Sodo': {'Arba Minchi': 4, 'Dawro': 6, 'Hossana': 4},
    'Gore': {'Tepi': 9, 'Gambella': 5, 'Bedelle': 6},
    'Dambidollo': {'Gimbi': 6, 'Assosa': 12, 'Gambella': 4},
    'Assosa': {'Gimbi': 8, 'Dambidollo': 12},
    'Dessie': {'Kemise': 4, 'Woldia': 6},
    'Metekel': {'Bahirdar': 11},
    'Azezo': {'Gondar': 1, 'Bahirdar': 7, 'Metema': 7},
    'Debre Tabor': {'Lalibella': 8, 'Gondar': 6, 'Bahirdar': 4},
    'Dire Dawa': {'Chiro': 8, 'Harar': 4},
    'Samara': {'Gobi Rasu': 10, 'Fanti Rasu': 7, 'Alamata': 11, 'Woldia': 8},
    'Robe': {'Liben': 11, 'Dodolla': 13, 'Goba': 18, 'Sof Oumer': 23},
    'Dilla': {'Hawassa': 3, 'Bulehora': 4},
    'Dawro': {'Bonga': 10, 'Wolaita Sodo': 6},
    'Tepi': {'Gore': 9, 'Bonga': 8, 'Mizan Teferi': 4},
    'Mizan Teferi': {'Tepi': 4, 'Bonga': 4},
    'Gambella': {'Gore': 5, 'Dambidollo': 4},
    'Arba Minchi': {'Wolaita Sodo': 5, 'Konso': 4, 'Basketo': 10},
    'Woldia': {'Dessie': 6, 'Lalibella': 7, 'Samara': 8, 'Alamata': 3},
    'Gondar': {'Azezo': 1, 'Humera': 9, 'Metema': 7, 'Debarke': 4, 'Debre Tabor': 6},
    'Metema': {'Azezo': 7, 'Gondar': 7},
    'Lalibella': {'Woldia': 7, 'Debre Tabor': 8, 'Sekota': 6},
    'Harar': {'Dire Dawa': 4, 'Babile': 2},
    'Fanti Rasu': {'Samara': 7, 'Kilbet Rasu': 6},
    'Alamata': {'Samara': 11, 'Woldia': 3, 'Mekelle': 5, 'Sekota': 6},
    'Liben': {'Robe': 11},
    'Goba': {'Robe': 18, 'Sof Oumer': 6, 'Babile': 28},
    'Sof Oumer': {'Goba': 6, 'Robe': 23, 'Gode': 23},
    'Bulehora': {'Dilla': 4, 'Yabello': 3},
    'Konso': {'Arba Minchi': 4, 'Yabello': 3},
    'Basketo': {'Arba Minchi': 10, 'Bench Maji': 5},
    'Humera': {'Shire': 8, 'Gondar': 9},
    'Debarke': {'Gondar': 4, 'Shire': 7},
    'Sekota': {'Alamata': 6, 'Mekelle': 9, 'Lalibella': 6},
    'Babile': {'Harar': 2, 'Jigjiga': 3, 'Goba': 28},
    'Kilbet Rasu': {'Fanti Rasu': 6},
    'Mekelle': {'Alamata': 5, 'Adigrat': 4, 'Adwa': 7, 'Sekota': 9},
    'Gode': {'Dollo': 17, 'Kebri Dehar': 5, 'Sof Oumer': 23},
    'Yabello': {'Bulehora': 3, 'Konso': 3, 'Moyale': 6},
    'Bench Maji': {'Basketo': 5},
    'Shire': {'Axum': 2, 'Humera': 8, 'Debarke': 7},
    'Jigjiga': {'Babile': 3, 'Dega Habur': 5},
    'Adigrat': {'Mekelle': 4, 'Adwa': 4},
    'Adwa': {'Mekelle': 7, 'Axum': 1, 'Adigrat': 4},
    'Dollo': {'Gode': 17, 'Moyale': 18},
    'Kebri Dehar': {'Gode': 5, 'Dega Habur': 6, 'Werdez': 6},
    'Moyale': {'Dollo': 18, 'Liben': 11, 'Yabello': 6},
    'Axum': {'Shire': 2, 'Adwa': 1},
    'Dega Habur': {'Jigjiga': 5, 'Kebri Dehar': 6},
    'Werdez': {'Kebri Dehar': 6}
}

# Defining a dictionary to represent the straight-line distances (SLD) from Moyale to other cities
# The keys are city names and the values are the straight-line distances from Moyale to those cities
sld_Moyale = {
    'Addis Ababa': 26,
    'Adama': 23,
    'Ambo': 31,
    'Debre Berhan': 31,
    'Debre Markos': 39,
    'Matahara': 26,
    'Asella': 22, 
    'Batu': 19,  
    'Wolkite': 25,  
    'Nekemte': 39, 
    'Debre Sina': 33,
    'Finote Selam': 42,
    'Awash': 27, 
    'Assasa': 18, 
    'Buta Jirra': 21, 
    'Shashamene': 16, 
    'Worabe': 22, 
    'Jimma': 33,
    'Hossana': 21,
    'Bedelle': 40, 
    'Gimbi': 43, 
    'Kemise': 40,  
    'Bahirdar': 48, 
    'Injibara': 44,
    'Chiro': 31,
    'Gobi Rasu': 32, 
    'Dodolla': 19, 
    'Hawassa': 15, 
    'Bonga': 33,
    'Wolaita Sodo': 17, 
    'Gore': 46,  
    'Dambidollo': 49,
    'Assosa': 51, 
    'Dessie': 44, 
    'Metekel': 59, 
    'Azezo': 55, 
    'Debre Tabor': 52,
    'Dire Dawa': 31, 
    'Samara': 42, 
    'Robe': 13, 
    'Dilla': 12, 
    'Dawro': 23, 
    'Tepi': 41,
    'Mizan Teferi': 37, 
    'Arba Minchi': 13, 
    'Gambella': 51,  
    'Woldia': 50,
    'Gondar': 56, 
    'Metema': 62, 
    'Lalibella': 57,
    'Harar': 35, 
    'Fanti Rasu': 49, 
    'Alamata': 53, 
    'Liben': 11, 
    'Goba': 40, 
    'Sof Oumer': 45, 
    'Bulehora': 8, 
    'Konso': 9, 
    'Basketo': 23,
    'Bench Maji': 28,
    'Humera': 65, 
    'Debarke': 60,
    'Sekota': 59,
    'Babile': 37, 
    'Kilbet Rasu': 55, 
    'Mekelle': 58, 
    'Gode': 35, 
    'Yabello': 6, 
    'Shire': 67, 
    'Adigrat': 62,
    'Adwa': 65, 
    'Dollo': 18,
    'Kebri Dehar': 40, 
    'Moyale': 0,
    'Axum': 66, 
    'Jigjiga': 40,
    'Dega Habur': 45, 
    'Werdez': 4
}

# Define a class for the Priority Queue used in the A* search algorithm
class Frontier_PQ():
    # Initialize the priority queue with the start node and its initial cost
    def __init__(self, start, cost=0):
        self.start = start
        self.cost = cost
        self.states = {start: cost}  # Dictionary to keep track of the explored nodes and their costs
        self.q = [[cost, start]]  # List to act as the priority queue with nodes to be explored

    # Method to add a state and its cost to the priority queue
    def add(self, state, cost):
        self.states[state] = cost
        heapq.heappush(self.q, [cost, state])

    # Method to pop the state with the lowest cost from the priority queue
    def pop(self):
        return heapq.heappop(self.q)

    # Method to replace the cost of a state in the priority queue
    def replace(self, state, cost):
        self.states[state] = cost
        for i, tup in enumerate(self.q):
            if tup[1] == state:
                self.q[i][0] = cost
                break  # Exit the loop once the state is found and updated

# Define a heuristic function for A* that uses the straight-line distances to Moyale
def heuristic_sld_Moyale(state):
    # Return the straight-line distance from the given state to Moyale
    return sld_Moyale[state]

# Test the heuristic function by printing the heuristic value for Moyale
print(heuristic_sld_Moyale("Moyale"))  # Expected output: 0


# Define the A* search function
def astar_search(start, goal, state_graph, heuristic, return_cost=False, return_nexp=False):
    # Initialize the priority queue with the start node
    frontier = Frontier_PQ(start)
    # Set to keep track of visited nodes
    visited = set()
    # Dictionary to keep track of the previous node for each visited node
    prev = {start: None}

    # Main loop to explore nodes until the goal is reached or the frontier is empty
    while frontier.q:
        # Pop the node with the lowest cost from the priority queue
        cost, curr = frontier.pop()
        # Add the current node to the visited set
        visited.add(curr)

        # If the current node is the goal, construct the path and return the results
        if curr == goal:
            p = path(prev, curr)
            if not return_nexp:
                # Return the path and cost if return_cost is True, otherwise return only the path
                return (p, pathcost(p, state_graph)) if return_cost else p
            else:
                # Return the path, cost, and number of explored nodes if return_nexp is True
                return (p, pathcost(p, state_graph), len(visited)) if return_cost else (p, len(visited))

        # Loop through adjacent nodes
        for adj in state_graph[curr]:
            if adj not in visited:
                # Calculate the new cost considering the heuristic function
                new_cost = cost + state_graph[curr][adj] + heuristic(adj) - heuristic(curr)

                # If the adjacent node is not in the frontier, add it
                if adj not in frontier.states:
                    prev[adj] = curr
                    frontier.add(adj, new_cost)
                # If the adjacent node is in the frontier but the new cost is lower, replace the cost
                elif frontier.states[adj] > new_cost:
                    prev[adj] = curr
                    frontier.replace(adj, new_cost)

# Execute the A* search algorithm starting from "Addis Ababa" to "Moyale"
ret = astar_search("Addis Ababa", "Moyale", map_distances, heuristic_sld_Moyale, True, True)

# Print the optimal path found by the A* search algorithm
print("The optimal path using A*:", ret[0])

# Print the cost of the optimal path found by the A* search algorithm
print("The optimal path cost using A*:", ret[1])

# Print the number of states expanded during the A* search
print("The number of states expanded during search using A*:", ret[2])

