class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = list(range(1, n//2+1))
        # for i in range(1, n//2 + 1):
        #     answer += [i, -1*i]
            # answer.append(-1*i)
        answer += list(range(-1, -1*(n//2+1), -1))
        if n%2 == 1:
            answer.append(0)
        
        return answer
            
        