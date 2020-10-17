class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        answer = [True]*(len(s)+1)
        for i in range(1, len(s) + 1):
            flag = True
            for j in range(i):                
                if answer[j] and s[j:i] in wordDict:
                    # answer[j] = append(True)
                    flag = False
                    break
            if flag:
                answer[i] = False
            
        return answer[-1]