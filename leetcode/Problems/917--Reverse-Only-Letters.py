class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        chars = ''
        string = list(S)
        for ch in S:
            if ch.isalpha():
                chars += ch
        index = len(chars) - 1
        for i in range(len(string)):
            if string[i].isalpha():
                string[i] = chars[index]
                index -= 1
        return ''.join(string)
            
        # print(chars)
        