class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        if len(matrix) == 0:
            return False
        top, down = 0, len(matrix) - 1
        
        while(top < down):
            if matrix[top][-1] < target:
                top += 1
            if matrix[down][0] > target:
                down -= 1
        if top != down:
            return False
        
        left, right = 0, len(matrix[0]) - 1
        
        while(left <= right):
            mid = (left+right)//2
            if matrix[top][mid] == target:
                return True
            if matrix[top][mid] > target:
                right = mid - 1
            if matrix[top][mid] < target:
                left = mid + 1
        
        return False
            
            
            
            
        