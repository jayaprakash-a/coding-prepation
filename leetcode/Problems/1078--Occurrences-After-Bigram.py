class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        textWords = text.split(' ')
        answer = []
        for i in range(len(textWords) - 2):
            if textWords[i] == first and textWords[i+1] == second:
                answer.append(textWords[i+2])
                
        return answer
        