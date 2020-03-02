class Node:
    def __init__(self, data):
        self.root = data
        self.leftC = None
        self.rightC = None
        
def insertRec(data, currNode):
    if(currNode.data == None):
        currNode.data = data
        return
    if(currNode.data < data):
        insertRec(data, currNode.rightC)
    elif(currNode.data > data):
        insertRec(data, currNode.leftC)
        
def deleteRec(data, currNode):
    if(currNode.data == data):
        temp = currNode.data
        if(currNode.leftC != None and currNode.rightC != None):
            currNode = None
        elif(currNode.leftC != None):
            currNode.data = currNode.leftC.data
            currNode.leftC.data = temp
            deleteRec(data, currNode.leftC)
        else:
            currNode.data = currNode.rightC.data
            currNode.rightC.data = temp
            deleteRec(data,currNode.rightC)
        return
    if(currNode.data < data):
        deleteRec(currNode.rightC, data)
    elif(currNode.data > data):
        deleteRec(currNode.leftC, data)

def findNextRec(num, currNode):
    if(currNode.data == None):
        return
    if(num == findMaxRec()):
        return None
    num = min(findNextRec(num,currNode.leftC), findNextRec(num, currNode.rightC))
    if(currNode.data > num):
        return currNode.data
    return num
            
def findPrevRec(num, currNode, minnum):
    if(currNode.data == None):
        return
    if(num == findMinRec()):
        return None
    num = max(findNextRec(num,currNode.leftC), findNextRec(num, currNode.rightC))
    if(currNode.data < num):
        return currNode.data
    return num
def findMinRec(currNode):
    if(currNode.data == None):
        return
    findMinRec(currNode.leftC)

def findMaxRec(cuurNode):
    if(cuurNode.data == None):
        return
    findMaxRec(currNode.rightC)
    if(currNode.rightC == None):
        return currNode.data
