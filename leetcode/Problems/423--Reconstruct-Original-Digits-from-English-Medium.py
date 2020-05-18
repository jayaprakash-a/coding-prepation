# zero, one, two, three, four, five, six, seven, eight, nine
class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0]*10
        
        for ch in s:
            if ch == 'z':
                count[0] += 1 # zero
            elif ch == 'w':
                count[2] += 1 # two
            elif ch == 'g':
                count[8] += 1 # eight
            elif ch == 'u':
                count[4] += 1 # four
            elif ch == 'x':
                count[6] += 1 # six
            elif ch == 'v':
                count[5] += 1 # five + seven
            elif ch == 's':
                count[7] += 1 # six + seven
            elif ch == 'o':
                count[1] += 1 # zero + one + two + four
            elif ch == 'r':
                count[3] += 1 # zero + three + four
            elif ch == 'i':
                count[9] += 1 # nine + six + eight + five
        
        count[7] -= count[6]
        count[5] -= count[7]
        count[1] -= (count[0]+count[2]+count[4])
        count[3] -= (count[0]+count[4])
        count[9] -= (count[6]+count[8]+count[5])
        answer = ''
        for i in range(len(count)):
            answer += (str(i)*count[i])
        return answer