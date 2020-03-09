class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        aVal = "{:032b}".format(a)
        bVal = "{:032b}".format(b)
        cVal = "{:032b}".format(c)
        
        answer = 0
        
        for i in range(32):
            sum = int(aVal[i]) + int(bVal[i]) + int(cVal[i])
            if sum == 1:
                answer += 1
            elif sum == 2:
                if int(aVal[i]) + int(bVal[i]) == 2:
                    answer += 2
            
        return answer
                
                    
                
            
        