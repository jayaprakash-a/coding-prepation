class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.head
        i = 0
        
        while(index != i and node!=None):
            i+=1
            node = node.next
        
        if not node:
            return -1
        return node.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.head
        
        while(node.next):
            node = node.next
        node.next = ListNode(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        node = self.head
        prev = None
        while(index != 0 and node!=None):
            index -= 1
            prev = node
            node = node.next
        if index != 0:
            return
        newNode = ListNode(val)
        prev.next = newNode
        newNode.next = node
        
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            return
        node = self.head
        prev = None
        while(index != 0 and node!=None):
            index -= 1
            prev = node
            node = node.next
        if index != 0:
            return
        if node:
            prev.next = node.next
        else:
            prev.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)





# class MyLinkedList:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.linkedList = []

#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         if index < 0 or index >= len(self.linkedList):
#             return -1
#         return self.linkedList[index]

#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         self.linkedList.insert(0, val)
        

#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         self.linkedList.append(val)
        

#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         if index == len(self.linkedList):
#             self.linkedList.append(val)
#         else:
#             self.linkedList.insert(index, val)
        

#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         if index >= 0 and index < len(self.linkedList):
#             self.linkedList.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)