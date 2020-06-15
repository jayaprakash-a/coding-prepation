class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if k == 1:
            bloomDay = sorted(bloomDay)
            return bloomDay[m-1]
        def isValid(k, j, m):
            flow, bouq = 0, 0
            for num in bloomDay:
                if num > j:
                    flow = 0
                else:
                    flow += 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq >= m:
                        return True
            return False            
        n = len(bloomDay)
        if m*k > n:
            return -1
        elif m*k == n:
            return max(bloomDay)
        
        minVal, maxVal = min(bloomDay), max(bloomDay)
        l, r = minVal, maxVal
        answer = maxVal
        while l < r:
            mid = (l+r)//2
            if isValid(k, mid, m):
                answer = min(answer, mid)
                r = mid
            else:
                l = mid+1

        return answer