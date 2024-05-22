# Project 1

#### Link to Project is [Project 1](https://inst.eecs.berkeley.edu/~cs188/sp23/projects/proj1/#q1-3-pts-finding-a-fixed-food-dot-using-depth-first-search)

## Q1: Finding a Fixed Food Dot using Depth First Search


	Your code should quickly find a solution for:
		python pacman.py -l tinyMaze -p SearchAgent
		python pacman.py -l mediumMaze -p SearchAgent
		python pacman.py -l bigMaze -z .5 -p SearchAgent
	
## Q2: Breadth First Search

Implement the breadth-first search (BFS) algorithm in the breadthFirstSearch function in search.py. Again, write a graph search algorithm that avoids expanding any already visited states. Test your code the same way you did for depth-first search.

## Q3: Varying the Cost Function

Implement the uniform-cost graph search algorithm in the uniformCostSearch function in search.py. We encourage you to look through util.py for some data structures that may be useful in your implementation. You should now observe successful behavior in all three of the following layouts, where the agents below are all UCS agents that differ only in the cost function they use.
	
	python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
	python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
	python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

## Q4: A\* search

Implement A\* graph search in the empty function aStarSearch in search.py. A\* takes a heuristic function as an argument. Heuristics take two arguments: a state in the search problem (the main argument), and the problem itself (for reference information). The nullHeuristic heuristic function in search.py is a trivial example.

You can test your A\* implementation on the original problem of finding a path through a maze to a fixed position using the Manhattan distance heuristic (implemented already as manhattanHeuristic in searchAgents.py).

	python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

## Q5: Finding All the Corners

In corner mazes, there are four dots, one in each corner. Our new search problem is to find the shortest path through the maze that touches all four corners (whether the maze actually has food there or not). Note that for some mazes like tinyCorners, the shortest path does not always go to the closest food first! Hint: the shortest path through tinyCorners takes 28 steps.

Note: Make sure to complete Question 2 before working on Question 5, because Question 5 builds upon your answer for Question 2.

Implement the CornersProblem search problem in searchAgents.py. You will need to choose a state representation that encodes all the information necessary to detect whether all four corners have been reached. Now, your search agent should solve:

	python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
	python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
