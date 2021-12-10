from pyamaze import maze, agent, COLOR, textLabel
# imports maze and agent classes from pymaze module
from queue import PriorityQueue

from pyamaze.pyamaze import textLabel


def h(cell1, cell2): # Heuristic function to calculate the manhattan distance bw 2 cells
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1-x2) + abs(y1-y2)

def aStar(m, goal=(1, 1), start=None): # a Star algorithm that takes a maze as an input
    # CHANGED - Created a default argument for goal node

    if start is None:
        start = (m.rows, m.cols) # Defining the start node - last element is the start node 

    g_score = {cell:float('inf') for cell in m.grid} # Create a dict with keys as the cell coordinates and value as infinity
    # Dictionary Comprehension - A dictionary comprehension takes the form {key: value for (key, value) in iterable}
    # Creating a dictionary for the g-score values
    g_score[start] = 0 # The g-score of the start cell is 0
    f_score = {cell:float('inf') for cell in m.grid}
    f_score[start] = h(start, goal) # The f-score of start cell is the heuristic cost for start cell and goal node

    open = PriorityQueue() # Creating a priority queue
    
    # In A* search - F = G + H 
    # where G is the actual cost, H is the heuristic cost and F is the parameter used to find the least cost 

    open.put((h(start, goal), h(start, goal), start))
    # Values in priority queue - (f_cost=heuristic_cost+g_cost(=0), heuristic_cost, cell_value)

    aPath = {} 
    # Declaring an empty dictionary to store the path in the form aPath[childCell] = currCell

    while not open.empty():
        # Pick the value from the queue 

        currCell = open.get()[2] 
        # This gives the location of the cell as this will return the 3rd element in the tuple in the queue
        # The get command dequeues the highest priority elements from the queue.

        if currCell == goal:
            break
            # If current cell is the goal cell, stop the loop
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True: # Check if the path in the direction 'd' is open 
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                    # If direction is east, the cell will be on the right and will have the location currCell[0] (same row)
                    # and currCell[1]+1 (next column)
                if d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                    # On the left column and on the same row
                if d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                if d == 'S':
                    childCell = (currCell[0]+1, currCell[1])

                temp_g_score = g_score[currCell]+1 
                # New g-score will be the g score of the current cell +1
                temp_f_score = temp_g_score + h(childCell, goal)
                # New f-score will be the sum of the new g score and the h-score of the childCell and goal

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, h(childCell, goal), childCell))
                    # If new f-score is less than the previous f-score, update the g-score and the f-score 
                    # then, put the updated values (f-score, h-score, location) for the childCell in a tuple and add it to the queue  
                    aPath[childCell] = currCell

    # aPath will give the reverse path (i.e., by pointing from childCell to currCell), hence we need a fwdPath
    fwdPath = {}
    cell = goal # take goal node as a starting point for the loop/path reverse loop
    while cell != start: # Do this until we do not reach the start node
        fwdPath[aPath[cell]] = cell # This swaps the key, value pairs
        # Eg., Supposing aPath[cell]=k, then fwdPath[k]=cell will be added to the dictionary
        cell = aPath[cell] # Go to the next node, i.e, set up the current value as the next key
    
    return fwdPath # returns the fwdPath 

if __name__ == "__main__":

    m = maze(100, 100)
    m.CreateMaze() # Use CreateMaze(a, b) to create a maze that has (a, b) as a goal node

    #print(m.rows, m.cols)

    #print(m.maze_map) 
    # maze_map is a dictionary keys are the cells, value is another dictionary with east, west, north and south as keys and values as 0 or
    # 1 indicating whether a path is open in that direction or not

    #print(m.grid) # List of all values inside the maze

    path = aStar(m)

    # We need to move an agent on this calculated path, import agent class from pyamaze, by default the agent is placed on the start cell
    a = agent(m, footprints=True, filled=True) # Set footprints=True 
    m.tracePath({a:path}, delay=0) # Input dict with key as agent and path as value
    l = textLabel(m, "A Star Path Length: ", len(path)+1)

    m.run() # Displays the maze