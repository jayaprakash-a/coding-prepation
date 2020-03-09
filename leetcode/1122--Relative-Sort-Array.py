class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        A = []
        
        for num in arr2:
            while(num in arr1):
                A.append(num)
                arr1.remove(num)
        
        A += sorted(arr1)
            
        return A
        