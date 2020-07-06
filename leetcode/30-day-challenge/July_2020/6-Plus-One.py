class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            temp = (digits[i]+carry)%10
            carry = (digits[i]+carry)//10
            digits[i] = temp
        if not carry:
            return digits
        digits.insert(0, carry)
        return digits