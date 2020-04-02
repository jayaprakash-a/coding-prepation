# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def find(self, val, arr):
        l, r = 0, len(arr)-1
        while(l <= r and l>=0 and r<len(arr)):
            mid = (l+r)//2
            if arr[mid] == val:
                
                return mid
            elif arr[mid] > val:
                r = mid-1
            else:
                l = mid+1
        
        return -1
            
            
            
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        # nums = []
        component, count = 0, 0
        G = sorted(G)
        while(head):
            index = self.find(head.val, G)
            if index != -1:
                G.pop(index)
                count += 1
            else:
                if count > 0:
                    component += 1
                    count = 0
            head = head.next
        if count > 0:
            component += 1
            # component = []
        return component
            