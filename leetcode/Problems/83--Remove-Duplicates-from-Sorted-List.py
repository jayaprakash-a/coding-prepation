# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node = head
        while(head):
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head = head.next
            
        return node
        