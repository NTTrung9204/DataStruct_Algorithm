class Node:
    def __init__(self, Values):
        self.Values = Values
        self.Next = None

class Queue:
    def __init__(self):
        self.Front = None
        self.Rear = None

    def IsEmpty(self):
        return self.Rear is None

    def EnQueue(self, Values):
        NewNode = Node(Values)
        if self.Rear is None : 
            self.Rear = self.Front = NewNode
        else:
            self.Front.Next = NewNode
            self.Front = NewNode

    def DeQueue(self):
        if self.IsEmpty():
            print("Queue is empty!")
        Values = self.Rear.Values
        if self.Rear == self.Front :
            self.Rear = self.Front = None
        else:
            self.Front = self.Front.Next
        return Values
    
    def Peeks(self):
        return self.Rear.Values
    
    def Size(self):
        Count = 0
        CurrentNode = self.Rear
        while CurrentNode.Next is not None:
            Count += 1
            CurrentNode = CurrentNode.Next
        return Count
    
MyQueue = Queue()

MyQueue.EnQueue(10)
MyQueue.EnQueue(20)
MyQueue.EnQueue(30)

print(MyQueue.DeQueue())
print(MyQueue.Peeks())
print(MyQueue.IsEmpty())
print(MyQueue.Size())  


    