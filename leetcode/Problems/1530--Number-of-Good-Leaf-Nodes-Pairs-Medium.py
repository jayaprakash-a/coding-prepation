# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # print('-------')
        self.answer = 0
        def helper(root, distance):
            if not root:
                return Counter()

            if not root.right and not root.left:
                a = Counter()
                a[1] = 1
                return a
            left = helper(root.left, distance)
            right = helper(root.right, distance)
            # print(root.val, left, right)
            for d1 in left:
                for d2 in right:
                    if d1 + d2 <= distance:
                        self.answer += (left[d1]*right[d2])
            newDict = Counter()
            temp = left+right
            for d1 in temp:
                if d1 + 1 < distance:
                    newDict[d1+1] = temp[d1]
            return newDict
        helper(root, distance)
        return self.answer