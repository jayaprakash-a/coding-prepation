class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def bc(n, k): 
            if(k > n - k): 
                k = n - k 
            res = 1
            for i in range(k): 
                res = res * (n - i) 
                res = res // (i + 1) 
            return res
        root = TreeNode(nums[0])
        def insert(root, val):
            if not root:
                return TreeNode(val)
            if root.val > val:
                root.left = insert(root.left, val)
            else:
                root.right = insert(root.right, val)
            return root
        for num in nums[1:]:
            root = insert(root, num)
            
        def getVal(root):
            if not root:
                return (0, 1)
            if root.left or root.right:            
                left = getVal(root.left)
                right = getVal(root.right)
            else:
                return (1, 1)
            return (1+left[0]+right[0], bc(left[0]+right[0], left[0])*left[1]*right[1])
            
        answer = (getVal(root)[1]-1)%(10**9+7)
        return answer