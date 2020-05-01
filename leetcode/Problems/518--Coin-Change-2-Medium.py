class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        answer = [0]*(amount+1)
        answer[0] = 1
        
        for j in range(len(coins)):
            for i in range(1, amount+1):
                if i-coins[j]>=0:
                    answer[i] += (answer[i-coins[j]])
        return answer[-1]
