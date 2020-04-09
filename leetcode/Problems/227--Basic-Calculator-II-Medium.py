class Solution:
    def getResult(self, op, n1, n2):
        if op == '+':
            return n1+n2
        elif op == '-':
            return n2-n1
        elif op == '*':
            return n2*n1
        elif op == '/':
            return n2//n1
        
    def calculate(self, s: str) -> int:
        precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        exp = s
        exp = exp.replace(' ', '')
        operatorStack = []
        valStack = []
        digitContinue = False
        for ch in exp:
            if ch == '(':
                digitContinue = False
                operatorStack.append(ch)
            elif ch.isdigit():
                if digitContinue:
                    topVal = valStack[-1]
                    num = 10*topVal + int(ch)
                    valStack[-1] = num
                else:
                    valStack.append(int(ch))
                digitContinue = True
            elif ch == ')':
                digitContinue = False
                while(operatorStack[-1] != '('):
                    operator = operatorStack.pop()
                    num1, num2 = valStack.pop(), valStack.pop()
                    valStack.append(self.getResult(operator, num1, num2))
                operatorStack.pop()
            else:
                digitContinue = False
                if len(operatorStack) == 0:
                    operatorStack.append(ch)
                else:
                    if operatorStack[-1] == '(':
                        operatorStack.append(ch)
                        continue
                    while(len(operatorStack) > 0 and operatorStack[-1] in precedence.keys() and precedence[ch] <= precedence[operatorStack[-1]]):
                        operator = operatorStack.pop()
                        num1, num2 = valStack.pop(), valStack.pop()
                        valStack.append(self.getResult(operator, num1, num2))
                    operatorStack.append(ch)
        while (len(operatorStack) > 0):
            operator = operatorStack.pop()
            num1, num2 = valStack.pop(), valStack.pop()
            valStack.append(self.getResult(operator, num1, num2))
        return valStack[-1]