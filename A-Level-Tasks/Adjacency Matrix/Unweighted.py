class Graph():
    def __init__(self):
        self.Data = []
        self.temp = []
        self.Nodes = []

    def Node_Add(self, item):
        self.Data.append([]) # adds a new column for the new node
        self.Nodes.append(item) #adds the nodes name to list
        self.temp.append(0) # temp is the length of all the nodes so that we can fill the latest node with the right amount of zeros
        
        for i in range(len(self.temp)): # fills the new node with all 0's
            self.Data[len(self.Data)-1].append(0)
            if i == len(self.Data)-1:
                pass
            else:
                self.Data[i].append(0)
            

    def Node_Remove(self,item):
        location = 0

        for i in range(len(self.Nodes)): #finds the node location based on the node lists location
            if self.Nodes[i] == item:
                location = i
            else:
                pass
        del(self.Data[location]) # deletes the row of that node
        for i in range(len(self.Data)):
            del(self.Data[i][location]) # deletes the column of that node in each of the lists
        del(self.Nodes[location]) # removes node from node list
        del(self.temp[location]) # shortens the temp list of how many 0's to add

    def see_graph(self):
        temp = 0
        for i in range(len(self.Nodes)):
            if temp < len(self.Nodes[i]):
                temp = len(self.Nodes[i])
        print((" "*temp)+"  "+'  '.join(self.Nodes))# formats the top row showing node names
        for columns in range(len(self.Data)): # goes through and print each column on a new line to see the graph easier
            print(self.Nodes[columns]+((temp - len(self.Nodes[columns]))* " "),self.Data[columns]) # prints the node name of the row followed by the row of that node
  
    def Node_Connect(self, item1, item2):
        location1 = 0
        location2 = 0
        for i in range(len(self.Nodes)):
            if self.Nodes[i] == item1:
                location1 = i
            else:
                pass
        for i in range(len(self.Nodes)):
            if self.Nodes[i] == item2:
                location2 = i
            else:
                pass
        self.Data[location1][location2] =1
        self.Data[location2][location1] = 1
    
Matrix = Graph()
x = False
while x == False:
    userinput = input("do you want to add, remove, connect a node or see the graph (add, remove, connect, see):")
    if userinput == "add":
        adding = input("what is the name of this node:")
        Matrix.Node_Add(adding)
    elif userinput == "remove":
        removing = input("what is the name of this node:")
        Matrix.Node_Remove(removing)
    elif userinput == "see":
        Matrix.see_graph()
    elif userinput == "connect":
        removing = input("what are the 2 nodes you want to connect (put a space between them):")
        temp = removing.split()
        Matrix.Node_Connect(temp[0],temp[1])
    elif userinput == "exit": 
        x = True
    else: x = False
