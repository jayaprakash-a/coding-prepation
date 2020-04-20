class Solution:
    def toGoatLatin(self, S: str) -> str:
        if len(S) == 0:
            return S
        S = S.split(' ')
        vowels = 'aeiouAEIOU'
        for i in range(len(S)):
            if S[i][0] in vowels:
                S[i] += 'ma'
            else:
                S[i] = S[i][1:]+S[i][0] + 'ma'
            S[i] += 'a'*(i+1)
        return ' '.join(S)