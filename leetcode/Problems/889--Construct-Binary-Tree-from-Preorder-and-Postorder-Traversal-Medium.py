# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        index = post.index(pre[1])
        # print('left', pre[0], pre[1:1+index+1], post[:index-1])
        # print('right', pre[0], pre[1+index+1:], post[index-1:-1])
        root.left = self.constructFromPrePost(pre[1:1+index+1], post[:index+1])
        root.right = self.constructFromPrePost(pre[1+index+1:], post[index+1:-1])
        
        return root