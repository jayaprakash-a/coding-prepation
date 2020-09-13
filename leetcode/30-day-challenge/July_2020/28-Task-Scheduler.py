class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = list(collections.Counter(tasks).values())
        maxFreq = max(taskFreq)
        maxCount = taskFreq.count(maxFreq)
        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)