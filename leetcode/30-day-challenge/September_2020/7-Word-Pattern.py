class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map1, map2 = {}, {}
        string = str.split()
        if len(pattern) != len(string):
            return False
        for i in range(len(pattern)):
            if pattern[i] in map1 and string[i] != map1[pattern[i]]:
                return False
            if pattern[i] not in map1 and string[i] in map2:
                return False
            map1[pattern[i]] = string[i]
            map2[string[i]] = pattern[i]
        return True