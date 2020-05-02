class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = len(s)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    # print(s[i:j+1])
                    answer += 1
        return answer
