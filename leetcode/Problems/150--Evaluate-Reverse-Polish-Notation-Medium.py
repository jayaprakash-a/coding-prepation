class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for tok in tokens:
            # print(nums)
            if tok[1:].isdigit() and tok[0] == '-':
                nums.append(-1*int(tok[1:]))
            elif tok.isdigit():
                # print(tok)
                nums.append(int(tok))
            else:
                
                n1 = nums.pop()
                n2 = nums.pop()
                if tok == '+':
                    nums.append(n2+n1)
                elif tok == '-':
                    nums.append(n2-n1)
                elif tok == '*':
                    nums.append(n2*n1)
                elif tok == '/':
                    val = n2/n1
                    if val > 0:
                        nums.append(math.floor(val))
                    else:
                        nums.append(math.ceil(val))
        return nums[-1]