class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        numSet = set()
        for num in leftChild:
            if num != -1:
                if num in numSet:
                    return False
                else:
                    numSet.add(num)
        
        for num in rightChild:
            if num != -1:
                if num in numSet:
                    return False
                else:
                    numSet.add(num)
        
        if len(numSet) == (n -1):
            return True
        else:
            return False
            
        
        