class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        ops = ['!', '&', '|']
        vals = []
        operations = []
        def assess(inp, op):
            ans = True
            if op == '&':
                ans = True
                for ch in inp:
                    ans = ans and(ch == 't')                
            elif op == '|':
                ans = False
                for ch in inp:
                    ans = ans or (ch == 't')
            elif op == '!':
                ans = (inp[0] != 't')
            if ans:
                return 't'
            else:
                return 'f'
        for ch in expression:
            if ch in ops:
                operations.append(ch)
            elif ch == ',':
                continue
            elif ch == ')':
                inp = []
                while(vals[-1] != '('):
                    inp.append(vals.pop())
                vals.pop()
                output = assess(inp, operations.pop())
                vals.append(output)
            else:
                vals.append(ch)
        
        return vals.pop() == 't'
                