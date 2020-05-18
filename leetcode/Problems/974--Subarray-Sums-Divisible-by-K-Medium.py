class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sumDict = collections.Counter()
        sumDict[0] = 1
        sumVal = 0
        answer = 0
        for num in A:
            sumVal = (sumVal+num)%K
            # if sumVal in sumDict.keys():
            # print('sumval, answer', sumVal, answer)
            answer += sumDict[sumVal]

            sumDict[sumVal] += 1
            

        return answer