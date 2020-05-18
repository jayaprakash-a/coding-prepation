# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        answer = [None for _ in range(k)]
        pointers = [None for _ in range(k)]
        temp = root
        length = 0
        while(temp):                   
            temp = temp.next
            length += 1
        
        index = 0
        temp = root
        prev = None
        while(temp):
            answer[index] = temp
            if index < (length%k):
                for _ in range(length//k +1):
                    prev = temp
                    if temp:
                        temp = temp.next
            else:
                for _ in range(length//k):
                    prev = temp
                    if temp:
                        temp = temp.next
            if prev:
                prev.next = None
            index += 1
        
        return answer