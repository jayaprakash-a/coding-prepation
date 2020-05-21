class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # print(str1, str2 )
        if str1 == str2:
            return str1
        elif str1 == '' or str2 == '':
            return ''
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        if str2 not in str1:
            return ''
        while(str2 in str1):
            str1 = str1.replace(str2, '')
        if str1 == '':
            return str2
        return self.gcdOfStrings(str2, str1)