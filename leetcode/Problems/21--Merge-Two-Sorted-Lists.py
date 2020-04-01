# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = answer = ListNode(0)
        while(l1 or l2):
            if (l1 and l2 and l1.val < l2.val) or not l2:
                print(l1.val)
                answer.next = ListNode(l1.val)
                l1 = l1.next
            elif (l1 and l2 and l2.val <= l1.val) or not l1:
                print(l2.val)
                answer.next = ListNode(l2.val)
                l2 = l2.next
            answer = answer.next
            
        
            
        return head.next