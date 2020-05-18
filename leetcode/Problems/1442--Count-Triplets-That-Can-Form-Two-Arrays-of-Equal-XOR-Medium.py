class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        arr.insert(0, 0)
        
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i]^arr[j] == 0:
                    count += j - i -1
        return count