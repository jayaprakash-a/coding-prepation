class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        answer = 0
        timeVals = [0 for _ in range(60)]
        for i in range(len(time)):
            timeVals[time[i]%60] += 1
        for i in range(1, 30):
            answer += (timeVals[i]*timeVals[60-i])
        answer += (timeVals[0]*(timeVals[0]-1))//2
        answer += (timeVals[30]*(timeVals[30]-1))//2
        return answer
                