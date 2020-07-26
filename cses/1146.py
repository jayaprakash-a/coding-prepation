def getAns(n):
    answer = {}
    answer[0] = 0
    answer[1] = 1
    answer[2] = 2
    answer[3] = 4
    def getVal(num):
        if num in answer:
            return answer[num]
        bitLength = len(bin(num)[2:])-1
        newNum = bitLength*(1 << (bitLength-1))
        twoPow = (1 << (bitLength) )- 1
        answer[twoPow] = newNum
        answer[num-twoPow-1] = getVal(num-twoPow-1)
        answer[num] = answer[twoPow] + (num-twoPow) + answer[num-twoPow-1]
        return answer[num]
    
    result =  getVal(n)
    print(answer)
    print(len(answer))
    return result
def main():
    n = int(input())
    print(getAns(n))
main()