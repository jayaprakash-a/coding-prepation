class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        preSum, sufSum = [0], [0]
        for num in cardPoints:
            preSum.append(preSum[-1]+num)
        for num in cardPoints[::-1]:
            sufSum.append(sufSum[-1]+num)
        maxVal = 0
        # print(preSum)
        # print(sufSum)
        for i in range(k):
            # print(preSum[i], sufSum[k-i])
            maxVal = max(preSum[i]+sufSum[k-i], maxVal)
        # print('Break')
        for i in range(k):
            # print(preSum[i], sufSum[k-i])
            maxVal = max(preSum[k-i]+sufSum[i], maxVal)
        return maxVal
            