class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # print('-----------')
        answer = 0
        while numBottles  >= numExchange:
            answer += numBottles - ((numBottles%numExchange))
            numBottles = (numBottles%numExchange) + numBottles//numExchange
            # print(numBottles)
        return answer+numBottles