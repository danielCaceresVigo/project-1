class Node:
    def __init__(self, data):
        self.data = data
        self.leftC = None
        self.rightC = None
        self.parent = None
    def __int__(self):
        self.data = None
def insertIter(num, currNode):
    new = Node(num)
    parent = currNode
    while(currNode != None):
        parent = currNode
        if(currNode.data > num):
            currNode = currNode.leftC
        else:
            currNode = currNode.rightC
    if(parent == None):
        parent = new
    elif(num < parent.data):
        parent.leftC = new
    else:
        parent.rightC = new
def deleteIter(num, currNode):
    while(currNode.data != num):
        if(currNode.data > num):
            currNode = currNode.leftC
        else:
            currNode = currNode.rightC
    while(currNode.rightC != None or currNode.leftC !=None):
        temp = currNode.data
        if(currNode.leftC != None):
            currNode.data = currNode.leftC.data
            currNode = currNode.leftC
            currNode.data = temp
        else:
            currNode.data = currNode.rightC.data
            currNode = currNode.rightC
            currNode.data = temp
    del currNode.data
def findNextIter(num, currNode):
    maxnum = findMaxIter(currNode)
    if(num == maxnum):
        return None
    if(currNode.data < maxnum and currNode.data > num):
        maxnum = currNode.data
    parent = currNode
    arr = []
    while(currNode != None):
        while(currNode != None):
            if(not(currNode.leftC.data in arr) and currNode.leftC != None):
                currNode = currNode.leftC
            elif(not(currNode.rightC.data in arr) and currNode.rightC != None):
                currNode = currNode.rightC
            else: break
        arr.append(currNode.data)
        if(currNode != None and currNode.data < maxnum and currNode.data > num):
            maxnum = currNode.data
    return maxnum
    
def findPrevIter(num, currNode):
    minnum = findMinIter(currNode)
    if(num == minnum):
        return None
    if(currNode.data > minnum and currNode.data < num):
        minnum = currNode.data
    parent = currNode
    arr = []
    while(currNode != None):
        while(currNode != None):
            if(not(currNode.leftC.data in arr) and currNode.leftC != None):
                currNode = currNode.leftC
            elif(not(currNode.rightC.data in arr) and currNode.rightC != None):
                currNode = currNode.rightC
            else: break
        arr.append(currNode.data)
        if(currNode != None and currNode.data > minnum and currNode.data < num):
            minnum = currNode.data
    return minnum
def findMinIter(currNode):
    while(currNode.leftC != None):
        currNode = currNode.leftC
    return currNode.data
def findMaxIter(currNode):
    while(currNode.rightC != None):
        currNode = currNode.rightC
    return currNode.data
