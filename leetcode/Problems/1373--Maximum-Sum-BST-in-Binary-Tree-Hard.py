# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.max, self.min = sys.maxsize, -sys.maxsize - 1

        def helper(root):
            if not root:
                return [self.min, self.max, True, self.min, self.min]
            left = helper(root.left)
            right = helper(root.right)
            if left[2] and right[2] and left[0] < root.val < right[1]:                
                answer = root.val 
                if left[3] != self.min:
                    answer += left[3]
                if right[3] != self.min:
                    answer += right[3]
                return [max(root.val, right[0]), min(root.val, left[1]), True, answer, max(left[4], right[4], answer)]
            else:
                return [0, 0, False, max(left[3], right[3]), max(left[4], right[4])]
        
        answer = helper(root)
        return max(0, answer[3], answer[4])