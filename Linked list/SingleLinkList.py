class Node:
    def __init__(self, Values):
        self.Values = Values
        self.Next = None

class SingleLinkList:
    def __init__(self):
        self.Head = None

    def AddLast(self, Values):
        NewNode = Node(Values)
        if self.Head == None:
            self.Head = NewNode
        else:
            CurrentNode = self.Head
            while CurrentNode.Next != None:
                CurrentNode = CurrentNode.Next
            CurrentNode.Next = NewNode

    def AddFirst(self, Values):
        NewNode = Node(Values)
        NewNode.Next = self.Head
        self.Head = NewNode

    def RemoveLast(self):
        if self.Head == None:
            print("Single link list was empty!!!")
        elif self.Head.Next == None : self.Head = None
        else:
            CurrentNode = self.Head
            while CurrentNode.Next.Next != None:
                CurrentNode = CurrentNode.Next
            CurrentNode.Next = None

    def RemoveFirst(self):
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


