# AI Game Algorithms

## Overview

This repository contains implementations of various AI algorithms for game playing, including:
Link to question: https://docs.google.com/document/d/1NwwO8RGdrSL322znKc0PdAkDNq7SuwCMbPu0tlrfWMI/edit
1. Minimax algorithm for Tic-Tac-Toe.
2. Extended Minimax algorithm with heuristic evaluation functions.
3. Minimax algorithm with Alpha-Beta Pruning for Chess.

Additionally, it includes a comprehensive lab report detailing the methodologies, experimental setup, results, and analysis.

## Table of Contents

- [Installation](#installation)
- [How to Play](#how-to-play)
  - [Tic-Tac-Toe](#tic-tac-toe)
  - [Chess](#chess)
- [Lab Report](#lab-report)

## Installation

Clone the repository:

	git clone https://github.com/MyNimrod/AI-principles-and-Techniques.git
	cd Deterministic_Adversarial_Search

Install the required dependencies:

	pip install -r requirements.txt

## How to Play

### Tic-Tac-Toe

To play the Tic-Tac-Toe game using the Minimax algorithm:

1. Run the game:

	python play_tic_tac_toe.py

2. To Run the heuristic algorithm:

	python play_tic_tac.py
	
### Chess

Implementing the Minimax algorithm with alpha-beta pruning for the game of chess is a complex task due to the vast number of possible board states. However, we can provide a simplified implementation that focuses on the core idea of alpha-beta pruning within the Minimax algorithm. This example assumes you have a basic chess engine capable of generating moves and evaluating board states.

To implement alpha-beta pruning, we need:

A function to generate all legal moves for a given board state.
A function to apply a move to the board and undo it.
A heuristic evaluation function for the board state.
The Minimax algorithm with alpha-beta pruning.

To play the Chess game using the Minimax algorithm with Alpha-Beta Pruning:

1. First, install the python-chess library:

	pip install python-chess

2. Run the game:

	python play_chess.py

3. The game will start with the user playing as White and the AI playing as Black. Make your moves by entering standard chess notation (e.g., e2e4).

### Lab Report

The repository includes a detailed lab report covering the following sections:

1. Introduction: Overview of the lab assignment, objectives, and goals.
2. Problem Statement: Definition of the problem and constraints.
3. Background / Literature Review: Relevant information and context.
4. Methodology or Algorithm Description: Explanation of the algorithms used, including pseudocode.
5. Implementation Details: Technical details of the implementation.
6. Experimental Setup: Datasets, test cases, and experiments conducted.
7. Results: Findings of the experiments with tables and charts.
8. Analysis: Interpretation of results and performance analysis.
9. Discussion: Implications of results and any unexpected outcomes.
10. Conclusion: Summary of main findings and significance.
11. Future Work: Suggestions for enhancements and further research.
12. References: List of external sources and citations.
13. Appendix: Additional supporting materials.

The full lab report is available in the Lab_Report.md file.




