class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        answer = float('inf')
        numSet = set()
        for num in arr:
            numSet = {num & val for val in numSet} | {num}
            for val in numSet:
                answer = min(answer, abs(val-target))
        return answer