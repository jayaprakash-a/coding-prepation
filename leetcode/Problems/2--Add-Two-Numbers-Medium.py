# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp1, temp2 = l1, l2
        carry = 0
        answer = ListNode(0)
        solution = answer
        previous = None
        while(temp1 or temp2 or carry != 0):
            sum = 0
            try:
                sum += temp1.val
                temp1 = temp1.next
            except:
                pass
            try:
                sum += temp2.val
                temp2 = temp2.next
            except:
                pass
            answer.val = ((sum+carry)%10)
            carry = (sum+carry)//10
            
            answer.next = ListNode(0)
            previous = answer
            answer = answer.next
            
        
        previous.next = None
        return solution
        