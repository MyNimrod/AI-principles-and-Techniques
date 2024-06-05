# AI Principles and Techniques Course Project

## Overview

This repository contains the project for the AI Principles and Techniques course. The project focuses on solving the Traveling Ethiopia search problem using various search algorithms. The project is implemented in a Jupyter notebook, which can be found [here](https://github.com/MyNimrod/AI-principles-and-Techniques/blob/main/Course_Project/Travelling_Ethiopia.ipynb).

## Project Structure

The project is organized into four main questions, each addressing different aspects of search algorithms and their applications to the Traveling Ethiopia search problem.

## Questions

### 1. State Space Graph Conversion and Search Strategies

#### 1.1 Convert Figure 1

Consider Figure 1 (A generic state space graph for traveling Ethiopia search problem) to solve the following problems.

- Convert Figure 1, a state space graph for traveling Ethiopia search problem, into some sort of manageable data structure such as stack or queue.

#### 1.2 Implement Search Strategies

- Write a class that takes the converted state space graph, initial state, goal state, and a search strategy and returns the corresponding solution/path according to the given strategy.
- Please consider only breadth-first search and depth-first search strategies for this question.

### 2. State Space Graph with Backward Cost

#### 2.1 Convert Figure 2

Given Figure 2, a state space graph with backward cost for the traveling Ethiopia search problem.

- Convert Figure 2 into some sort of manageable data structure such as stack or queue.

#### 2.2 Uniform Cost Search

- Assuming “Addis Ababa” as an initial state, write a program that uses uniform cost search to generate a path to “Lalibela”.

#### 2.3 Customized Uniform Cost Search

- Given “Addis Ababa” as an initial state and “Axum”, “Gondar”, “Lalibela”, Babile, “Jimma”, “Bale”, “Sof Oumer”, and “Arba Minch” as goal states (in no specific order), write a customized uniform cost search algorithm to generate a path that lets a visitor visit all those goal states preserving the local optimum.

### 3. State Space Graph with Heuristic and Backward Cost

Given Figure 3, a state space graph with heuristic and backward cost.

- Write a class that uses A star search to generate a path from the initial state “Addis Ababa” to the goal state “Moyale”.

### 4. Adversarial Search

Assume an adversary joins the Traveling Ethiopia Search Problem as shown in Figure 4.

- The goal of the agent would be to reach a state where it gains good quality of Coffee.
- Write a class that shows how the MiniMax search algorithm directs an agent to the best achievable destination.

## Figures

#### 1. Figure 1 Traveling Ethiopia

![Figure 1](https://github.com/MyNimrod/AI-principles-and-Techniques/blob/main/Course_Project/Figure%201%20Traveling%20Ethiopia.png)

#### 2. Figure 2 Traveling Ethiopia

![Figure 2](https://github.com/MyNimrod/AI-principles-and-Techniques/blob/main/Course_Project/Figure%202%20Traveling%20Ethiopia.jpg)

#### 3. Figure 3 Traveling Ethiopia

![Figure 3](https://github.com/MyNimrod/AI-principles-and-Techniques/blob/main/Course_Project/Figure%203%20Traveling%20Ethiopia.jpg)

#### 4. Figure 4 Adversarial Traveling Ethiopia
![Figure 4](https://github.com/MyNimrod/AI-principles-and-Techniques/blob/main/Course_Project/Figure%204%20Adversary%20Traveling%20Ethiopia.jpg)

(Note: The figures are available in the repository.)

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/MyNimrod/AI-principles-and-Techniques.git
    ```
2. Navigate to the project directory:
    ```bash
    cd AI-principles-and-Techniques/Course_Project
    ```
3. Open the Jupyter notebook:
    ```bash
    jupyter notebook Travelling_Ethiopia.ipynb
    ```
4. Follow the instructions in the notebook to run the code for each question.

## Requirements

- Jupyter Notebook
- Python 3.x
- Required Python libraries (specified in the notebook)

## Acknowledgements

This project is part of the AI Principles and Techniques course.

