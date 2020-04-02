class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        minLen = min(len(v1), len(v2))
        for i in range(minLen):
            if int(v1[i]) > int(v2[i]):
                return '1'
            elif int(v2[i]) > int(v1[i]):
                return '-1'
            
        for j in range(minLen, len(v1)):
            if int(v1[j]) != 0:
                return '1'
        for j in range(minLen, len(v2)):
            if int(v2[j]) != 0:
                return '-1'
        
        return 0
        