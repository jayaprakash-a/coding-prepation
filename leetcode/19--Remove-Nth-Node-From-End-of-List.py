# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        indexNode, trackNode = head, head
        
        i = 0
        while(i < n):
            indexNode = indexNode.next
            i += 1
        
        if not indexNode:
            return head.next
        
        while(indexNode.next):
            trackNode = trackNode.next
            indexNode = indexNode.next
            
        trackNode.next = trackNode.next.next
        
        return head
        