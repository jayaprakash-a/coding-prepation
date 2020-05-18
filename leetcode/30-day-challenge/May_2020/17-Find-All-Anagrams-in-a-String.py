class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[:len(p)-1])
        answer = []
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1
            if pCounter == sCounter:
                answer.append(i-len(p)+1)
            
            sCounter[s[i-len(p)+1]] -= 1
            
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]
        return answer