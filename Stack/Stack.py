class Node:
    def __init__(self, Values):
        self.Values = Values
        self.Next = None

class Stack:
    def __init__(self):
        self.Head = None

    def Push(self, Values):
        NewNode = Node(Values)
        NewNode.Next = self.Head
        self.Head = NewNode

    def Pop(self):
        if self.Head == None:
            print("Single link list was empty!!!")
        else:
            self.Head = self.Head.Next

    def Display(self):
        CurrentNode = self.Head
        while CurrentNode != None:
            print(CurrentNode.Values, end = " -> ")
            CurrentNode = CurrentNode.Next
        print("None")

MyList = Stack()

MyList.AddLast(30)
MyList.AddLast(10)
MyList.AddLast(60)
MyList.AddLast(80)

MyList.RemoveLast()

MyList.Display()
