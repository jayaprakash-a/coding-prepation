class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) <= k:
            return False
        num = int(s[:k], 2)
        nums = {num}
        for i in range(k, len(s)):
            num %= (1<<(k-1))
            num = (num << 1) + int(s[i])
            nums.add(num)
        return len(nums) == (1<<k)