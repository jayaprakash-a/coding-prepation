class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(1, 11):
            for j in range(1, 11):
                if i+j>len(S):
                    continue
                else:
                    answer = self.checkSplit(S, i, j)
                    # print(S[:i], S[i:i+j], answer)
                    if len(answer) >= 2:
                        return answer
        return []
    def checkSplit(self, S, i, j):
        # print()
        x, y = S[:i], S[i:i+j]
        if int(x) > 2147483647 or int(y) > 2147483647 or (x[0] == '0' and len(x) > 1) or (y[0] == '0' and len(y) > 1):
            return []
        lastInd = i+j
        answer = [int(x), int(y)]
        while True:
            sumVal = int(x)+int(y)
            if len(str(sumVal)) > 10 or int(sumVal) > 2147483647:
                return []
            # print('check', i, j, 'values', x, y, lastInd, 'sum', sumVal, 'while', lastInd+len(str(sumVal)), S[lastInd:lastInd+len(str(sumVal))])
            if lastInd+len(str(sumVal)) > len(S):
                return []
            
            if S[lastInd:lastInd+len(str(sumVal))] != str(sumVal):
                return []
            else:
                answer.append(sumVal)
                lastInd += len(str(sumVal))
            if lastInd == len(S):
                return answer
            x, y = y, str(sumVal)
        return answer
        
    