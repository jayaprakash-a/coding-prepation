class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-1):
            temp = arr[len(arr)-i-2]
            arr[len(arr)-i-2] = maxVal
            if temp > maxVal:
                maxVal = temp
        return arr
        