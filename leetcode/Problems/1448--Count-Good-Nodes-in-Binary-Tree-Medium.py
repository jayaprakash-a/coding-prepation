# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        values = [root.val]
        maxVal = root.val
        answer = 1
        def getVal(root, maxVal):
            if not root:
                return 0
            answer = 0
            if root.val >= maxVal:
                answer += 1
            maxVal = max(maxVal, root.val)
            answer += getVal(root.left, maxVal)
            answer += getVal(root.right, maxVal)
            return answer
        return getVal(root, maxVal)
            
                
            
        