class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        maxValue = max(arr)
        l, r = 0, maxValue+1
        answer = maxValue
        minDiff = target
        arr = sorted(arr)
        while(l < r):
            mid = (r+l)//2
            value = 0
            for i in range(len(arr)):
                if arr[i] >= mid:
                    value += (len(arr)-i)*mid
                    break
                else:
                    value += arr[i]
            if abs(value-target) < minDiff:
                answer = mid
                minDiff = abs(value-target)
            
            elif abs(value-target) == minDiff:
                answer = min(mid, answer)
            
            if value >= target:
                r = mid
            else:
                l = mid + 1

        return answer
            
            