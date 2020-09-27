class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45 or k > 9:
            return []
        answer = []
        def getAns(start, arr):
            arr = list(arr)
            if len(arr) == k and sum(arr) == n:
                answer.append(arr)
            elif len(arr) > k or sum(arr) > n or start > 9:
                return
            for i in range(start, 10):
                arr += [i]
                getAns(i+1, arr)
                arr.pop()
        getAns(1, [])
        
        return answer