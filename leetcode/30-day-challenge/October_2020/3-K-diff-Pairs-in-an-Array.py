class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        answer = set()
        nums = sorted(nums)

        
        if k < 0:
            return 0
        count, visited = 0, set()
        
        if k == 0:
            nc = collections.Counter(nums)
            for num in nc:
                if nc[num] >= 2:
                    count += 1
            return count
        for num in nums:
            if num not in visited:
                if num-k in visited:
                    count += 1
                elif num+k in visited:
                    count += 1
                visited.add(num)
        return count