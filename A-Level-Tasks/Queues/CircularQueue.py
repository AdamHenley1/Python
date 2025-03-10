class CircularQueue():
    def __init__(self, Maxs):
        self.Maxs = Maxs
        self.Count = 0
        self.Data = []
        self.RP = -1
        self.FP = 0
        
    
    def EnQueue(self,Item):
        if self.Count == self.Maxs:
            print("error queue is full")
        elif self.RP == self.Maxs-1 and self.FP > 0:
            print("[loop]Adding ", Item)
            self.RP = 0
            self.Data[self.RP] = Item
            self.Count += 1
        else:
            print("Adding ", Item)
            self.RP += 1
            self.Data.append(Item)
            self.Count += 1

    def Peek(self):
        print("The Current Task Is ", self.Data[self.FP])
    
    def DeQueue(self):
        if self.FP == self.Maxs-1 and self.RP > 0:
            print("[Loop]Executing ", self.Data[self.FP])
            self.FP = 0
            self.Count -= 1
        else:
            print("executing ", self.Data[self.FP])
            self.FP += 1
            self.Count -=1

    def IsFull(self):
        if self.Count == self.Maxs:
            print("True")
        else:
            print("False")

    def IsEmpty(self):
        if self.Count == 0:
            print("True")
        else:
            print("False")

Circ = CircularQueue(5)

Circ.EnQueue("1");
Circ.EnQueue("2");
Circ.EnQueue("3");
Circ.EnQueue("4");
Circ.EnQueue("5");
Circ.EnQueue("6");
Circ.DeQueue();
Circ.DeQueue();
Circ.EnQueue("6");
Circ.EnQueue("9");
Circ.EnQueue("69");
Circ.EnQueue("9887");
Circ.EnQueue("643");
Circ.EnQueue("953553");
Circ.DeQueue();
Circ.IsEmpty();
Circ.EnQueue("3jk");
Circ.IsFull();
Circ.DeQueue();
Circ.DeQueue();
Circ.DeQueue();
Circ.DeQueue();
Circ.DeQueue();
Circ.IsFull();
Circ.IsEmpty();