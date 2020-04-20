class Solution:
    def __init__(self):
        self.answer = []
        self.charMap = {'2':'abc', '3':'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7':'pqrs', '8':'tuv', '9' : 'wxyz'}
   
    def genComb(self, digits, index, string):
        if index == len(digits):
            self.answer.append(string)
            return
        # print(index, digits)
        for i in range(len(self.charMap[digits[index]])):
            string += self.charMap[digits[index]][i]
            self.genComb(digits, index+1, string)
            string = string[:-1]
        return
    def letterCombinations(self, digits: str) -> List[str]:
        sampleAns = ''
        if len(digits) == 0:
            return []
        
        self.genComb(digits, 0, '')
        
        return self.answer
        
        
            