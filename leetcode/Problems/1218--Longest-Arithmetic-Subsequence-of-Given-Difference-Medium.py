class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        answer = Counter()
        for num in arr:
            answer[num] = answer[num-diff] + 1
        return max(answer.values())
        