class Solution:
    
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        def comp(x):
            return x[1], x[0]
        answer = []
        # sortArr = 
        # if len(arr)%2 == 0:
        median = sorted(arr)[(len(arr)-1)//2]
        # answer = []
        for num in arr:
            answer.append([num, abs(num-median)])
        
        sortedArr = sorted(answer, key=comp, reverse=True)
        result = []
        for i in range(k):
            result.append(sortedArr[i][0])
        
        return result
        