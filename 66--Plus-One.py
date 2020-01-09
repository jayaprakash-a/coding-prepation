class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        index = len(digits) - 1
        carry = 0
        while(index >= 0):
            sum = digits[index] + carry
            if index == len(digits) - 1:
                sum += 1
            digits[index] = sum % 10
            if sum > 9:                
                carry = 1
            else:
                carry = 0
            
            index -= 1
                
        if carry == 1:
            digits.insert(0, 1)
        return digits
        