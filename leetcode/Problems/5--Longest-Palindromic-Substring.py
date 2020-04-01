class Solution:
    def expandBiDirection(self, s, left, right):
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        # print(s[left+1:right])
        return s[left+1:right]
        
    def longestPalindrome(self, s: str) -> str:

        maxLen = 0
        answer = ''
        for i in range(len(s)):
            ans1 = self.expandBiDirection(s, i, i)
            ans2 = self.expandBiDirection(s, i, i+1)
            
            maxVal = max(len(ans1), len(ans2))
            if maxVal > len(answer):
                if len(ans1) >= len(ans2):
                    answer = ans1
                else:
                    answer = ans2
                
        return answer
                
                