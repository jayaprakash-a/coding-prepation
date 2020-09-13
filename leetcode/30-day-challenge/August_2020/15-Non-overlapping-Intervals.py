class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])  # sort on start time
        currEnd, cnt = intervals[0][1], 0
        for x in intervals[1:]:
            if x[0] < currEnd:  # find overlapping interval
                cnt += 1
                currEnd = min(currEnd, x[1])  # erase the one with larger end time
            else:
                currEnd = x[1]   # update end time
        return cnt