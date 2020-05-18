class Solution:
    def maxDiff(self, num: int) -> int:
        intMap = {}
        num1 = list(str(num))
        num2 = list(str(num))
        d1, d2 = '9', '1'
        n1, n2 = ''.join(num1), ''.join(num2)
        for i in range(len(num1)):
            if num1[i] != '9':
                d1 = num1[i]
                num1[i] = '9'
                n1 = n1.replace(d1, '9')
                break
        
        
        if num2[0] == '1':
            for i in range(1, len(num2)):
                if num2[i] != '0' and num2[i] != '1':
                    d2 = num2[i]
                    num2[i] = '0'
                    n2 = n2.replace(d2, '0')
                    break
        else:
            d2 = num2[0]
            num2[0] = '1'
            n2 = n2.replace(d2, '1')

        answer = int(n1)-int(n2)
        return answer
            