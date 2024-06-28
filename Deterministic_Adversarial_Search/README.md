```markdown
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
- [Future Work](#future-work)
- [References](#references)

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

