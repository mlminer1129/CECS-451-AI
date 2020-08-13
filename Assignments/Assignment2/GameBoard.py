'''
Converts a standard gameboard to a graph file
Skeleton code (c) 2020 Arjang Fahim

Salvador Gallardo
010098489

John Miner
003047679

CECS 451
'''

#import what we need
import numpy as np
import Graph as g
import copy
from numpy.core.numeric import Infinity


#Creating GameBoard class that will take in one .lay file
class GameBoard(object):
    
    def __init__(self, maze_file):
        #Initialize blank GameBoard
        self.graph = g.Graph()
        
        #open file for reading 
        self.file = open(maze_file, 'r')
        rows = 0
        lines = []
        #Iterate and build rows/columns
        for line in self.file:
            lines.append(line)
            rows = rows + 1
            columns = (len(line))
            #print(line)
        self.n = columns 
        self.m = rows
        #create a maxtrix version of the txt file
        self.fileMatrix = [list(line) for line in lines]
        
        #calling methods on self
        self.MazeMatrix_Build()
        self.GoalNode()
        self.StartNode()
        
        startIndex = self.start[0]* self.n + self.start[1] 
        goalIndex = self.goal[0]* self.n + self.goal[1]
        
        print ('start:' , startIndex)
        print ('goal:', goalIndex, '\n')
    
    def solve(self):
        
        self.rebuild_path()
        self.printSolvedMaze()
        

    # returns goal node position
    def GoalNode(self):
        #initialize x and y as empty set in case there is no start or end included
        x = []
        y = []
        #Iterate through to find the 'P' starting point
        for i in range(len(self.fileMatrix)):
            for j in range(len(self.fileMatrix[i])):
                if self.fileMatrix[i][j] == '.':
                    x = i
                    y = j
        #assign goal node if there is one else return the empty set ([],[])        
        self.goal = (x, y)
        return self.goal

    # returns starting node position    
    def StartNode(self):
        for i in range(len(self.fileMatrix)):
            for j in range(len(self.fileMatrix[i])):
                if self.fileMatrix[i][j] == 'P':
                    x = i
                    y = j
        self.start = (x, y)
        return self.start

    def MazeMatrix_Build(self):
        adjecencyDimention = self.m*self.n
        self.matrix = np.zeros((adjecencyDimention, adjecencyDimention))
        #print(self.matrix)
        validSpace = [ ' ', '.', 'P']
        #iterate through the file
        #print(self.fileMatrix)
        for i in range(len(self.fileMatrix)):
            for j in range(len(self.fileMatrix[i])):
                if self.fileMatrix[i][j] in validSpace:
                    #declare variables for neighbor spaces
                    upRow = i - 1
                    downRow = i + 1
                    rightCol = j + 1
                    leftCol = j - 1
                    
                    #find if the up, down, right and left neighbors are valid spots
                    
                    adjIndex = i * self.n + j
                    
                    self.graph.add_vertex(adjIndex)
                    
                    #Check if can move up
                    if (upRow > -1):
                        if (self.fileMatrix[upRow][j] in validSpace):
                            #print("can move up")
                            adjUp = adjIndex - self.n
                            if (adjUp < adjecencyDimention and adjUp >-1):
                                self.graph.add_edge(adjIndex, adjUp)
                                
                    #Check if can move down
                    if(downRow < adjecencyDimention):    
                        if (self.fileMatrix[downRow][j] in validSpace):
                            #print("can move down")
                            adjDown = adjIndex + self.n
                            if (adjDown < adjecencyDimention and adjDown >-1):
                                self.graph.add_edge(adjIndex, adjDown)
                                
                    #Check if can move right
                    if(rightCol < adjecencyDimention):
                        if (self.fileMatrix[i][rightCol] in validSpace):
                            #print("can move right ")
                            adjRight = adjIndex + 1
                            if (adjRight < adjecencyDimention and adjRight >-1):
                                self.graph.add_edge(adjIndex, adjRight)    
                    
                    #Check if can move left
                    if(leftCol > -1):    
                        if (self.fileMatrix[i][leftCol] in validSpace):
                            #print("can move left ")
                            adjLeft = adjIndex - 1
                            if (adjLeft < adjecencyDimention and adjLeft >-1):
                                self.graph.add_edge(adjIndex, adjLeft)
        
        #for line in self.fileMatrix:
            #print(line)
     
    #breath first search algorithm   
    def bfs(self):
        q = [] #FIFO queue
        self.visited = [] #list of visited nodes
        self.parent = {}
        
        #compute index number according to row and column
        startIndex = self.start[0]* self.n + self.start[1] 
        goalIndex = self.goal[0]* self.n + self.goal[1]
        
        self.visited.append(startIndex) #mark the start as visited
       
        #grab the neighbors of the start node
        v = self.graph.get_vertex(startIndex)
        neighbors = v.get_connections()
        
        #iterate through neighbors and add the start as parent node
        for n in neighbors:
            q.append(n.get_id())
            self.parent[n.get_id()] = startIndex
        
        #set variable max to track largest frontier size    
        self.max = len(q)
            
        while len(q) !=  0:
            first = q.pop(0) #grab the first item on the queue
            node = self.graph.get_vertex(first) #grab the handle to the vertex object
            self.visited.append(node.get_id()) #mark the node as visited
            if node.get_id() == goalIndex:   #if goal found exit loop
                break
            else:
                neighbors = node.get_connections() #grab neighbors of current node
                for n in neighbors:
                    if n.get_id() not in self.visited:
                        self.parent[n.get_id()] = node.get_id() #assign a parent to the node
                        q.append(n.get_id())                    #add the node to the queue 
                        if len(q) > self.max:
                            self.max = len(q)
                            
                
        #self.graph.graph_summary()
        print ("\nBFS:")
        self.solve()
        self.printStats()

    def dfs(self):
        s = []
        self.visited = []
        self.parent = {}
        
        start = self.start[0]* self.n + self.start[1]
        goal = self.goal[0]* self.n + self.goal[1]
        
        node = self.graph.get_vertex(start)
        #print(s)
        neighbors = node.get_connections()
        #print(neighbors)
        
        for n in neighbors:
            s.append(n.get_id())
            self.parent[n.get_id()] = start
        #print(s)
        self.max = len(s)
        while len(s) != 0:
            pop = s.pop()
            node = self.graph.get_vertex(pop)
            self.visited.append(node.get_id())
            if  node.get_id() == goal:
                print('\nDFS:')
                self.solve()
                #continue running till stack is empty
                
            else:
                
                neighbors = node.get_connections()
                for n in neighbors:
                    if n.get_id() not in self.visited:
                        self.parent[n.get_id()] = node.get_id()
                        s.append(n.get_id())
                        if len(s) > self.max:
                            self.max = len(s)
            #self.visited.remove(node.get_id())
        #print(s) #fringe cases
        
        #self.solve()
        self.printStats()
        
        
        
        
                

    #rebuild path using the parent nodes
    def rebuild_path(self):
        startIndex = self.start[0]* self.n + self.start[1]
        
        #grab the final node visited
        location = self.visited[len(self.visited)-1]
        
        #add the node to the path
        self.path = [location]
        
        #search for the parent of each node backwards to rebuild path
        while location != startIndex:
            location = self.parent[location]
            self.path.append(location)
          
        #reverse path to fix the order   
        self.path.reverse()  
        
    def aStar(self):
        
        #calc heuristics
        cost = {}           #dictionary for saving the cost from start to vertex
        heuristic = {}      #dictionary for saving the h(n) values 
        
        bestPath = []       #list to save the optimal route
        
        #iterate through the vertecies and calculate heuristics
        verts = self.graph.get_verticies()
        for v in verts:
            x = int(v / self.n)       #calculate x index
            y = int(v - x*self.n)     #calculate y index
            distance = abs(x - self.goal[0]) + abs(y - self.goal[1])
            heuristic[v] = distance
            cost[v] = Infinity
        
        openList = [] #list of vertecies to explore
        self.visited = [] #list of visited nodes
        self.parent = {}  #dictionary for parent node for path rebuild
        
        #compute index number according to row and column
        startIndex = self.start[0]* self.n + self.start[1] 
        goalIndex = self.goal[0]* self.n + self.goal[1]
        
        
        self.visited.append(startIndex) #mark the start as visited
       
        currentCost = 0             #cost to get to vertex
        cost[startIndex] = currentCost
        #grab the neighbors of the start node
        v = self.graph.get_vertex(startIndex)
        neighbors = v.get_connections()
        
        #iterate through neighbors and add the start as parent node
        currentNode = v
        f = Infinity            #set f function cost to arbritrary high value
        currentCost = currentCost +1
        #iterate through the neighbors
        for n in neighbors:
            openList.append(n.get_id())   #add to queue 
            self.parent[n.get_id()] = startIndex  #set the parent
            cost[n.get_id()] = currentCost        #set the cost
            #caculate f(n) = g(n) + h(n) 
            fN = cost[n.get_id()] + heuristic[n.get_id()]
            #find choose the best node to start
            if fN < f:
                f = fN
                currentNode = n
        
        self.max = len(openList) #set max to the frontier size
        
        #begin a* search
        while len(openList) !=  0:
            openList.remove(currentNode.get_id())
            self.visited.append(currentNode.get_id())
            
            neighbors = currentNode.get_connections()
            currentCost = cost[currentNode.get_id()] 
            
            if currentNode.get_id() == goalIndex:
                self.rebuild_path() # calculate path
                #if this is the first path found or this path is better than previous
                if len(bestPath) == 0 or len(self.path) < len(bestPath):
                    bestPath = copy.deepcopy(self.path)         #save a deep copy of the current path
            
            #iterate through all neighbors
            for n in neighbors:
                prevCost = cost[n.get_id()] + heuristic[n.get_id()]  #calculate previous cost to node 
                newCost = currentCost + heuristic[n.get_id()]       #calculate new cost to node
                
                #if new path is better than old , update values
                if newCost < prevCost:
                    openList.append(n.get_id())
                    self.parent[n.get_id()] = currentNode.get_id()
                    cost[n.get_id()] = currentCost + 1
             
            #update max frontier size if length has surpassed previous max       
            if self.max < len(openList):
                self.max = len(openList)        
            #iterate through the queue and find best choice
            for n in openList:
                lowest = Infinity
                if cost[n] + heuristic[n] < lowest:
                    currentNode = self.graph.get_vertex(n)
        

        print ("\nA*")
        #load the best path found
        self.path = bestPath   
        self.printSolvedMaze()
        self.printStats()
     
    #print the maze showing path taken   
    def printSolvedMaze(self):
        line = ''
        for i in range(len(self.fileMatrix)):
            for j in range(len(self.fileMatrix[i])):
                locationIndex = i* self.n + j
                if locationIndex in self.path:
                    line = line + '.'
                else:
                    line = line + self.fileMatrix[i][j]
            
        print(line)
        
        
    def printStats(self):
        #print("Size of graph: " , len(self.graph.get_verticies()))
        print ('Path: ', self.path)
        print("Path cost: ", len(self.path))
        print("Nodes expanded: ", len(self.visited))
        print("Max frontier: ", self.max)
        
    def SaveMatrix(self, path):
        #Write new file to be written to
        file = open(path, 'w')
        #Iterate through file
        for line in self.matrix:
            #assign '' to data to concatenate later
            data = ''
            #iterate through each individual cell in each line and write to file
            for cell in line:
                data = data + ' ' + str(int(cell)) + '\t'
            data = data + '\n'
            file.write(str(data))
    
    def PlotGraph(self):
        # Don't worry about it for now, we may use it foe the next assignment
        self.graph.graph_summary()
    
    def PlotSolution(self, solution, path):
        # Don't worry about it for now, we may use it foe the next assignment
        pass





#------------------------[End of class Gameboard]----------------------------------------    


        

if __name__ == '__main__':
    
    #pull in Maze
    #game = GameBoard('smallMaze.lay')
    #solution : 77,78,79,101,123,122,144,166,165,164,186,185,184,183,182,181,180,179,178,177 (size 20)
    
    game = GameBoard('smallMaze.lay')
    
    game.bfs()
    game.dfs()
    #game.aStar()
    #game.PlotGraph()

    
    
    
    
    
    