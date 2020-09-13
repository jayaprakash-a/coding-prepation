class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxNum, count = arr[0], 0
        for i in range(1, len(arr)):
            if arr[i] > maxNum:
                maxNum = arr[i]
                count = 1
                if count == k:
                    return maxNum
            else:
                count += 1
                if count == k:
                    return maxNum
        return maxNum