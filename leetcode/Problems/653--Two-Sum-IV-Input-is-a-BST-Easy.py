
class BSTIterator:

    def __init__(self, root: TreeNode, forward):
        self.pointers = []
        curr = root
        self.forward = forward
        if self.forward:
            while curr != None:
                self.pointers.append(curr)
                curr = curr.left
        else:
            while curr != None:
                self.pointers.append(curr)
                curr = curr.right


    def next(self) -> int:
        if self.forward:
            curr = self.pointers[-1].right
            answer = self.pointers[-1].val
            self.pointers.pop()

            while curr != None:
                self.pointers.append(curr)
                curr = curr.left

            return answer
        else:
            curr = self.pointers[-1].left
            answer = self.pointers[-1].val
            self.pointers.pop()

            while curr != None:
                self.pointers.append(curr)
                curr = curr.right
            return answer
        
    def hasNext(self) -> bool:
        return len(self.pointers) > 0
    
class Solution:

    
    def findTarget(self, root: TreeNode, k: int) -> bool:
        l, r = BSTIterator(root, True), BSTIterator(root, False)
        lVal, rVal = l.next(), r.next()

        while(lVal < rVal):
            if lVal + rVal == k:
                return True
            elif lVal + rVal < k:
                lVal = l.next()
            else:
                rVal = r.next()
        return False