class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        preInc = 0
        prev = -1*sys.maxsize
        i = 0
        while i < len(arr) and arr[i] >= prev:
            prev = arr[i]
            i += 1
        left = i-1
        next = sys.maxsize
        i = len(arr)-1
        while i >= 0 and arr[i] <= next:
            next = arr[i]
            i -= 1
        right = i+1
        if left == len(arr)-1 and right == 0:
            return 0
        answer = min(len(arr)-left-1, right)
        queue = deque([[left, right]])
        while queue:
            [left, right] = queue.pop()
            if 0 <= left < len(arr) and 0 <= right < len(arr):
                if arr[right] >= arr[left]:
                    answer = min(answer, right-left-1)
                if arr[right] < arr[left]:
                    queue.append([left-1, right])
                    queue.append([left, right+1])
            elif 0 <= left < len(arr):
                answer = min(answer, len(arr)-left-1)
            elif 0 <= right < len(arr):
                answer = min(answer, right)
        return answer                    
