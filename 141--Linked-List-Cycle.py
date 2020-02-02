# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slowNode = head        
        fastNode = head.next
        try:            
            while slowNode is not fastNode:
                slowNode = slowNode.next
                fastNode = fastNode.next.next
            return True
        except:
            return False
        