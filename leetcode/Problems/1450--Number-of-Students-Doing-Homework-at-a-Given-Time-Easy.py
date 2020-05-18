class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], time: int) -> int:
        answer = 0
        for start, end in zip(startTime, endTime):
            if start <= time <= end:
                answer += 1
        return answer 