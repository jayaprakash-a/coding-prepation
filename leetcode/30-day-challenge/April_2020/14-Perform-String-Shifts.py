class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        totLeftShift = 0
        length = len(s)
        
        for [dir, amount] in shift:
            if dir == 0:
                totLeftShift = (totLeftShift+amount)%length
            else:
                totLeftShift = (totLeftShift-amount)%length
        newStr = ['a']*length
        for i in range(length):
            newStr[(i-totLeftShift)%length] = s[i]
        
        
        return ''.join(newStr)