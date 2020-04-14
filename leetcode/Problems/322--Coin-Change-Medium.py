class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [0]+[float(inf)]*amount
        
        for i in range(1, len(arr)):
            for c in coins:
                if i >= c and arr[i-c] != float(inf):
                    arr[i] = min(arr[i], arr[i-c]+1)
        
        # print(arr)
        if arr[-1] != float(inf):
            return arr[-1]
        return -1