import math
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        sum1 = num + 1
        answer = num+2
        v1 = int(math.sqrt(num+1)) + 1
        v2 = int(math.sqrt(num+2)) + 1
        
        answerval = [0, 0]
        f1, f2 = False, False
        while(v1 > 0 and v2 > 0):
            if (num+1) % v1 != 0:
                v1 -=1
            else:
                print('c1', v1, abs(v1 - (num+1)/v1), answer)
                if abs(v1 - (num+1)/v1) < answer:
                    answer = abs(v1 - (num+1)/v1) 
                    answerval[0], answerval[1]  = v1, int((num+1)/v1)
                    print('ans', answerval)
                else:
                    f1 = True
                v1 -=1
                    
            if (num+2) % v2 != 0:
                v2 -=1
            else:
                print('c2', v2, abs(v2 - (num+2)/v2), answer)
                if abs(v2 - (num+2)/v2) < answer:
                    answer = abs(v2 - (num+2)/v2)
                    answerval[0], answerval[1]  = v2, int((num+2)/v2)
                    print('ans', answerval)
                else:
                    f2 = True
                v2 -=1
            if f1 and f2:
                return sorted(answerval)
        
        return sorted(answerval)
            
            
            
                       
                      
            
        