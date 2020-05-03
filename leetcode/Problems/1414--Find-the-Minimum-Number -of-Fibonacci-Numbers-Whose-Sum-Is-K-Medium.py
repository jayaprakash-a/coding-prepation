class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        if k <= 2:
            return 1

        fibVals = [1, 1]
        fibVal = 2
        while(fibVal <= k):
            fibVals.append(fibVal)
            fibVal = fibVals[-1]+fibVals[len(fibVals)-2]
        print(fibVals)
        # maxFib = fibVals[-1]
        answer = 0

        diff = k
        # print(k)
        while(diff != 0):
            if diff <= 2:
                answer += 1
                break
            # print(diff)
            index = bisect_left(fibVals, diff)
            if index == len(fibVals) or diff < fibVals[index]:
                index -= 1
            # print(diff, fibVals[index])
            answer += 1
            diff = k-fibVals[index]
            k = diff

        return answer
