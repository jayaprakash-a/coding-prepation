# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.answer = 0
        def dfs(node, prevSums, sum):
            if not node:
                return
            
            temp = prevSums[sum]
            newSums = Counter()

            for prevSum in prevSums:
                newSums[prevSum + node.val] = prevSums[prevSum]
                if prevSum + node.val == sum:
                    self.answer += prevSums[prevSum]
            newSums[node.val] = prevSums[0] + 1
            if node.val == sum:
                self.answer += 1
            
            # print(node.val, self.answer, prevSums, newSums)
            dfs(node.left, newSums, sum)
            dfs(node.right, newSums, sum)
        
        dfs(root, Counter(), sum)
        
        return self.answer