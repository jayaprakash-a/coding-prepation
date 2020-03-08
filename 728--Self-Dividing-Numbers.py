class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for i in range(left, right+1):
            flag = True
            numStr = str(i)
            for ch in numStr:
                if ch != '0' and i % int(ch) == 0:
                    continue
                else:
                    flag = False
                    break
            if flag:
                answer.append(i)
        
        return answer
        