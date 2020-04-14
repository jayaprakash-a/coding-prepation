class Solution:
    def getValStr(self, num, a, b, c):
        if num == 0:
            return ''
        if num == 4:
            return a+b
        if num == 9:
            return a+c
        if num < 4:
            return a*(num)
        else:
            return b+a*(num - 5)
    def intToRoman(self, num: int) -> str:
        thPlaceVal = num//1000
        num = num%1000
        hPlaceVal = num//100
        num = num%100
        tPlaceVal = num//10
        num = num%10
        
        onPlaceVal = num
        
        return thPlaceVal*'M'+self.getValStr(hPlaceVal, 'C','D','M')+self.getValStr(tPlaceVal, 'X','L','C')+self.getValStr(onPlaceVal, 'I','V','X')
        