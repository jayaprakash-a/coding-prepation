# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        answer = []
        head = None
        headNode = head
        while(True):
            minValue = None
            for i in range(len(lists)):
                if lists[i]:
                    if minValue == None:
                        minValue = lists[i].val
                    elif minValue > lists[i].val:
                        minValue = lists[i].val
            count = 0
            for i in range(len(lists)):
                if lists[i] and lists[i].val == minValue:
                    count += 1
                    lists[i] = lists[i].next

            answer += ([minValue]*count)
            if minValue == None:
                break
        for num in answer[::-1]:
            new_node = ListNode(num)
            new_node.next = head
            head = new_node
        return head
            
                
        