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


