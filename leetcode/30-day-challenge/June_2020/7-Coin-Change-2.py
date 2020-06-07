class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins)
        answer = [0]*(amount+1)
        answer[0] += 1
        for coin in coins:
            for i in range(1, amount+1):            
                if i >= coin:
                    answer[i] += answer[i-coin]
        return answer[-1]