class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # class Solution:
    # def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        answer = 0
        for i in range(len(timeSeries)-1):
            answer += min((timeSeries[i+1]-timeSeries[i]), duration)
        # answer += duration
        return answer+duration