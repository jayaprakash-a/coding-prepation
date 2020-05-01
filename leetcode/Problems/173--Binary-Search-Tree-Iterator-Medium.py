# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.pointers = []
        curr = root
        while curr != None:
            self.pointers.append(curr)
            curr = curr.left
        # for i in range(len(self.pointers)):
            # print('print', self.pointers[i].val)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # print(self.pointers[-1])
        curr = self.pointers[-1].right
        answer = self.pointers[-1].val
        self.pointers.pop()
        
        while curr != None:
            self.pointers.append(curr)
            curr = curr.left
        # print(answer)
        # print(self.pointers[-1].val)
        # return self.pointers[-1].val
        return answer
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.pointers) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()