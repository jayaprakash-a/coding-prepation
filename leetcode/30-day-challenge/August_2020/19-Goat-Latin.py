class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        vowels = 'aeiouAEIOU'
        for i in range(len(words)):
            if words[i][0] not in vowels:
                words[i] = words[i][1:] + words[i][0]
            words[i] += 'ma'
            words[i] += ('a'*(i+1))
        return ' '.join(words)
            