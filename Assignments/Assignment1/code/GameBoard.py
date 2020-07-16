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
import pandas as pd
import numpy as np
#Creating GameBoard class that will take in one .lay file
class GameBoard( object):
    #Initialize blank GameBoard
    def __init__(self, maze_file):
        
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
    

    # returns goal node position
    def GoalNode(self):
        #initialize x and y as empty set in case there is no start or end included
        x = []
        y = []
        #Iterate through to find the 'P' starting point
        for i in range(len(self.fileMatrix)):
            for j in range(len(self.fileMatrix[i])):
                if self.fileMatrix[i][j] == 'P':
                    x = i
                    y = j
        #assign goal node if there is one else return the empty set ([],[])
        self.goal = (x, y)
        return self.goal

    # returns starting node position    
    def StartNode(self):
        #initialize x and y as empty set in case there is no start or end included
        x = []
        y = []
        #Iterate through to find the '.' starting point
        for i in range(len(self.fileMatrix)):
            for j in range(len(self.fileMatrix[i])):
                if self.fileMatrix[i][j] == '.':
                    x = i
                    y = j
        #assign start node if there is one else return the empty set ([],[])
        self.start = (x, y)
        return self.start

    def MazeMatrix_Build(self):
        adjecencyDimention = self.m*self.n
        self.matrix = np.zeros((adjecencyDimention, adjecencyDimention))
        #print(self.matrix)
        print()
        #iterate through the file
        #print(self.fileMatrix)
        for i in range(len(self.fileMatrix)):
            for j in range(len(self.fileMatrix[i])):
                if self.fileMatrix[i][j] == ' ':
                    #declare variables for neighbor spaces
                    upRow = i - 1
                    downRow = i + 1
                    rightCol = j + 1
                    leftCol = j - 1
                    
                    #find if the up, down, right and left neighbors are valid spots
                    
                    adjIndex = i * self.n + j
                    
                    
                    #Check if can move up
                    if (upRow > -1):
                        if (self.fileMatrix[upRow][j] == ' '):
                            #print("can move up")
                            adjUp = adjIndex - adjecencyDimention
                            if (adjUp < 220 and adjUp >-1):
                                self.matrix[adjIndex][adjUp] = 1
                    #Check if can move down
                    if(downRow < 220):    
                        if (self.fileMatrix[downRow][j] == ' '):
                            #self.matrix[adjIndex][adjIndex + self.n] = 1
                            adjDown = adjIndex + adjecencyDimention
                            if (adjDown < 220 and adjDown >-1):
                                self.matrix[adjIndex][adjDown] = 1
                    #Check if can move right
                    if(rightCol < 220):
                        if (self.fileMatrix[i][rightCol] == ' '):
                            #print("can move right ")
                            adjRight = adjIndex + 1
                            if (adjRight < 220 and adjRight >-1):
                                self.matrix[adjIndex][adjRight] = 1    
                    #Check if can move left
                    if(leftCol > -1):    
                        if (self.fileMatrix[i][leftCol] == ' '):
                            #print("can move left ")
                            adjLeft = adjIndex - 1
                            if (adjLeft < 220 and adjLeft >-1):
                                self.matrix[adjIndex][adjLeft] = 1
                                    
        
        #for line in self.fileMatrix:
            #print(line)
        
    
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

    def PlotSolution(self, solution, path):
        # Don't worry about it for now, we may use it foe the next assignment
        pass




#------------------------[End of class Gameboard]----------------------------------------    


        

if __name__ == '__main__':
    #pull in Maze
    game = GameBoard('smallMaze.lay')
    #Save Adjacency matrix
    game.SaveMatrix('output.txt')
    #Print Start Node
    print("Start: ", game.StartNode())
    #Print Goal Node
    print("Goal: ", game.GoalNode())
    
    
    
    
    
    