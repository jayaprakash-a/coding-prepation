class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer = sum(arr)
        for i in range(3, len(arr)+1, 2):
            for j in range(len(arr)):
                if j+i <= len(arr):
                    # print(j, j+i, arr[j:j+i])
                    for k in range(j, j+i, 1):
                        answer += arr[k]
        return answer