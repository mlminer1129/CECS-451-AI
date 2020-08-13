'''
Salvador Gallardo
ID : 010098489

CECS 451 AI
9 July 2020
'''

#this class is a graph data structs composed of vertex objects
class Graph(object):
    
    #initizlize a dictionary and count of vertex
    def __init__(self):
        self.vertecies = {}
        self.num_vertecies = 0
        
    
    #add a vertex to the graph
    def add_vertex(self, vertex):
        new_v = Vertex(vertex)
        self.vertecies[vertex] = new_v
        self.num_vertecies = self.num_vertecies +1
    
    
    
    #grab a vertex object to a given vertex id    
    def get_vertex(self, vertex):
        if vertex in self.vertecies:
            return self.vertecies[vertex]
        else:
            return None
        
    #add and edge to a graph with a weight
    def add_edge(self, start, end, weight = 1):
        if start not in self.vertecies:
            self.add_vertex(start)
        if end not in self.vertecies:
            self.add_vertex(end)
        self.vertecies[start].add_neighbor(self.vertecies[end], weight)
    
    #get all the nodes of the graph
    def get_verticies(self):
        return self.vertecies.keys()
    
    #print all the edges and weights 
    def graph_summary(self):
        for v in self.vertecies.values():
            v_id = v.get_id()
            for w in v.get_connections():
                w_id = w.get_id()
                if v.get_weight(w) > 1:
                    print(v_id, ' -> ',  w_id, v.get_weight(w))
                else:
                    print(v_id, ' -> ', w_id)
        print('\n')
        
#this class is for storing a node with neighbors 
class Vertex:
    
    
    
    #crete a vertex with id and initialize dict of adjecent
    def __init__(self, node):
        self.id = node
        self.adjecent = {}
        
    #get the keys of all the neigbors to the node
    def get_connections(self):
        return self.adjecent.keys()
    
    #add a neighbor to the vertex
    def add_neighbor(self, neighbor, weight):
        self.adjecent[neighbor] = weight

    #get the id of the node
    def get_id(self):
        return self.id
    
    #get the wieght to a specific neighbor 
    def get_weight(self, neighbor):
        return self.adjecent[neighbor]
    


''' 
#testing the graph and vertex class

#create a graph object
g = Graph()
#add vertecies to the graph
g.add_vertex('S')
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
#add edges to the graph
g.add_edge('S', 'A')
g.add_edge('S', 'C')
g.add_edge('A', 'C')
g.add_edge('A', 'B')
g.add_edge('C', 'A')
g.add_edge('C', 'B')
g.add_edge('C', 'D')

#print the graph
g.graph_summary()
'''
