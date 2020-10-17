# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
        temp.next = head
        rem = length - (k%length)
        # temp = 
        while rem:
            rem -= 1
            temp = temp.next
        answer = temp.next
        temp.next = None
        return answer
