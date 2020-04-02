class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        
        numCount = [0]*10
        for i in range(len(secret)):
            numCount[int(secret[i])] += 1
            if secret[i] == guess[i]:
                bulls += 1
        
        for num in guess:
            if numCount[int(num)] > 0:
                numCount[int(num)] -= 1
                cows += 1
        
        return str(bulls)+'A'+str(cows-bulls)+'B'
        
        
        
        
        
        