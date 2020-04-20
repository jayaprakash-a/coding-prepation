class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect_left(arr, x)
        
        l, r, count = index-1, index+1, 0
        answer = []
        if arr[index] == x:
            print(index)
            answer = [x]
            count += 1
            if l < 0:
                r = 1
            elif r >= len(arr):
                l = len(arr)-2
        else:
            r = index
        
            if l < 0:
                r = 0
            elif r >= len(arr):
                l = len(arr)-1
        
        
        
        while(count < k):
            # print(answer)
            if l < 0:
                answer.append(arr[r])
                r += 1
            elif r >= len(arr):
                answer.insert(0, arr[l])
                l -= 1 
            elif abs(arr[l]-x) <= abs(arr[r]-x):
                answer.insert(0, arr[l])
                l -= 1 
            elif abs(arr[l]-x) > abs(arr[r]-x):
                answer.append(arr[r])
                r += 1
            count += 1
        return answer