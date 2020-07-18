# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        answer = []
        q.append((root, 0, 0))
        minInd, maxInd = sys.maxsize, -1*sys.maxsize
        while q:
            node = q.popleft()
            answer.append((node[0].val, node[1], node[2]))
            minInd = min(minInd, node[1])
            maxInd = max(maxInd, node[1])
            if node[0].left:
                q.append((node[0].left, node[1]-1, node[2]+1))
            if node[0].right:
                q.append((node[0].right, node[1]+1, node[2]+1))
        
        def helper(x):
            return x[1], x[2], x[0]
        answer = sorted(answer, key=helper)
        result = [[]]
        result[0].append(answer[0][0])
        
        for i in range(1, len(answer)):
            if answer[i][1] != answer[i-1][1]:
                result.append([])
            result[-1].append(answer[i][0])
        return result