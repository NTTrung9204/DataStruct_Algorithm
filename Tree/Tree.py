class Node:
    def __init__(self, Values):
        self.Values = Values
        self.Left = None
        self.Right = None

class BinaryTree:
    def __init__(self):
        self.Root = None

    def Insert(self, Values):
        if self.Root == None : 
            self.Root = Node(Values)
        else:
            self._InsertRecursive(self.Root, Values)

    def _InsertRecursive(self, CurrentNode, Values):
        if CurrentNode.Values < Values:
            if CurrentNode.Right == None : CurrentNode.Right = Node(Values)
            else : self._InsertRecursive(CurrentNode.Right, Values)
        if CurrentNode.Values > Values:
            if CurrentNode.Left == None : CurrentNode.Left = Node(Values)
            else : self._InsertRecursive(CurrentNode.Left, Values)

    def DisplayLNR(self):
        if self.Root is None : print("Tree don't have any elements!")
        else :
            self._DisplayLNRRecursive(self.Root)
    
    def _DisplayLNRRecursive(self, CurrentNode):
        if CurrentNode is not None:
            self._DisplayLNRRecursive(CurrentNode.Left)
            print(CurrentNode.Values)
            self._DisplayLNRRecursive(CurrentNode.Right)

    def NumberOfLeaveNode(self):
        return self._NumberOfLeaveNodeRecursive(self.Root)
    
    def _NumberOfLeaveNodeRecursive(self, CurrentNode):
        if CurrentNode is None : 
            return 0
        if CurrentNode.Left is None and CurrentNode.Right is None : 
            return 1
        
        LeftLeaveNode = self._NumberOfLeaveNodeRecursive(CurrentNode.Left)
        RightLeaveNode = self._NumberOfLeaveNodeRecursive(CurrentNode.Right)

        return LeftLeaveNode + RightLeaveNode
    
    def NumberOfNode(self):
        return self._NumberOfNodeRecursive(self.Root)
    
    def _NumberOfNodeRecursive(self, CurrentNode):
        if CurrentNode is None : 
            return 0
        
        LeftNode = self._NumberOfNodeRecursive(CurrentNode.Left)
        RightNode = self._NumberOfNodeRecursive(CurrentNode.Right)

        return LeftNode + RightNode + 1
    
    def DepthOfTree(self):
        return self._DepthOfTreeRecursive(self.Root)
    
    def _DepthOfTreeRecursive(self, CurrentNode):
        if CurrentNode is None:
            return 0
        
        LeftDepth = self._DepthOfTreeRecursive(CurrentNode.Left)
        RightDepth = self._DepthOfTreeRecursive(CurrentNode.Right)

        return max(LeftDepth, RightDepth) + 1
    
    def Delete(self, Values):
        self.Root = self._Delete(self.Root, Values)

    def _Delete(self, Root, Values):
        if Root is None:
            return Root
        if Values < Root.Values:
            Root.Left = self._Delete(Root.Left, Values)
        elif Values > Root.Values:
            Root.Right = self._Delete(Root.Right, Values)
        else:
            if Root.Left is None:
                return Root.Right
            elif Root.Right is None:
                return Root.Left
            Root.Values = self._FindMinValue(Root.Right)
            Root.Right = self._Delete(Root.Right, Root.Values)
        return Root

    def _FindMinValue(self, node):
        current = node
        while current.Left is not None:
            current = current.Left
        return current.Values

    


Model = BinaryTree()

Model.Insert(10)
Model.Insert(30)
Model.Insert(70)
Model.Insert(20)
Model.Insert(100)
Model.Insert(90)

Model.DisplayLNR()
print()
Model.Delete(70)
Model.Delete(20)
print(Model.Root.Values)

Model.DisplayLNR()

print(Model.DepthOfTree())
print(Model.NumberOfLeaveNode())
print(Model.NumberOfNode())
