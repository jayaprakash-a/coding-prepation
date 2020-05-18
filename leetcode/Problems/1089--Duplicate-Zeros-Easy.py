class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = list(arr)
        i, j = 0, 0
        
        while i < len(temp):
            while(i < len(temp) and j < len(temp) and temp[j] != 0):
                arr[i] = temp[j]
                i += 1
                j += 1
            if i < len(temp) and j < len(temp):
                arr[i] = 0
                i += 1
                if i < len(temp):
                    arr[i] = 0
                    i += 1
                    j += 1
                