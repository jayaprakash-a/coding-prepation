class Solution:
    def reformat(self, s: str) -> str:
        chars = []
        digits = []
        
        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                chars.append(ch)
        
        if abs(len(digits)-len(chars)) >= 2:
            return ''
        
        if len(digits) == len(chars) and s[0].isdigit():
            newStr = ''.join([chars[i]+digits[i] for i in range(len(chars))])
            return newStr
        elif len(digits) == len(chars):
            newStr = ''.join([digits[i]+chars[i] for i in range(len(chars))])
            return newStr
        if len(digits)>len(chars):
            newStr = ''.join([digits[i]+chars[i] for i in range(len(chars))])
            newStr += digits[-1]
        else :
            newStr = ''.join([chars[i]+digits[i] for i in range(len(digits))])
            newStr += chars[-1]
        

        return newStr