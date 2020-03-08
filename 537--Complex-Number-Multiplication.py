class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        [ar, ai] = a.split('+')
        [br, bi] = b.split('+')
        
        ai, bi = ai[:-1], bi[:-1]
        # print(ai, bi)
        
        cr = int(ar)*int(br) - int(ai)*int(bi)
        ci = int(ai)*int(br) + int(bi)*int(ar)
        
        answer = str(cr) + '+' + str(ci) + 'i'
        
        return answer
        