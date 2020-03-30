class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        arithmeticLengths = []
        prevSum = 0
        count = 0
        answer = 0
        for i in range(len(A)-1):
            if A[i+1]-A[i] == prevSum:
                count += 1
            else:
                if count >= 2:                    
                    answer += ((count-1)*(count))//2
                    # print(count, answer)
                prevSum = A[i+1]-A[i]
                count = 1
        if count >= 2:
            answer += ((count)*(count-1))//2
            # print(count, answer)
        return answer
        
        