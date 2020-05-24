# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0
        def checkPalin(entries):
            counter = collections.Counter(entries)
            odd = 0
            for key in counter.keys():
                if counter[key] % 2 == 1:
                    odd += 1
            # print(entries, odd<=1 )
            return odd <= 1
        def getCount(root, entries):
            if not root:
                return 
            entries.append(root.val)
            if not root.right and not root.left:
                if checkPalin(entries):
                    self.count += 1
            getCount(root.left, list(entries))
            getCount(root.right, list(entries))
        
        getCount(root, [])
        return self.count