# AI Project: Game State Analysis

### CS1108 (Artificial Intelligence and Machine Learning)

In this project we have used A*, Minimax, BFS and DFS on various games (Maze Traversal and Tic-Tac-Toe) to analyze their states and suggest the next step for the best possible result.

For this purpose, we have used A*, BFS and DFS on a maze game and implemented it in Python using the `pyamaze` package and used the Minimax algorithm to create a Tic-Tac-Toe game 
to be played against moves calculated by the algorithm.

In the file Comparison.py we have solved the maze using all the algorithms and calculated the time taken by all the algorithms to solve the same maze.

We have found that up until mazes of size 10 x 10, all algorithms have almost similar solving times. For mazes of higer order, A* becomes considerably faster than BFS and DFS. 
This is as expected as A* is an informed search algorithm and BFS and DFS are not. 

\
*References*

Pyamaze: https://towardsdatascience.com/a-python-module-for-maze-search-algorithms-64e7d1297c96
