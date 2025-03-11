class Graph():
    def __init__(self):
        self.Data = []
        self.temp = []
        self.Nodes = []
    def Node_Add(self, item):
        #print(self.Data)
        self.Data.append([])
        self.Nodes.append(item)
        self.temp.append(0)
        for i in range(len(self.temp)):
            self.Data[len(self.Data)-1].append(0)
        for i in range(len(self.Data)-1):
            self.Data[i].append(0)

    def Node_Remove(self,item):
        location = 0
        for i in range(len(self.Nodes)):
            if self.Nodes[i] == item:
                location = i
            else:
                pass
        del(self.Data[location])
        for i in range(len(self.Data)):
            del(self.Data[i][location])
        del(self.Nodes[location])
        del(self.temp[location])

    def see_graph(self):
        print('  ', '  '.join(self.Nodes))
        for columns in range(len(self.Data)):
            print(self.Nodes[columns],self.Data[columns])
  
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
Matrix.Node_Add("a")
Matrix.Node_Add("b")
Matrix.Node_Add("c")
Matrix.Node_Connect("a","c")
Matrix.see_graph()
Matrix.Node_Add("d")
Matrix.Node_Add("e")
Matrix.Node_Remove("b")
Matrix.see_graph()
Matrix.Node_Add("f")
Matrix.Node_Connect("d","f")
Matrix.see_graph()