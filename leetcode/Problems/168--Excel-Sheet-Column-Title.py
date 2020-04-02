class Solution:
    def convertToTitle(self, n: int) -> str:
        
        n = n - 1
        if n < 26:
            # print(n)
            return chr(n+ord('A'))
        answer = []
        while (n // 26):
            answer.append(self.convertToTitle(n // 26))
            n = n - (n // 26 * 26)
        answer.append(chr(n+ord('A')))
        return ''.join(answer)
            
        