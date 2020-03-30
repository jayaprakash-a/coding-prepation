class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap = {}
        charSet = set()
        
        for i in range(len(s)):
            if s[i] not in charMap.keys():
                if t[i] in charSet:
                    return False
                charMap[s[i]] = t[i]
                charSet.add(t[i])
            else:
                if charMap[s[i]] != t[i]:
                    return False
        return True
        