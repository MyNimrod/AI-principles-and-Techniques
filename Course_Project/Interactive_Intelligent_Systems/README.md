# Interactive Intelligent Systems Project 

![Figure 5](https://github.com/MyNimrod/AI-principles-and-Techniques/blob/main/Course_Project/Interactive_Intelligent_Systems/Figure%205%20Traveling%20Ethiopia.png)

5. Interactive Intelligent systems: Figure 5 is a relaxed state space graph for traveling Ethiopia search problem.

5.1 Design a three-wheel functional robot using Gazebo. Let it have a working physics engine and sensors such as Proximity sensor, gyroscope, RGB camera, ...

5.2 Create a .world file with all the states in Figure 5 using a Cartesian coordinate system.

5.3 Write a ROS based class that use any uninformed search strategy and generate a path for the robot to travel from any given initial state in Figure 5 to the given goal state.


This repository contains the implementation for the Interactive Intelligent Systems project focused on the traveling Ethiopia search problem. Below are instructions for setting up and running the components of the project.

## 5.1 Designing a Three-Wheel Functional Robot using Gazebo

### Prerequisites

Ensure you have Ubuntu 20.04 installed.

### Installing Necessary Tools and Libraries

1. **ROS Melodic**: Follow the official ROS installation guide for Melodic [here](http://wiki.ros.org/melodic/Installation/Ubuntu).
   
2. **Gazebo**: Install Gazebo using the command:

   sudo apt-get install gazebo9 libgazebo9-dev

3. **Clone the Repository**

	git clone https://github.com/MyNimrod/AI-principles-and-Techniques.git

### Running the Robot Simulation

Navigate to the my_robot_description folder and launch the robot in Gazebo:

	roslaunch my_robot_description robot.launch

### Robot Features

- Physics Engine: Utilizes Gazebo's physics engine.
- Sensors: Includes proximity sensor, gyroscope, RGB camera.

## 5.2 Creating a .world File with Ethiopian States

### Installing Gazebo

Ensure Gazebo is installed as per the instructions above.

### Coordinates Calculation for Ethiopian States

Coordinates for Ethiopian states can be derived using a Cartesian coordinate system. Ensure these are accurately placed in your .world file.
The .world file is located in:

	/AI-principles-and-Techniques/Course_Project/Interactive_Intelligent_Systems/gazebo/ethiopian_town.world
	
### Running the .world File

Navigate to the gazebo directory and launch the Ethiopian towns world file:

	gazebo ethiopian_towns.world

##  5.3 Implementing Uninformed Search Strategy with ROS

### Setting Up the Environment

Ensure you have Jupyter Notebook installed.

### Running the BFS Implementation

Open the uninformed_strategy.ipynb notebook located in the AI-principles-and-Techniques/Course_Project/Interactive_Intelligent_systems/ directory and 
execute the cells to generate a path for the robot from any initial state to the goal state using Breadth-First Search (BFS).

	