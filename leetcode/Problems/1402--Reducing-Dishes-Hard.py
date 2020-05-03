class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        posArr = []
        posSum = 0
        negArr = []
        for val in satisfaction:
            if val >= 0:
                posSum += val
                posArr.append(val)
            else:
                negArr.append(val)

        negArr = sorted(negArr, reverse=True)
        posArr = sorted(posArr)
        negNewArr = [0]*len(negArr)
        for i in range(1, len(negArr)):
            negArr[i] = negArr[i-1]+negArr[i]
            negNewArr[i] = negArr[i-1]+negNewArr[i-1]
        # print(posArr)
        sumVal = sum([(i+1)*posArr[i] for i in range(len(posArr))])

        answer = sumVal
        for i in range(len(negArr)):
            # print(negNewArr[i],negArr[i],(i+1)*posSum, sumVal)
            if negNewArr[i]+negArr[i]+(i+1)*posSum+sumVal > answer:
                answer = negNewArr[i]+negArr[i]+(i+1)*posSum+sumVal

        return answer
