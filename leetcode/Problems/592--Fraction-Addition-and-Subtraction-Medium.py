class Solution:
    def calc(self, op, pn, pd, n, d):
        if n == d == 0 and op == '-':
            return -1*pn, pd
        elif n == d == 0 and op == '+':
            return pn, pd
        if op == '+':
            return (d*pn + n*pd), (d*pd)
        else:
            return (d*pn - n*pd), (d*pd)
    
    def fractionAddition(self, exp: str) -> str:
        
        def processFrac(frac):
            [n, d] = map(int, frac.split('/'))
            if n == 0:
                return '0/1'
            def hcf(a, b):
                if a%b == 0:
                    return b
                return hcf(b, a%b)
            gcd = hcf(abs(n), d)
            n //= gcd
            d //= gcd
            return str(n) + '/' + str(d)
        
        fracs = ['0/1']
        ops = []
        index = 0
        prevInd = 0
        if exp[0] == '-':
            ops.append('-')
            index += 1
            prevInd += 1
        else:
            ops.append('+')
        
        for i in range(index, len(exp)):
            ch = exp[i]
            if ch == '-' or ch == '+':
                fracs.append(exp[prevInd:i])
                ops.append(ch)
                prevInd = i+1
        fracs.append(exp[prevInd:])
        
        prevFrac = fracs[0]
        
        for i in range(1, len(fracs)):
            currentFrac = fracs[i]
            [prevNum, prevDenom] = map(int, prevFrac.split('/'))
            [currNum, currDenom] = map(int, currentFrac.split('/'))            
            pn, pd = self.calc(ops[i-1], prevNum, prevDenom, currNum, currDenom)       
            prevFrac = str(pn) + '/' + str(pd)
            prevFrac = processFrac(prevFrac)
        
        

        prevFrac = processFrac(prevFrac)  
        return prevFrac