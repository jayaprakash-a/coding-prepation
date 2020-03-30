class Solution:

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr = sorted(arr)        
        minDiff = min([arr[i+1]-arr[i] for i in range(len(arr)-1)])
        
        answer = [[arr[i], arr[i+1]]  for i in range(len(arr)-1) if (arr[i+1]-arr[i] == minDiff)]
        
        
        return answer