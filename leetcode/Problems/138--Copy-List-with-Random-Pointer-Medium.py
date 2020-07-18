"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return None
        
        nodeList, temp = [], head
        tempList = []
        
        while temp:
            tempList.append(temp)
            copy = Node(temp.val)
            nodeList.append(copy)
            temp = temp.next
        
        randomPointer = []
        
        for i in range(len(tempList)):
            if tempList[i].random == None:
                randomPointer.append(-1)
            for j in range(len(tempList)):
                if tempList[j] == tempList[i].random:
                    randomPointer.append(j)
                    break
        
        for i in range(len(nodeList)):
            if i != len(nodeList)-1:
                nodeList[i].next = nodeList[i+1]
            if randomPointer[i] != -1:
                nodeList[i].random = nodeList[randomPointer[i]]
        
        return nodeList[0]