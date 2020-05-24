class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def vowCount(dict):
            return dict['a'] + dict['e'] + dict['i'] + dict['u'] + dict['o']
        vowels = collections.Counter(s[:k])
        maxVal = 0
        for i in range(k, len(s)):
            
            # print(vowels)
            maxVal = max(maxVal, vowCount(vowels))
            vowels[s[i]] += 1
            vowels[s[i-k]] -= 1
        maxVal = max(maxVal, vowCount(vowels))
        return maxVal
        